import tkinter as tk
from win32api import GetSystemMetrics


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

    def start(self):
        self.controller.show_frame(FrameChessboard)
        # show board and menu
        #
        self.menu()
        self.board_squares()
        self.show_default_pieces()

    def menu(self):
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.controller.config(menu=self.menubar)
        self.filemenu.add_command(label="Quit", command=self.controller.destroy)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)

    def highlight_moves_by_clicking_on_square(self, event):
        item2 = self.board.find_closest(event.x, event.y)
        current_piece = self.board.gettags(item2)[2]
        item = self.a7

        if current_piece == "rook" and 'a7' in self.board.gettags(item)[0]:
            current_color = self.board.itemcget(item, 'fill')
            if current_color == 'grey' or current_color == "white":
                self.board.itemconfig(item, fill='green')
            else:
                self.board.itemconfig(item, fill=self.board.gettags(item)[1])

    def identify_closest_square(self, event):
        item = self.board.find_closest(event.x, event.y)[0]
        tags = self.board.gettags(item)
        print (tags)
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        canvas.find_closest(x, y)
        print (canvas.find_closest(x, y))

    def board_squares(self):
        self.board = tk.Canvas(self, width=500, height=500)
        self.board.pack()
        self.board.bind('<Button-2>', self.identify_closest_square)
        self.board.bind('<Button-1>', self.highlight_moves_by_clicking_on_square)

        # DRAW CHESSBOARD
        # (starting space from left, start space from top, till where (width), till where (height)
        self.a8 = tk.Canvas.create_rectangle(self.board, 0, 0, 62.5, 62.5, fill="white", activefill="green",
                                             tag=("a8", "white"))
        self.b8 = tk.Canvas.create_rectangle(self.board, 62.5, 0, 125, 62.5, fill="grey", activefill="green",
                                             tag=("b8", "grey"))
        self.c8 = tk.Canvas.create_rectangle(self.board, 125, 0, 187.5, 62.5, fill="white", activefill="green",
                                             tag=("c8", "white"))
        self.d8 = tk.Canvas.create_rectangle(self.board, 187.5, 0, 250, 62.5, fill="grey", activefill="green",
                                             tag=("d8", "grey"))
        self.e8 = tk.Canvas.create_rectangle(self.board, 250, 1, 312.5, 62.5, fill="white", activefill="green",
                                             tag=("e8", "white"))
        self.f8 = tk.Canvas.create_rectangle(self.board, 312.5, 0, 375, 62.5, fill="grey", activefill="green",
                                             tag=("f8", "grey"))
        self.g8 = tk.Canvas.create_rectangle(self.board, 375, 0, 437, 62.5, fill="white", activefill="green",
                                             tag=("g8", "white"))
        self.h8 = tk.Canvas.create_rectangle(self.board, 437, 0, 500, 62.5, fill="grey", activefill="green",
                                             tag=("h8", "grey", "rook"))

        self.a7 = tk.Canvas.create_rectangle(self.board, 0, 62.5, 62.5, 125, fill="grey", activefill="green",
                                             tag=("a7", "grey"))
        self.b7 = tk.Canvas.create_rectangle(self.board, 62.5, 62.5, 125, 125, fill="white", activefill="green",
                                             tag=("b7", "white"))
        self.c7 = tk.Canvas.create_rectangle(self.board, 125, 62.5, 187.5, 125, fill="grey", activefill="green",
                                             tag=("c7", "grey"))
        self.d7 = tk.Canvas.create_rectangle(self.board, 187.5, 62.5, 250, 125, fill="white", activefill="green",
                                             tag=("d7", "white"))
        self.e7 = tk.Canvas.create_rectangle(self.board, 250, 62.5, 312.5, 125, fill="grey", activefill="green",
                                             tag=("e7", "grey"))
        self.f7 = tk.Canvas.create_rectangle(self.board, 312.5, 62.5, 375, 125, fill="white", activefill="green",
                                             tag=("f7", "white"))
        self.g7 = tk.Canvas.create_rectangle(self.board, 375, 62.5, 437, 125, fill="grey", activefill="green",
                                             tag=("g7", "grey"))
        self.h7 = tk.Canvas.create_rectangle(self.board, 437, 62.5, 500, 125, fill="white", activefill="green",
                                             tag=("h7", "white"))

        self.a6 = tk.Canvas.create_rectangle(self.board, 0, 125, 62.5, 187.5, fill="white", activefill="green",
                                             tag=("a6", "white"))
        self.b6 = tk.Canvas.create_rectangle(self.board, 62.5, 125, 125, 187.5, fill="grey", activefill="green",
                                             tag=("b6", "grey"))
        self.c6 = tk.Canvas.create_rectangle(self.board, 125, 125, 187.5, 187.5, fill="white", activefill="green",
                                             tag=("c6", "white"))
        self.d6 = tk.Canvas.create_rectangle(self.board, 187.5, 125, 250, 187.5, fill="grey", activefill="green",
                                             tag=("d6", "grey"))
        self.e6 = tk.Canvas.create_rectangle(self.board, 250, 125, 312.5, 187.5, fill="white", activefill="green",
                                             tag=("e6", "white"))
        self.f6 = tk.Canvas.create_rectangle(self.board, 312.5, 125, 375, 187.5, fill="grey", activefill="green",
                                             tag=("f6", "grey"))
        self.g6 = tk.Canvas.create_rectangle(self.board, 375, 125, 437, 187.5, fill="white", activefill="green",
                                             tag=("g6", "white"))
        self.h6 = tk.Canvas.create_rectangle(self.board, 437, 125, 500, 187.5, fill="grey", activefill="green",
                                             tag=("h6", "grey"))

        self.a5 = tk.Canvas.create_rectangle(self.board, 0, 187.5, 62.5, 250, fill="grey", activefill="green",
                                             tag=("a5", "grey"))
        self.b5 = tk.Canvas.create_rectangle(self.board, 62.5, 187.5, 125, 250, fill="white", activefill="green",
                                             tag=("b5", "white"))
        self.c5 = tk.Canvas.create_rectangle(self.board, 125, 187.5, 187.5, 250, fill="grey", activefill="green",
                                             tag=("c5", "grey"))
        self.d5 = tk.Canvas.create_rectangle(self.board, 187.5, 187.5, 250, 250, fill="white", activefill="green",
                                             tag=("d5", "white"))
        self.e5 = tk.Canvas.create_rectangle(self.board, 250, 187.5, 312.5, 250, fill="grey", activefill="green",
                                             tag=("e5", "grey"))
        self.f5 = tk.Canvas.create_rectangle(self.board, 312.5, 187.5, 375, 250, fill="white", activefill="green",
                                             tag=("f5", "white"))
        self.g5 = tk.Canvas.create_rectangle(self.board, 375, 187.5, 437, 250, fill="grey", activefill="green",
                                             tag=("g5", "grey"))
        self.h5 = tk.Canvas.create_rectangle(self.board, 437, 187.5, 500, 250, fill="white", activefill="green",
                                             tag=("h5", "white"))

        self.a4 = tk.Canvas.create_rectangle(self.board, 0, 250, 62.5, 312.5, fill="white", activefill="green",
                                             tag=("a4", "white"))
        self.b4 = tk.Canvas.create_rectangle(self.board, 62.5, 250, 125, 312.5, fill="grey", activefill="green",
                                             tag=("b4", "grey"))
        self.c4 = tk.Canvas.create_rectangle(self.board, 125, 250, 187.5, 312.5, fill="white", activefill="green",
                                             tag=("c4", "white"))
        self.d4 = tk.Canvas.create_rectangle(self.board, 187.5, 250, 250, 312.5, fill="grey", activefill="green",
                                             tag=("d4", "grey"))
        self.e4 = tk.Canvas.create_rectangle(self.board, 250, 250, 312.5, 312.5, fill="white", activefill="green",
                                             tag=("e4", "white"))
        self.f4 = tk.Canvas.create_rectangle(self.board, 312.5, 250, 375, 312.5, fill="grey", activefill="green",
                                             tag=("f4", "grey"))
        self.g4 = tk.Canvas.create_rectangle(self.board, 375, 250, 437, 312.5, fill="white", activefill="green",
                                             tag=("g4", "white"))
        self.h4 = tk.Canvas.create_rectangle(self.board, 437, 250, 500, 312.5, fill="grey", activefill="green",
                                             tag=("h4", "grey"))

        self.a3 = tk.Canvas.create_rectangle(self.board, 0, 312.5, 62.5, 375, fill="grey", activefill="green",
                                             tag=("a3", "grey"))
        self.b3 = tk.Canvas.create_rectangle(self.board, 62.5, 312.5, 125, 375, fill="white", activefill="green",
                                             tag=("b3", "white"))
        self.c3 = tk.Canvas.create_rectangle(self.board, 125, 312.5, 187.5, 375, fill="grey", activefill="green",
                                             tag=("c3", "grey"))
        self.d3 = tk.Canvas.create_rectangle(self.board, 187.5, 312.5, 250, 375, fill="white", activefill="green",
                                             tag=("d3", "white"))
        self.e3 = tk.Canvas.create_rectangle(self.board, 250, 312.5, 312.5, 375, fill="grey", activefill="green",
                                             tag=("e3", "grey"))
        self.f3 = tk.Canvas.create_rectangle(self.board, 312.5, 312.5, 375, 375, fill="white", activefill="green",
                                             tag=("f3", "white"))
        self.g3 = tk.Canvas.create_rectangle(self.board, 375, 312.5, 437, 375, fill="grey", activefill="green",
                                             tag=("g3", "grey"))
        self.h3 = tk.Canvas.create_rectangle(self.board, 437, 312.5, 500, 375, fill="white", activefill="green",
                                             tag=("h3", "white"))

        self.a2 = tk.Canvas.create_rectangle(self.board, 0, 375, 62.5, 437, fill="white", activefill="green",
                                             tag=("a2", "white"))
        self.b2 = tk.Canvas.create_rectangle(self.board, 62.5, 375, 125, 437, fill="grey", activefill="green",
                                             tag=("b2", "grey"))
        self.c2 = tk.Canvas.create_rectangle(self.board, 125, 375, 187.5, 437, fill="white", activefill="green",
                                             tag=("c2", "white"))
        self.d2 = tk.Canvas.create_rectangle(self.board, 187.5, 375, 250, 437, fill="grey", activefill="green",
                                             tag=("d2", "grey"))
        self.e2 = tk.Canvas.create_rectangle(self.board, 250, 375, 312.5, 437, fill="white", activefill="green",
                                             tag=("e2", "white"))
        self.f2 = tk.Canvas.create_rectangle(self.board, 312.5, 375, 375, 437, fill="grey", activefill="green",
                                             tag=("f2", "grey"))
        self.g2 = tk.Canvas.create_rectangle(self.board, 375, 375, 437, 437, fill="white", activefill="green",
                                             tag=("g2", "white"))
        self.h2 = tk.Canvas.create_rectangle(self.board, 437, 375, 500, 437, fill="grey", activefill="green",
                                             tag=("h2", "grey"))

        self.a1 = tk.Canvas.create_rectangle(self.board, 0, 437, 62.5, 500, fill="grey", activefill="green",
                                             tag=("a1", "grey"))
        self.b1 = tk.Canvas.create_rectangle(self.board, 62.5, 437, 125, 500, fill="white", activefill="green",
                                             tag=("b1", "white"))
        self.c1 = tk.Canvas.create_rectangle(self.board, 125, 437, 187.5, 500, fill="grey", activefill="green",
                                             tag=("c1", "grey"))
        self.d1 = tk.Canvas.create_rectangle(self.board, 187.5, 437, 250, 500, fill="white", activefill="green",
                                             tag=("d1", "white"))
        self.e1 = tk.Canvas.create_rectangle(self.board, 250, 437, 312.5, 500, fill="grey", activefill="green",
                                             tag=("e1", "grey"))
        self.f1 = tk.Canvas.create_rectangle(self.board, 312.5, 437, 375, 500, fill="white", activefill="green",
                                             tag=("f1", "white"))
        self.g1 = tk.Canvas.create_rectangle(self.board, 375, 437, 437, 500, fill="grey", activefill="green",
                                             tag=("g1", "grey"))
        self.h1 = tk.Canvas.create_rectangle(self.board, 437, 437, 500, 500, fill="white", activefill="green",
                                             tag=("h1", "white"))

    def show_default_pieces(self):
        # BLACKS
        self.a8_piece = tk.Canvas.create_text(self.board, 30, 30, text=self.unicode_piece_symbols["r"], font=("Arial", 30))
        self.b8_piece = tk.Canvas.create_text(self.board, 92, 30, text=self.unicode_piece_symbols["k"], font=("Arial", 30))
        self.c8_piece = tk.Canvas.create_text(self.board, 157, 30, text=self.unicode_piece_symbols["b"], font=("Arial", 30))
        self.d8_piece = tk.Canvas.create_text(self.board, 218, 30, text=self.unicode_piece_symbols["q"], font=("Arial", 30))
        self.e8_piece = tk.Canvas.create_text(self.board, 280, 30, text=self.unicode_piece_symbols["ki"], font=("Arial", 30))
        self.f8_piece = tk.Canvas.create_text(self.board, 343, 30, text=self.unicode_piece_symbols["b"], font=("Arial", 30))
        self.g8_piece = tk.Canvas.create_text(self.board, 403, 30, text=self.unicode_piece_symbols["k"], font=("Arial", 30))
        self.h8_piece = tk.Canvas.create_text(self.board, 469, 30, text=self.unicode_piece_symbols["r"], font=("Arial", 30))

        self.a7_piece = tk.Canvas.create_text(self.board, 32, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30))
        self.b7_piece = tk.Canvas.create_text(self.board, 94, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30))
        self.c7_piece = tk.Canvas.create_text(self.board, 157, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30))
        self.d7_piece = tk.Canvas.create_text(self.board, 218, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30))
        self.e7_piece = tk.Canvas.create_text(self.board, 282, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30))
        self.f7_piece = tk.Canvas.create_text(self.board, 343, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30))
        self.g7_piece = tk.Canvas.create_text(self.board, 406, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30))
        self.h7_piece = tk.Canvas.create_text(self.board, 469, 95, text=self.unicode_piece_symbols["p"], font=("Arial", 30))

        # WHITES
        self.a2_piece = tk.Canvas.create_text(self.board, 30, 469, text=self.unicode_piece_symbols["R"], font=("Arial", 30))
        self.b2_piece = tk.Canvas.create_text(self.board, 92, 469, text=self.unicode_piece_symbols["K"], font=("Arial", 30))
        self.c2_piece = tk.Canvas.create_text(self.board, 157, 469, text=self.unicode_piece_symbols["B"], font=("Arial", 30))
        self.d2_piece = tk.Canvas.create_text(self.board, 218, 469, text=self.unicode_piece_symbols["Q"], font=("Arial", 30))
        self.e2_piece = tk.Canvas.create_text(self.board, 280, 469, text=self.unicode_piece_symbols["KI"],font=("Arial", 30))
        self.f2_piece = tk.Canvas.create_text(self.board, 343, 469, text=self.unicode_piece_symbols["B"], font=("Arial", 30))
        self.g2_piece = tk.Canvas.create_text(self.board, 403, 469, text=self.unicode_piece_symbols["K"], font=("Arial", 30))
        self.h2_piece = tk.Canvas.create_text(self.board, 469, 469, text=self.unicode_piece_symbols["R"], font=("Arial", 30))

        self.a1_piece = tk.Canvas.create_text(self.board, 32, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30))
        self.b1_piece = tk.Canvas.create_text(self.board, 94, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30))
        self.c1_piece = tk.Canvas.create_text(self.board, 157, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30))
        self.d1_piece = tk.Canvas.create_text(self.board, 218, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30))
        self.e1_piece = tk.Canvas.create_text(self.board, 282, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30))
        self.f1_piece = tk.Canvas.create_text(self.board, 343, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30))
        self.g1_piece = tk.Canvas.create_text(self.board, 406, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30))
        self.h1_piece = tk.Canvas.create_text(self.board, 469, 406, text=self.unicode_piece_symbols["P"], font=("Arial", 30))
