#from prova import*


class Game:
    def __init__(self):
        # variables used later
        self.count = 1
        self.player = ""
        self.turn = ""
        # build chessboard
        self.build_chessboard_dictionary()
        #
        print(self.chessboard["a1"]["present piece"])

    def move(self, piece, starting_coordinates, end_coordinates):
        # delete piece and owner from old position

        # put piece and owner in new position

    def check_mate(self):
        if self.turn == 10:
            return True

    def turn(self):
        while not self.check_mate():
            if self.count % 2 == 0:
                self.player = 1
            else:
                self.player = 0

    def build_chessboard_dictionary(self):
        # 0 = whites, 1 = blacks
        # r = rook, k = knight, b = bishop, q = queen, ki = king, p = pawn
        self.chessboard = {"a1": {"present piece": "r", "owner present": "0", "previous piece": "", "owner previous": ""},
                           "a2": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "a3": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "a4": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "a5": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "a6": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "a7": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "a8": {"present piece": "r", "owner present": "", "previous piece": "", "owner previous": ""},
                           "b1": {"present piece": "k", "owner present": "", "previous piece": "", "owner previous": ""},
                           "b2": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "b3": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "b4": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "b5": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "b6": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "b7": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "b8": {"present piece": "k", "owner present": "", "previous piece": "", "owner previous": ""},
                           "c1": {"present piece": "b", "owner present": "", "previous piece": "", "owner previous": ""},
                           "c2": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "c3": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "c4": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "c5": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "c6": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "c7": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "c8": {"present piece": "b", "owner present": "", "previous piece": "", "owner previous": ""},
                           "d1": {"present piece": "q", "owner present": "", "previous piece": "", "owner previous": ""},
                           "d2": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "d3": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "d4": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "d5": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "d6": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "d7": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "d8": {"present piece": "q", "owner present": "", "previous piece": "", "owner previous": ""},
                           "e1": {"present piece": "ki", "owner present": "", "previous piece": "", "owner previous": ""},
                           "e2": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "e3": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "e4": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "e5": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "e6": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "e7": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "e8": {"present piece": "ki", "owner present": "", "previous piece": "", "owner previous": ""},
                           "f1": {"present piece": "b", "owner present": "", "previous piece": "", "owner previous": ""},
                           "f2": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "f3": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "f4": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "f5": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "f6": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "f7": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "f8": {"present piece": "b", "owner present": "", "previous piece": "", "owner previous": ""},
                           "g1": {"present piece": "k", "owner present": "", "previous piece": "", "owner previous": ""},
                           "g2": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "g3": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "g4": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "g5": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "g6": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "g7": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "g8": {"present piece": "k", "owner present": "", "previous piece": "", "owner previous": ""},
                           "h1": {"present piece": "r", "owner present": "", "previous piece": "", "owner previous": ""},
                           "h2": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "h3": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "h4": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "h5": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "h6": {"present piece": "", "owner present": "", "previous piece": "", "owner previous": ""},
                           "h7": {"present piece": "p", "owner present": "", "previous piece": "", "owner previous": ""},
                           "h8": {"present piece": "r", "owner present": "", "previous piece": "", "owner previous": ""}}


game = Game()
