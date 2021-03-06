import tkinter as tk
from Chess.Game import Game
from Chess.Moves.Moves import Moves


class FrameChessboard(tk.Frame):
    def __init__(self, app, controller):
        tk.Frame.__init__(self, app)
        self.app = app
        self.controller = controller
        self.unicode_piece_symbols = {
            "R": u"♖", "r": u"♜",
            "K": u"♘", "k": u"♞",
            "B": u"♗", "b": u"♝",
            "Q": u"♕", "q": u"♛",
            "KI": u"♔", "ki": u"♚",
            "P": u"♙", "p": u"♟",
        }
        self.current_board_colors = {}
        self.game = Game()
        self.pieces_position = self.game.pieces_position

        # this data is used to keep track of an item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        self.board = tk.Canvas(self, width=800, height=800)
        self.board.pack()
        self.allow_pieces_to_move(self.game.player_moving)
        self.piece_moving = None
        self.piece_moving_start_coordinates = []
        self.piece_moving_start_tag_position = None
        self.piece_moving_end_tag_position = None

    def tag_unbind(self, old_player):
        self.board.tag_unbind("{}_piece".format(old_player), "<ButtonPress-1>")
        self.board.tag_unbind("{}_piece".format(old_player), "<ButtonRelease-1>")
        self.board.tag_unbind("{}_piece".format(old_player), "<B1-Motion>")

    def allow_pieces_to_move(self, current_player):
        # add bindings for clicking, dragging and releasing over any object with the "piece" tag
        self.board.tag_bind("{}_piece".format(current_player), "<ButtonPress-1>", self.on_piece_press)
        self.board.tag_bind("{}_piece".format(current_player), "<ButtonRelease-1>", self.on_piece_release)
        self.board.tag_bind("{}_piece".format(current_player), "<B1-Motion>", self.on_piece_motion)
        # self.board.tag_bind("square", "<Motion>", self.highlight_square)

    def print_piece_coordinates(self, event):
        item = self.board.find_closest(event.x, event.y)
        coordinates_of_square = self.board.coords(item)
        print(coordinates_of_square)

    def highlight_square(self, event):
        item = self.board.find_closest(event.x, event.y)
        coordinates_of_square = self.board.coords(item)
        # print(coordinates_of_square)
        # finds piece id number even by hovering on square.
        self.board.itemconfig(item, activefill="#F9E79F")

    def start(self):
        self.menu()
        self.draw_chessboard()
        self.show_default_pieces()

    def menu(self):
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.controller.config(menu=self.menubar)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)
        self.filemenu.add_command(label="Quit", command=self.controller.destroy)
        self.filemenu.add_command(label="New Game", command=self.controller.destroy)
        # self.filemenu.add_command(label="Undo move", command=self.controller.destroy)
        # self.filemenu.add_command(label="Redo move", command=self.controller.destroy)

    def on_piece_press(self, event):
        '''Begining drag of an object'''
        adjusted_coordinates = self.adjust_current_piece_coords(self.find_current_square_coords(event.x, event.y))
        adjusted_x = adjusted_coordinates[0]
        adjusted_y = adjusted_coordinates[1]
        # record the item and its location
        self._drag_data["item"] = self.board.find_closest(event.x, event.y)[0]
        self.piece_moving = self.board.gettags(self._drag_data["item"])[1]
        self.piece_moving_start_tag_position = self.find_current_square_tag_coordinates(event.x, event.y)
        self.piece_moving_start_coordinates = [adjusted_x, adjusted_y]
        self.highlight_moves_by_clicking_on_piece(piece_moving=self.piece_moving, start_tag=self.piece_moving_start_tag_position)
        # print("piece moving: {}".format(self.piece_moving))
        # print("piece moving start position: {}".format(self.piece_moving_start_position))
        self._drag_data["x"] = adjusted_x
        self._drag_data["y"] = adjusted_y

    def find_piece_on_given_square(self, square_tag_coordinates):
        square = self.board.find_withtag(square_tag_coordinates)
        coordinates_of_square = self.board.coords(square)
        enclosed_objects = self.board.find_enclosed(coordinates_of_square[0], coordinates_of_square[1],
                                                    coordinates_of_square[2], coordinates_of_square[3])
        for item in enclosed_objects:
            if self.piece_moving.islower():
                try:
                    if self.board.gettags(item)[1].isupper():
                        return item
                except IndexError:
                    pass
            else:
                try:
                    if self.board.gettags(item)[1].islower():
                        return item
                except IndexError:
                    pass

    def remove_taken_piece_from_board(self, end_square_coordinate):
        taken_piece = self.find_piece_on_given_square(end_square_coordinate)
        self.board.delete(taken_piece)

    def on_piece_release(self, event):
        print(f"piece moving: {self.piece_moving}")
        print(f"start tag position: {self.piece_moving_start_tag_position}")
        print(f"end position tag: {self.piece_moving_end_tag_position}")
        self.game.temporary_update_pieces_position_next_turn(self.piece_moving, self.piece_moving_start_tag_position,
                                                             self.piece_moving_end_tag_position)
        if ((self.game.is_end_position_free_or_with_opponent_piece(
                self.piece_moving, self.piece_moving_end_tag_position)) and (
                Moves().move_is_possible(piece=self.piece_moving, start_tag=self.piece_moving_start_tag_position,
                                         end_tag=self.piece_moving_end_tag_position,
                                         all_turns_pieces_position=self.game.pieces_configurations_of_all_turns,
                                         max_turn=self.game.moves_done))):
            print("move possible")
            if self.piece_moving.lower() == "p":
                en_passant = Moves().get_piece_class(self.piece_moving).en_passant(
                    self.piece_moving_start_tag_position, self.game.pieces_configurations_of_all_turns,
                    self.game.moves_done)
                if self.piece_moving_end_tag_position in en_passant.keys():
                    if self.game.temporary_update_pieces_position_next_turn(
                            self.piece_moving, self.piece_moving_start_tag_position,
                            self.piece_moving_end_tag_position, en_passant[self.piece_moving_end_tag_position]):
                        self.remove_taken_piece_from_board(en_passant[self.piece_moving_end_tag_position])
                else:
                    self.remove_taken_piece_from_board(self.piece_moving_end_tag_position)
            else:
                if self.game.temporary_update_pieces_position_next_turn(
                        self.piece_moving, self.piece_moving_start_tag_position, self.piece_moving_end_tag_position):
                    self.remove_taken_piece_from_board(self.piece_moving_end_tag_position)
            self.piece_moving = None
            self.piece_moving_start_tag_position = None
            self.piece_moving_end_tag_position = None
            self.disable_moves_for_old_player_and_enable_for_new()
        else:
            print("move not possible")
            self.put_piece_where_it_was()
            del self.game.pieces_configurations_of_all_turns[self.game.moves_done + 1]
        '''End drag of an object'''
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
        for square_color_changed in self.current_board_colors.keys():
            square = self.board.find_withtag(square_color_changed)
            self.board.itemconfig(square, fill=self.current_board_colors[square_color_changed])
        self.current_board_colors = {}

    def disable_moves_for_old_player_and_enable_for_new(self):
        old_player = self.game.player_moving
        self.tag_unbind(old_player)
        new_player = self.game.update_current_player()
        self.allow_pieces_to_move(new_player)

    def find_current_square_tag_coordinates(self, x, y):
        for item in self.board.find_withtag("square"):
            if self.board.coords(item)[0] <= x <= self.board.coords(item)[2] and self.board.coords(item)[1] <= y <= self.board.coords(item)[3]:
                tag_coords_of_current_square = self.board.gettags(item)[1]
                # print(tag_coords_of_current_square)
                # print(self.board.coords(item))
                # print(self.board.gettags("current"))
                # print(self.board.coords("current"))
                return tag_coords_of_current_square

    def find_current_square_coords(self, x, y):
        for item in self.board.find_withtag("square"):
            if self.board.coords(item)[0] <= x <= self.board.coords(item)[2] and self.board.coords(item)[1] <= y <= self.board.coords(item)[3]:
                coords_of_current_square = self.board.coords(item)
                # print(self.board.gettags(item))
                # print(self.board.coords(item))
                # print(self.board.gettags("current"))
                # print(self.board.coords("current"))
                return coords_of_current_square

    def adjust_current_piece_coords(self, coordinates):
        return [coordinates[0] + 30, coordinates[1] + 30]

    def put_piece_where_it_was(self):
        # compute how much the mouse has moved
        delta_x = self.piece_moving_start_coordinates[0] - self._drag_data["x"]
        delta_y = self.piece_moving_start_coordinates[1] - self._drag_data["y"]
        # move the object the appropriate amount
        self.board.move(self._drag_data["item"], delta_x, delta_y)

    def on_piece_motion(self, event):
        '''Handle dragging of an object'''
        adjusted_coordinates = self.adjust_current_piece_coords(self.find_current_square_coords(event.x, event.y))
        self.piece_moving_end_tag_position = self.find_current_square_tag_coordinates(event.x, event.y)
        adjusted_x = adjusted_coordinates[0]
        adjusted_y = adjusted_coordinates[1]
        # compute how much the mouse has moved
        delta_x = adjusted_x - self._drag_data["x"]
        delta_y = adjusted_y - self._drag_data["y"]
        # move the object the appropriate amount
        self.board.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = adjusted_coordinates[0]
        self._drag_data["y"] = adjusted_coordinates[1]

    def highlight_moves_by_clicking_on_piece(self, piece_moving, start_tag):
        all_moves_possible = Moves().get_all_possible_moves(
            piece=piece_moving, start_tag=start_tag, all_turns_pieces_position=self.game.pieces_configurations_of_all_turns,
            max_turn=self.game.moves_done)
        self.current_board_colors = {}
        for coordinate in all_moves_possible:
            square = self.board.find_withtag(coordinate)
            current_color = self.board.itemcget(square, 'fill')
            self.current_board_colors[coordinate] = current_color
            self.board.itemconfig(square, fill="#F9E79F")

    def draw_chessboard(self):
        # DRAW CHESSBOARD
        # coordinates[0]: start space from left. at every letter (a-h) += 62.5. start = 0. resets at every num
        # coordinates[1]: start space from top. at every row (number) += 62.5. start = 0. never resets.
        # coordinates[2]: till where: width. at every column (letter): += 62.5. start = 62.5. reset at every num.
        # coordinates[3]: till where: height. at every row (number): += 62.5. start = 62.5. never resets.
        coordinates = [0, 0, 62.5, 62.5]
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        color_index = 1
        for number in range(1, 9):
            coordinates[0] = 0
            coordinates[2] = 62.5
            for letter in range(8):
                # decide square color
                if number % 2 != 0:
                    if color_index % 2 != 0:
                        color = "white"
                    else:
                        color = "grey"
                else:
                    if color_index % 2 != 0:
                        color = "grey"
                    else:
                        color = "white"

                square_coords = letters[letter] + str(9 - number)
                tk.Canvas.create_rectangle(self.board, coordinates[0], coordinates[1], coordinates[2], coordinates[3],
                                           fill=color, tags=("square", square_coords))
                # write small coordinates in initial squares
                if letter == 0:
                    tk.Canvas.create_text(self.board, coordinates[0] + 10, coordinates[1] + 10, text=str(9 - number),
                                          font=("Arial", 10))
                if number == 8:
                    tk.Canvas.create_text(self.board, coordinates[2] - 10, coordinates[3] - 10, text=letters[letter],
                                          font=("Arial", 10))
                coordinates[0] += 62.5
                coordinates[2] += 62.5
                color_index += 1
            coordinates[1] += 62.5
            coordinates[3] += 62.5

    def show_default_pieces(self):
        for coordinate in self.pieces_position.keys():
            canvas_element = self.board.find_withtag(coordinate)
            coordinates_of_element = self.board.coords(canvas_element)
            piece_name = self.unicode_piece_symbols[self.pieces_position[coordinate]]
            piece_color = "white" if self.pieces_position[coordinate].isupper() else "black"
            piece_color_tag = "{}_piece".format(piece_color)
            tk.Canvas.create_text(self.board, coordinates_of_element[0] + 30, coordinates_of_element[1] + 30,
                                  text=piece_name, font=("Arial", 30), activefill="green",
                                  tags=(piece_color_tag, self.pieces_position[coordinate]), width="30")
