from Chess.Utils import Utils


class King:
    def __init__(self, piece_moving):
        self.utils = Utils()
        self.piece_moving = piece_moving

    def move_is_possible(self, start_tag, end_tag, all_turns_pieces_position, max_turn):
        return end_tag in self.get_all_allowed_moves(start_tag=start_tag, max_turn=max_turn,
                                                     all_turns_pieces_position=all_turns_pieces_position)

    def get_all_allowed_moves(self, start_tag, all_turns_pieces_position, max_turn, piece=None):
        current_coordinate_number = int(self.utils.get_current_number(start_tag))
        print(f"current_coordinate_number: {current_coordinate_number}")
        current_coordinate_letter = self.utils.get_current_letter(start_tag)
        print(f"current_coordinate_letter: {current_coordinate_letter}")
        all_moves = self.horizontal_moves(current_coordinate_number, current_coordinate_letter,
                                          all_turns_pieces_position[max_turn]) + \
                    self.vertical_moves(current_coordinate_number, current_coordinate_letter,
                                        all_turns_pieces_position[max_turn]) + \
                    self.diagonal_moves(current_coordinate_number, current_coordinate_letter,
                                        all_turns_pieces_position[max_turn])
        print(all_moves)
        return all_moves

    def horizontal_moves(self, number, letter, pieces_position):
        moves = []
        current_letter_number = self.utils.letter_to_number(letter)
        if current_letter_number + 1 in range(1, 9):
            move = f"{self.utils.number_to_letter(current_letter_number + 1)}{number}"
            if (self.utils.end_position_is_free(move, pieces_position)) or (
                    self.utils.end_position_contains_opponent_piece(self.piece_moving, move,
                                                                    pieces_position)):
                moves.append(move)
        if current_letter_number - 1 in range(1, 9):

            move = f"{self.utils.number_to_letter(current_letter_number - 1)}{number}"
            if (self.utils.end_position_is_free(move, pieces_position)) or (
                    self.utils.end_position_contains_opponent_piece(self.piece_moving, move,
                                                                    pieces_position)):
                moves.append(move)
        return moves

    def vertical_moves(self, number, letter, pieces_position):
        moves = []
        if number + 1 in range(1, 9):
            move = f"{letter}{number + 1}"
            if (self.utils.end_position_is_free(move, pieces_position)) or (
                    self.utils.end_position_contains_opponent_piece(self.piece_moving, move,
                                                                    pieces_position)):
                moves.append(move)
        if number - 1 in range(1, 9):
            move = f"{letter}{number - 1}"
            if (self.utils.end_position_is_free(move, pieces_position)) or (
                    self.utils.end_position_contains_opponent_piece(self.piece_moving, move,
                                                                    pieces_position)):
                moves.append(move)
        return moves

    def diagonal_moves(self, number, letter, pieces_position):
        moves = []
        current_letter_number = self.utils.letter_to_number(letter)
        """ Up - rightwards: letter + 1, number + 1 """
        if current_letter_number + 1 in range(1, 9) and number + 1 in range(1, 9):
            move = f"{self.utils.number_to_letter(current_letter_number + 1)}{number + 1}"
            if (self.utils.end_position_is_free(move, pieces_position)) or (
                    self.utils.end_position_contains_opponent_piece(self.piece_moving, move,
                                                                    pieces_position)):
                moves.append(move)
        """ down - leftwards: letter - 1, number - 1 """
        if current_letter_number - 1 in range(1, 9) and number - 1 in range(1, 9):
            move = f"{self.utils.number_to_letter(current_letter_number - 1)}{number - 1}"
            if (self.utils.end_position_is_free(move, pieces_position)) or (
                    self.utils.end_position_contains_opponent_piece(self.piece_moving, move,
                                                                    pieces_position)):
                moves.append(move)
        """ up - leftwards: letter - 1, number + 1 """
        if current_letter_number - 1 in range(1, 9) and number + 1 in range(1, 9):
            move = f"{self.utils.number_to_letter(current_letter_number - 1)}{number + 1}"
            if (self.utils.end_position_is_free(move, pieces_position)) or (
                    self.utils.end_position_contains_opponent_piece(self.piece_moving, move,
                                                                    pieces_position)):
                moves.append(move)
        """ down - rightwards: letter + 1, number - 1 """
        if current_letter_number + 1 in range(1, 9) and number - 1 in range(1, 9):
            move = f"{self.utils.number_to_letter(current_letter_number + 1)}{number - 1}"
            if (self.utils.end_position_is_free(move, pieces_position)) or (
                    self.utils.end_position_contains_opponent_piece(self.piece_moving, move,
                                                                    pieces_position)):
                moves.append(move)
        return moves
