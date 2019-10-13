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
        self.current_color = ""
        ##################
        # this data is used to keep track of an
        # item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        self.board = tk.Canvas(self, width=500, height=500)
        self.board.pack()
        # add bindings for clicking, dragging and releasing over
        # any object with the "token" tag
        self.board.tag_bind("piece", "<ButtonPress-1>", self.on_piece_press)
        self.board.tag_bind("piece", "<ButtonRelease-1>", self.on_piece_release)
        self.board.tag_bind("piece", "<B1-Motion>", self.on_piece_motion)

    def start(self):
        self.controller.show_frame(FrameChessboard)
        # show board and menu
        self.menu()
        self.board_squares()
        self.show_default_pieces()

    def menu(self):
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.controller.config(menu=self.menubar)
        self.filemenu.add_command(label="Quit", command=self.controller.destroy)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)

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

    def board_squares(self):
        # DRAW CHESSBOARD
        # (starting space from left, start space from top, till where (width), till where (height)
        # tags: square coordinates, square color, current piece, owner current piece

        self.a8 = tk.Canvas.create_rectangle(self.board, 0, 0, 62.5, 62.5, fill="white",
                                             tag=("a8", "white", "rook", "blacks"))

        self.b8 = tk.Canvas.create_rectangle(self.board, 62.5, 0, 125, 62.5, fill="grey",
                                             tag=("b8", "grey", "knight", "blacks"))
        self.c8 = tk.Canvas.create_rectangle(self.board, 125, 0, 187.5, 62.5, fill="white",
                                             tag=("c8", "white", "bishop", "blacks"))
        self.d8 = tk.Canvas.create_rectangle(self.board, 187.5, 0, 250, 62.5, fill="grey",
                                             tag=("d8", "grey", "queen", "blacks"))
        self.e8 = tk.Canvas.create_rectangle(self.board, 250, 1, 312.5, 62.5, fill="white",
                                             tag=("e8", "white", "king", "blacks"))
        self.f8 = tk.Canvas.create_rectangle(self.board, 312.5, 0, 375, 62.5, fill="grey",
                                             tag=("f8", "grey", "bishop", "blacks"))
        self.g8 = tk.Canvas.create_rectangle(self.board, 375, 0, 437, 62.5, fill="white",
                                             tag=("g8", "white", "knight", "blacks"))
        self.h8 = tk.Canvas.create_rectangle(self.board, 437, 0, 500, 62.5, fill="grey",
                                             tag=("h8", "grey", "rook", "blacks"))

        self.a7 = tk.Canvas.create_rectangle(self.board, 0, 62.5, 62.5, 125, fill="grey",
                                             tag=("a7", "grey", "pawn", "blacks"))
        self.b7 = tk.Canvas.create_rectangle(self.board, 62.5, 62.5, 125, 125, fill="white",
                                             tag=("b7", "white", "pawn", "blacks"))
        self.c7 = tk.Canvas.create_rectangle(self.board, 125, 62.5, 187.5, 125, fill="grey",
                                             tag=("c7", "grey", "pawn", "blacks"))
        self.d7 = tk.Canvas.create_rectangle(self.board, 187.5, 62.5, 250, 125, fill="white",
                                             tag=("d7", "white", "pawn", "blacks"))
        self.e7 = tk.Canvas.create_rectangle(self.board, 250, 62.5, 312.5, 125, fill="grey",
                                             tag=("e7", "grey", "pawn", "blacks"))
        self.f7 = tk.Canvas.create_rectangle(self.board, 312.5, 62.5, 375, 125, fill="white",
                                             tag=("f7", "white", "pawn", "blacks"))
        self.g7 = tk.Canvas.create_rectangle(self.board, 375, 62.5, 437, 125, fill="grey",
                                             tag=("g7", "grey", "pawn", "blacks"))
        self.h7 = tk.Canvas.create_rectangle(self.board, 437, 62.5, 500, 125, fill="white",
                                             tag=("h7", "white", "pawn", "blacks"))

        self.a6 = tk.Canvas.create_rectangle(self.board, 0, 125, 62.5, 187.5, fill="white",
                                             tag=("a6", "white", None, None))
        self.b6 = tk.Canvas.create_rectangle(self.board, 62.5, 125, 125, 187.5, fill="grey",
                                             tag=("b6", "grey", None, None))
        self.c6 = tk.Canvas.create_rectangle(self.board, 125, 125, 187.5, 187.5, fill="white",
                                             tag=("c6", "white", None, None))
        self.d6 = tk.Canvas.create_rectangle(self.board, 187.5, 125, 250, 187.5, fill="grey",
                                             tag=("d6", "grey", None, None))
        self.e6 = tk.Canvas.create_rectangle(self.board, 250, 125, 312.5, 187.5, fill="white",
                                             tag=("e6", "white", None, None))
        self.f6 = tk.Canvas.create_rectangle(self.board, 312.5, 125, 375, 187.5, fill="grey",
                                             tag=("f6", "grey", None, None))
        self.g6 = tk.Canvas.create_rectangle(self.board, 375, 125, 437, 187.5, fill="white",
                                             tag=("g6", "white", None, None))
        self.h6 = tk.Canvas.create_rectangle(self.board, 437, 125, 500, 187.5, fill="grey",
                                             tag=("h6", "grey", None, None))

        self.a5 = tk.Canvas.create_rectangle(self.board, 0, 187.5, 62.5, 250, fill="grey",
                                             tag=("a5", "grey", None, None))
        self.b5 = tk.Canvas.create_rectangle(self.board, 62.5, 187.5, 125, 250, fill="white",
                                             tag=("b5", "white", None, None))
        self.c5 = tk.Canvas.create_rectangle(self.board, 125, 187.5, 187.5, 250, fill="grey",
                                             tag=("c5", "grey", None, None))
        self.d5 = tk.Canvas.create_rectangle(self.board, 187.5, 187.5, 250, 250, fill="white",
                                             tag=("d5", "white", None, None))
        self.e5 = tk.Canvas.create_rectangle(self.board, 250, 187.5, 312.5, 250, fill="grey",
                                             tag=("e5", "grey", None, None))
        self.f5 = tk.Canvas.create_rectangle(self.board, 312.5, 187.5, 375, 250, fill="white",
                                             tag=("f5", "white", None, None))
        self.g5 = tk.Canvas.create_rectangle(self.board, 375, 187.5, 437, 250, fill="grey",
                                             tag=("g5", "grey", None, None))
        self.h5 = tk.Canvas.create_rectangle(self.board, 437, 187.5, 500, 250, fill="white",
                                             tag=("h5", "white", None, None))

        self.a4 = tk.Canvas.create_rectangle(self.board, 0, 250, 62.5, 312.5, fill="white",
                                             tag=("a4", "white", None, None))
        self.b4 = tk.Canvas.create_rectangle(self.board, 62.5, 250, 125, 312.5, fill="grey",
                                             tag=("b4", "grey", None, None))
        self.c4 = tk.Canvas.create_rectangle(self.board, 125, 250, 187.5, 312.5, fill="white",
                                             tag=("c4", "white", None, None))
        self.d4 = tk.Canvas.create_rectangle(self.board, 187.5, 250, 250, 312.5, fill="grey",
                                             tag=("d4", "grey", None, None))
        self.e4 = tk.Canvas.create_rectangle(self.board, 250, 250, 312.5, 312.5, fill="white",
                                             tag=("e4", "white", None, None))
        self.f4 = tk.Canvas.create_rectangle(self.board, 312.5, 250, 375, 312.5, fill="grey",
                                             tag=("f4", "grey", None, None))
        self.g4 = tk.Canvas.create_rectangle(self.board, 375, 250, 437, 312.5, fill="white",
                                             tag=("g4", "white", None, None))
        self.h4 = tk.Canvas.create_rectangle(self.board, 437, 250, 500, 312.5, fill="grey",
                                             tag=("h4", "grey", None, None))

        self.a3 = tk.Canvas.create_rectangle(self.board, 0, 312.5, 62.5, 375, fill="grey",
                                             tag=("a3", "grey", None, None))
        self.b3 = tk.Canvas.create_rectangle(self.board, 62.5, 312.5, 125, 375, fill="white",
                                             tag=("b3", "white", None, None))
        self.c3 = tk.Canvas.create_rectangle(self.board, 125, 312.5, 187.5, 375, fill="grey",
                                             tag=("c3", "grey", None, None))
        self.d3 = tk.Canvas.create_rectangle(self.board, 187.5, 312.5, 250, 375, fill="white",
                                             tag=("d3", "white", None, None))
        self.e3 = tk.Canvas.create_rectangle(self.board, 250, 312.5, 312.5, 375, fill="grey",
                                             tag=("e3", "grey", None, None))
        self.f3 = tk.Canvas.create_rectangle(self.board, 312.5, 312.5, 375, 375, fill="white",
                                             tag=("f3", "white", None, None))
        self.g3 = tk.Canvas.create_rectangle(self.board, 375, 312.5, 437, 375, fill="grey",
                                             tag=("g3", "grey", None, None))
        self.h3 = tk.Canvas.create_rectangle(self.board, 437, 312.5, 500, 375, fill="white",
                                             tag=("h3", "white", None, None))

        self.a2 = tk.Canvas.create_rectangle(self.board, 0, 375, 62.5, 437, fill="white",
                                             tag=("a2", "white", "pawn", "whites"))
        self.b2 = tk.Canvas.create_rectangle(self.board, 62.5, 375, 125, 437, fill="grey",
                                             tag=("b2", "grey", "pawn", "whites"))
        self.c2 = tk.Canvas.create_rectangle(self.board, 125, 375, 187.5, 437, fill="white",
                                             tag=("c2", "white", "pawn", "whites"))
        self.d2 = tk.Canvas.create_rectangle(self.board, 187.5, 375, 250, 437, fill="grey",
                                             tag=("d2", "grey", "pawn", "whites"))
        self.e2 = tk.Canvas.create_rectangle(self.board, 250, 375, 312.5, 437, fill="white",
                                             tag=("e2", "white", "pawn", "whites"))
        self.f2 = tk.Canvas.create_rectangle(self.board, 312.5, 375, 375, 437, fill="grey",
                                             tag=("f2", "grey", "pawn", "whites"))
        self.g2 = tk.Canvas.create_rectangle(self.board, 375, 375, 437, 437, fill="white",
                                             tag=("g2", "white", "pawn", "whites"))
        self.h2 = tk.Canvas.create_rectangle(self.board, 437, 375, 500, 437, fill="grey",
                                             tag=("h2", "grey", "pawn", "whites"))

        self.a1 = tk.Canvas.create_rectangle(self.board, 0, 437, 62.5, 500, fill="grey",
                                             tag=("a1", "grey", "rook", "whites"))
        self.b1 = tk.Canvas.create_rectangle(self.board, 62.5, 437, 125, 500, fill="white",
                                             tag=("b1", "white", "knight", "whites"))
        self.c1 = tk.Canvas.create_rectangle(self.board, 125, 437, 187.5, 500, fill="grey",
                                             tag=("c1", "grey", "bishop", "whites"))
        self.d1 = tk.Canvas.create_rectangle(self.board, 187.5, 437, 250, 500, fill="white",
                                             tag=("d1", "white", "queen", "whites"))
        self.e1 = tk.Canvas.create_rectangle(self.board, 250, 437, 312.5, 500, fill="grey",
                                             tag=("e1", "grey", "king", "whites"))
        self.f1 = tk.Canvas.create_rectangle(self.board, 312.5, 437, 375, 500, fill="white",
                                             tag=("f1", "white", "bishop", "whites"))
        self.g1 = tk.Canvas.create_rectangle(self.board, 375, 437, 437, 500, fill="grey",
                                             tag=("g1", "grey", "knight", "whites"))
        self.h1 = tk.Canvas.create_rectangle(self.board, 437, 437, 500, 500, fill="white",
                                            tag=("h1", "white", "rook", "whites"))

    def show_default_pieces(self):
        # empty pieces are set by default to be changed later on during the game
        # tags: piece coordinates, piece owner, piece
        # BLACKS
        self.a8_piece = tk.Canvas.create_text(self.board, 30, 30, text=self.unicode_piece_symbols["r"], font=("Arial", 30),
                                              tag=("a8", "blacks", "rook"), activefill="green", tags="piece")
        self.b8_piece = tk.Canvas.create_text(self.board, 92, 30, text=self.unicode_piece_symbols["k"], font=("Arial", 30),
                                              tag=("a8", "blacks", "knight"), activefill="green", tags="piece")
        self.c8_piece = tk.Canvas.create_text(self.board, 157, 30, text=self.unicode_piece_symbols["b"], font=("Arial", 30),
                                              tag=("a8", "blacks", "bishop"), activefill="green", tags="piece")
        self.d8_piece = tk.Canvas.create_text(self.board, 218, 30, text=self.unicode_piece_symbols["q"], font=("Arial", 30),
                                              tag=("a8", "blacks", "queen"), activefill="green", tags="piece")
        self.e8_piece = tk.Canvas.create_text(self.board, 280, 30, text=self.unicode_piece_symbols["ki"], font=("Arial", 30),
                                              tag=("a8", "blacks", "king"), activefill="green", tags="piece")
        self.f8_piece = tk.Canvas.create_text(self.board, 343, 30, text=self.unicode_piece_symbols["b"], font=("Arial", 30),
                                              tag=("a8", "blacks", "bishop"), activefill="green", tags="piece")
        self.g8_piece = tk.Canvas.create_text(self.board, 403, 30, text=self.unicode_piece_symbols["k"], font=("Arial", 30),
                                              tag=("a8", "blacks", "knight"), activefill="green", tags="piece")
        self.h8_piece = tk.Canvas.create_text(self.board, 469, 30, text=self.unicode_piece_symbols["r"], font=("Arial", 30),
                                              tag=("h8", "blacks", "rook"), activefill="green", tags="piece")

        self.a7_piece = tk.Canvas.create_text(self.board, 32, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30),
                                              tag=("a7", "blacks", "pawn"), activefill="green", tags="piece")
        self.b7_piece = tk.Canvas.create_text(self.board, 94, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30),
                                              tag=("b7", "blacks", "pawn"), activefill="green", tags="piece")
        self.c7_piece = tk.Canvas.create_text(self.board, 157, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30),
                                              tag=("c7", "blacks", "pawn"), activefill="green", tags="piece")
        self.d7_piece = tk.Canvas.create_text(self.board, 218, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30),
                                              tag=("d7", "blacks", "pawn"), activefill="green", tags="piece")
        self.e7_piece = tk.Canvas.create_text(self.board, 282, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30),
                                              tag=("e7", "blacks", "pawn"), activefill="green", tags="piece")
        self.f7_piece = tk.Canvas.create_text(self.board, 343, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30),
                                              tag=("f7", "blacks", "pawn"), activefill="green", tags="piece")
        self.g7_piece = tk.Canvas.create_text(self.board, 406, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30),
                                              tag=("g7", "blacks", "pawn"), activefill="green", tags="piece")
        self.h7_piece = tk.Canvas.create_text(self.board, 469, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30),
                                              tag=("h7", "blacks", "pawn"), activefill="green", tags="piece")

        self.a6_piece = tk.Canvas.create_text(self.board, 32, 160, text=None,
                                              font=("Arial", 30), tag=("a6", None, None), activefill="green", tags="piece")
        self.b6_piece = tk.Canvas.create_text(self.board, 94, 160, text=None,
                                              font=("Arial", 30), tag=("b6", None, None), activefill="green", tags="piece")
        self.c6_piece = tk.Canvas.create_text(self.board, 157, 160, text=None,
                                              font=("Arial", 30), tag=("c6", None, None), activefill="green", tags="piece")
        self.d6_piece = tk.Canvas.create_text(self.board, 218, 160, text=None,
                                              font=("Arial", 30), tag=("d6", None, None), activefill="green", tags="piece")
        self.e6_piece = tk.Canvas.create_text(self.board, 282, 160, text=None,
                                              font=("Arial", 30), tag=("e6", None, None), activefill="green", tags="piece")
        self.f6_piece = tk.Canvas.create_text(self.board, 343, 160, text=None,
                                              font=("Arial", 30), tag=("f6", None, None), activefill="green", tags="piece")
        self.g6_piece = tk.Canvas.create_text(self.board, 406, 160, text=None,
                                              font=("Arial", 30),  tag=("g6", None, None), activefill="green", tags="piece")
        self.h6_piece = tk.Canvas.create_text(self.board, 469, 160, text=None,
                                              font=("Arial", 30), tag=("h6", None, None), activefill="green", tags="piece")

        self.a5_piece = tk.Canvas.create_text(self.board, 32, 220, text=None,
                                              font=("Arial", 30), tag=("a5", None, None), activefill="green", tags="piece")
        self.b5_piece = tk.Canvas.create_text(self.board, 94, 220, text=None,
                                              font=("Arial", 30), tag=("b5", None, None), activefill="green", tags="piece")
        self.c5_piece = tk.Canvas.create_text(self.board, 157, 220, text=None,
                                              font=("Arial", 30), tag=("c5", None, None), activefill="green", tags="piece")
        self.d5_piece = tk.Canvas.create_text(self.board, 218, 220, text=None,
                                              font=("Arial", 30), tag=("d5", None, None), activefill="green", tags="piece")
        self.e5_piece = tk.Canvas.create_text(self.board, 282, 220, text=None,
                                              font=("Arial", 30), tag=("e5", None, None), activefill="green", tags="piece")
        self.f5_piece = tk.Canvas.create_text(self.board, 343, 220, text=None,
                                              font=("Arial", 30), tag=("f5", None, None), activefill="green", tags="piece")
        self.g5_piece = tk.Canvas.create_text(self.board, 406, 220, text=None,
                                              font=("Arial", 30), tag=("g5", None, None), activefill="green", tags="piece")
        self.h5_piece = tk.Canvas.create_text(self.board, 469, 220, text=None,
                                              font=("Arial", 30), tag=("h5", None, None), activefill="green", tags="piece")

        self.a4_piece = tk.Canvas.create_text(self.board, 32, 283, text=None,
                                              font=("Arial", 30), tag=("a4", None, None), activefill="green", tags="piece")
        self.b4_piece = tk.Canvas.create_text(self.board, 94, 283, text=None,
                                              font=("Arial", 30), tag=("b4", None, None), activefill="green", tags="piece")
        self.c4_piece = tk.Canvas.create_text(self.board, 157, 283, text=None,
                                              font=("Arial", 30), tag=("c4", None, None), activefill="green", tags="piece")
        self.d4_piece = tk.Canvas.create_text(self.board, 218, 283, text=None,
                                              font=("Arial", 30), tag=("d4", None, None), activefill="green", tags="piece")
        self.e4_piece = tk.Canvas.create_text(self.board, 282, 283, text=None,
                                              font=("Arial", 30), tag=("e4", None, None), activefill="green", tags="piece")
        self.f4_piece = tk.Canvas.create_text(self.board, 343, 283, text=None,
                                              font=("Arial", 30), tag=("f4", None, None), activefill="green", tags="piece")
        self.g4_piece = tk.Canvas.create_text(self.board, 406, 283, text=None,
                                              font=("Arial", 30), tag=("g4", None, None), activefill="green", tags="piece")
        self.h4_piece = tk.Canvas.create_text(self.board, 469, 283, text=None,
                                              font=("Arial", 30), tag=("h4", None, None), activefill="green", tags="piece")

        self.a3_piece = tk.Canvas.create_text(self.board, 32, 346, text=None,
                                              font=("Arial", 30), tag=("a3", None, None), activefill="green", tags="piece")
        self.b3_piece = tk.Canvas.create_text(self.board, 94, 346, text=None,
                                              font=("Arial", 30), tag=("b3", None, None), activefill="green", tags="piece")
        self.c3_piece = tk.Canvas.create_text(self.board, 157, 346, text=None,
                                              font=("Arial", 30), tag=("c3", None, None), activefill="green", tags="piece")
        self.d3_piece = tk.Canvas.create_text(self.board, 218, 346, text=None,
                                              font=("Arial", 30), tag=("d3", None, None), activefill="green", tags="piece")
        self.e3_piece = tk.Canvas.create_text(self.board, 282, 346, text=None,
                                              font=("Arial", 30), tag=("e3", None, None), activefill="green", tags="piece")
        self.f3_piece = tk.Canvas.create_text(self.board, 343, 346, text=None,
                                              font=("Arial", 30), tag=("f3", None, None), activefill="green", tags="piece")
        self.g3_piece = tk.Canvas.create_text(self.board, 406, 346, text=None,
                                              font=("Arial", 30), tag=("g3", None, None), activefill="green", tags="piece")
        self.h3_piece = tk.Canvas.create_text(self.board, 469, 346, text=None,
                                              font=("Arial", 30), tag=("h3", None, None), activefill="green", tags="piece")

        # WHITES
        self.a2_piece = tk.Canvas.create_text(self.board, 30, 469, text=self.unicode_piece_symbols["R"], font=("Arial", 30),
                                              tag=("a2", "whites", "pawn"), activefill="green", tags="piece")
        self.b2_piece = tk.Canvas.create_text(self.board, 92, 469, text=self.unicode_piece_symbols["K"], font=("Arial", 30),
                                              tag=("b2", "whites", "pawn"), activefill="green", tags="piece")
        self.c2_piece = tk.Canvas.create_text(self.board, 157, 469, text=self.unicode_piece_symbols["B"], font=("Arial", 30),
                                              tag=("c2", "whites", "pawn"), activefill="green", tags="piece")
        self.d2_piece = tk.Canvas.create_text(self.board, 218, 469, text=self.unicode_piece_symbols["Q"], font=("Arial", 30),
                                              tag=("d2", "whites", "pawn"), activefill="green", tags="piece")
        self.e2_piece = tk.Canvas.create_text(self.board, 280, 469, text=self.unicode_piece_symbols["KI"],font=("Arial", 30),
                                              tag=("e2", "whites", "pawn"), activefill="green", tags="piece")
        self.f2_piece = tk.Canvas.create_text(self.board, 343, 469, text=self.unicode_piece_symbols["B"], font=("Arial", 30),
                                              tag=("f2", "whites", "pawn"), activefill="green", tags="piece")
        self.g2_piece = tk.Canvas.create_text(self.board, 403, 469, text=self.unicode_piece_symbols["K"], font=("Arial", 30),
                                              tag=("g2", "whites", "pawn"), activefill="green", tags="piece")
        self.h2_piece = tk.Canvas.create_text(self.board, 469, 469, text=self.unicode_piece_symbols["R"], font=("Arial", 30),
                                              tag=("h2", "whites", "pawn"), activefill="green", tags="piece")

        self.a1_piece = tk.Canvas.create_text(self.board, 32, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30),
                                              tag=("a1", "whites", "rook"), activefill="green", tags="piece")
        self.b1_piece = tk.Canvas.create_text(self.board, 94, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30),
                                              tag=("b1", "whites", "knight"), activefill="green", tags="piece")
        self.c1_piece = tk.Canvas.create_text(self.board, 157, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30),
                                              tag=("c1", "whites", "bishop"), activefill="green", tags="piece")
        self.d1_piece = tk.Canvas.create_text(self.board, 218, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30),
                                              tag=("d1", "whites", "queen"), activefill="green", tags="piece")
        self.e1_piece = tk.Canvas.create_text(self.board, 282, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30),
                                              tag=("e1", "whites", "king"), activefill="green", tags="piece")
        self.f1_piece = tk.Canvas.create_text(self.board, 343, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30),
                                              tag=("f1", "whites", "bishop"), activefill="green", tags="piece")
        self.g1_piece = tk.Canvas.create_text(self.board, 406, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30),
                                              tag=("g1", "whites", "knight"), activefill="green", tags="piece")
        self.h1_piece = tk.Canvas.create_text(self.board, 469, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30),
                                              tag=("h1", "whites", "rook"), activefill="green", tags="piece")
