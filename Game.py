class Game:
    def __init__(self):
        self.moves_done = 0
        self.player_moving = "white"
        self.pieces_position = {"a8": "r", "b8": "k", "c8": "b", "d8": "q", "e8": "ki", "f8": "b", "g8": "k", "h8": "r",
                                "a7": "p", "b7": "p", "c7": "p", "d7": "p", "e7": "p", "f7": "p", "g7": "p", "h7": "p",
                                "a2": "P", "b2": "P", "c2": "P", "d2": "P", "e2": "P", "f2": "P", "g2": "P", "h2": "P",
                                "a1": "R", "b1": "K", "c1": "B", "d1": "Q", "e1": "KI", "f1": "B", "g1": "K", "h1": "R"}
        self.pieces_configurations_of_all_turns = {0: self.pieces_position}

    def update_current_player(self):
        if self.player_moving == "white":
            self.player_moving = "black"
        else:
            self.player_moving = "white"
        self.moves_done += 1
        return self.player_moving

    def update_pieces_position(self, piece_moved, start_coordinates, end_coordinates):
        print("previous pieces config:")
        print(self.pieces_position[start_coordinates])
        del self.pieces_position[start_coordinates]
        # block taking your own pieces to be done in framework
        self.pieces_position[end_coordinates] = piece_moved
        self.pieces_configurations_of_all_turns[self.moves_done] = self.pieces_position

        print("new config:")
        try:
            print(self.pieces_position[start_coordinates])
        except KeyError:
            print("no piece found in old position")
        print(self.pieces_position[end_coordinates])
        print(self.pieces_configurations_of_all_turns)