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

    def temporary_update_pieces_position_next_turn(self, piece_moved, start_coordinates, end_coordinates,
                                                   extra_piece_to_remove_coordinates=None):
        need_to_remove_taken_piece = False
        self.pieces_configurations_of_all_turns[self.moves_done + 1] = self.pieces_configurations_of_all_turns[self.moves_done].copy()
        print("############## before removing")
        print(self.pieces_configurations_of_all_turns[self.moves_done + 1])
        del self.pieces_configurations_of_all_turns[self.moves_done + 1][start_coordinates]

        if end_coordinates in self.pieces_configurations_of_all_turns[self.moves_done + 1].keys():
            need_to_remove_taken_piece = True
        self.pieces_configurations_of_all_turns[self.moves_done + 1][end_coordinates] = piece_moved
        if extra_piece_to_remove_coordinates:
            if extra_piece_to_remove_coordinates in self.pieces_configurations_of_all_turns[self.moves_done + 1].keys():
                del self.pieces_configurations_of_all_turns[self.moves_done + 1][extra_piece_to_remove_coordinates]
            need_to_remove_taken_piece = True
        print("after removing:")
        print(self.pieces_configurations_of_all_turns[self.moves_done + 1])
        return need_to_remove_taken_piece

    def need_to_update_pieces_position(self, piece_moved, start_coordinates, end_coordinates):
        need_to_remove_taken_piece = False
        next_turn_configuration = self.pieces_configurations_of_all_turns[self.moves_done].copy()
        del next_turn_configuration[start_coordinates]
        if end_coordinates in next_turn_configuration.keys():
            need_to_remove_taken_piece = True
        next_turn_configuration[end_coordinates] = piece_moved
        self.pieces_configurations_of_all_turns[self.moves_done + 1] = next_turn_configuration
        return need_to_remove_taken_piece

    def is_end_position_free_or_with_opponent_piece(self, piece_moved, end_coordinates):
        if end_coordinates in self.pieces_configurations_of_all_turns[self.moves_done].keys():
            if (piece_moved.islower() and self.pieces_configurations_of_all_turns[self.moves_done][end_coordinates].isupper()) or (
                    piece_moved.isupper() and self.pieces_configurations_of_all_turns[self.moves_done][end_coordinates].islower()):
                return True
            else:
                return False
        else:
            return True

