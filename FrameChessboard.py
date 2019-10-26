import tkinter as tk
from Game import *


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
        self.game = Game()
        self.pieces_position = self.game.pieces_position

        # this data is used to keep track of an item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        self.board = tk.Canvas(self, width=500, height=500)
        self.board.pack()
        self.allow_pieces_to_move(self.game.player_moving)

    def tag_unbind(self, old_player):
        self.board.tag_unbind("{}_piece".format(old_player), "<ButtonPress-1>")
        self.board.tag_unbind("{}_piece".format(old_player), "<ButtonRelease-1>")
        self.board.tag_unbind("{}_piece".format(old_player), "<B1-Motion>")

    def allow_pieces_to_move(self, current_player):
        print("current player: {}".format(current_player))
        # add bindings for clicking, dragging and releasing over any object with the "piece" tag
        self.board.tag_bind("{}_piece".format(current_player), "<ButtonPress-1>", self.on_piece_press)
        self.board.tag_bind("{}_piece".format(current_player), "<ButtonRelease-1>", self.on_piece_release)
        self.board.tag_bind("{}_piece".format(current_player), "<B1-Motion>", self.on_piece_motion)
        self.board.tag_bind("square", "<Motion>", self.highlight_square)

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

    def on_piece_press(self, event):
        '''Begining drag of an object'''
        adjusted_coordinates = self.adjust_current_piece_coords(self.find_current_square_coords(event.x, event.y))
        adjusted_x = adjusted_coordinates[0]
        adjusted_y = adjusted_coordinates[1]
        # record the item and its location
        self._drag_data["item"] = self.board.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = adjusted_x
        self._drag_data["y"] = adjusted_y

    def on_piece_release(self, event):
        '''End drag of an object'''
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0
        self.disable_moves_for_old_player_and_enable_for_new()
         
    def disable_moves_for_old_player_and_enable_for_new(self):
        # check that move has actually occurred
        # if move successful --> update turn
        old_player = self.game.player_moving
        self.tag_unbind(old_player)
        new_player = self.game.update_current_player()
        self.allow_pieces_to_move(new_player)

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

    def on_piece_motion(self, event):
        '''Handle dragging of an object'''
        adjusted_coordinates = self.adjust_current_piece_coords(self.find_current_square_coords(event.x, event.y))
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

    def highlight_moves_by_clicking_on_square(self, event):
        # get object closest to to current mouse position
        item2 = self.board.find_closest(event.x, event.y)
        # get 3d tag of the closest element
        current_piece = self.board.gettags(item2)[2]
        # item = highlighted piece
        # item = self.frames["FrameChessboard"].a7

        if current_piece == "rook" and 'a7' in self.board.gettags(item)[0]:
            # get current color of the square
            current_color = self.board.itemcget(item, 'fill')
            # if current square is not highlighted
            if current_color == 'grey' or current_color == "white":
                # highlight square
                self.board.itemconfig(item, fill='green')
            else:
                # if it was already highlighted, set it back to its original color
                self.board.itemconfig(item, fill=self.board.gettags(item2)[1])

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
