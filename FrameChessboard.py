import tkinter as tk


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
        self.pieces_position = {"a8": "r", "b8": "k", "c8": "b", "d8": "q", "e8": "ki", "f8": "b", "g8": "k", "h8": "r",
                                "a7": "p", "b7": "p", "c7": "p", "d7": "p", "e7": "p", "f7": "p", "g7": "p", "h7": "p",
                                "a2": "P", "b2": "P", "c2": "P", "d2": "P", "e2": "P", "f2": "P", "g2": "P", "h2": "P",
                                "a1": "R", "b1": "K", "c1": "B", "d1": "Q", "e1": "KI", "f1": "B", "g1": "K", "h1": "R"}
        self.current_color = ""
        ##################
        # this data is used to keep track of an
        # item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        self.board = tk.Canvas(self, width=500, height=500)
        self.board.pack()
        self.allow_pieces_to_move()

    def allow_pieces_to_move(self):
        # add bindings for clicking, dragging and releasing over
        # any object with the "piece" tag
        self.board.tag_bind("piece", "<ButtonPress-1>", self.on_piece_press)
        self.board.tag_bind("piece", "<ButtonRelease-1>", self.on_piece_release)
        self.board.tag_bind("piece", "<B1-Motion>", self.on_piece_motion)
        self.board.tag_bind("square", "<Motion>", self.highlight_square)

    def highlight_square(self, event):
        item = self.board.find_closest(event.x, event.y)
        try:
            item = self.board.find_overlapping(item)
        except:
            pass
        coordinates_of_square = self.board.coords(item)
        print(coordinates_of_square)
        # finds piece id number even by hovering on square.
        # print(self.board.find_enclosed(coordinates_of_square[0], coordinates_of_square[1], coordinates_of_square[2], coordinates_of_square[3]))
        self.board.itemconfig(item, activefill="#F9E79F")

    def allow_squres_to_highlight(self, event):
        # any object with the "piece" tag
        self.board.tag_bind("square", "<Motion>", self.on_piece_press)
        # add bindings for mouse hovering over board squares
        # get object closest to to current mouse position
        item = self.board.find_closest(event.x, event.y)
        # get 3d tag of the closest element
        current_piece = self.board.gettags(item)[2]
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
                self.board.itemconfig(item, fill=self.board.gettag(item2)[0])


    def start(self):
        self.menu()
        self.board_squares()
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
        # record the item and its location
        self._drag_data["item"] = self.board.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def on_piece_release(self, event):
        '''End drag of an object'''
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def on_piece_motion(self, event):
        '''Handle dragging of an object'''
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.board.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

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

    def board_squares(self):
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
                if number % 2 == 0:
                    if color_index % 2 != 0:
                        color = "white"
                    else:
                        color = "grey"
                else:
                    if color_index % 2 != 0:
                        color = "grey"
                    else:
                        color = "white"

                square_coords = letters[letter] + str(number)
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
            tk.Canvas.create_text(self.board, coordinates_of_element[0] + 10, coordinates_of_element[1] + 10,
                                  text=self.unicode_piece_symbols[self.pieces_position[coordinate]], font=("Arial", 30),
                                  activefill="green", tags="piece", anchor='nw')
