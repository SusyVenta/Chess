class Game:
    def __init__(self):
        self.moves_done = 0
        self.player_moving = "white"
        self.pieces_position = {"a8": "r", "b8": "k", "c8": "b", "d8": "q", "e8": "ki", "f8": "b", "g8": "k", "h8": "r",
                                "a7": "p", "b7": "p", "c7": "p", "d7": "p", "e7": "p", "f7": "p", "g7": "p", "h7": "p",
                                "a2": "P", "b2": "P", "c2": "P", "d2": "P", "e2": "P", "f2": "P", "g2": "P", "h2": "P",
                                "a1": "R", "b1": "K", "c1": "B", "d1": "Q", "e1": "KI", "f1": "B", "g1": "K", "h1": "R"}
        self.pieces_configurations_of_all_turns = {0: self.pieces_position}

        # self.make_current_player_move()

    def update_current_player(self):
        self.player_moving = "black" if self.player_moving == "white" else "white"
        print(self.player_moving)

    # def make_current_player_move(self):


    # def move(self, piece, starting_coordinates, end_coordinates):
    #     # delete piece and owner from old position
    #
    #     # put piece and owner in new position
    #
    # def check_mate(self):
    #     if self.turn == 10:
    #         return True
    #
    # def turn(self):
    #     while not self.check_mate():
    #         if self.moves_done % 2 == 0:
    #             self.player_moving = 1
    #         else:
    #             self.player_moving = 0


game = Game()
