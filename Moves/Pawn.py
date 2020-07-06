from Chess.Utils import Utils


class Pawn:
    def __init__(self, piece_moving):
        self.piece_moving = piece_moving
        self.utils = Utils()

    def move_is_possible(self, start_tag, end_tag, all_turns_pieces_position, max_turn):
        return end_tag in self.get_all_allowed_moves(start_tag, all_turns_pieces_position, max_turn)

    def get_all_allowed_moves(self, start_tag, all_turns_pieces_position, max_turn, piece=None):
        current_coordinate_number = int(self.utils.get_current_number(start_tag))
        current_coordinate_letter = self.utils.get_current_letter(start_tag)
        print(f"max_turn: {max_turn}")
        print(f"all_turns_pieces_position: {all_turns_pieces_position}")
        current_pieces_position = all_turns_pieces_position[max_turn]
        all_moves = []
        if self.utils.is_white_moving(self.piece_moving):
            if current_coordinate_number == 2:
                if current_coordinate_number + 2 in range(1, 9):
                    possible_move_coordinate = f"{current_coordinate_letter}{current_coordinate_number + 2}"
                    in_between_coordinate = f"{current_coordinate_letter}{current_coordinate_number + 1}"
                    if (self.utils.end_position_is_free(possible_move_coordinate, current_pieces_position)) and (
                            self.utils.end_position_is_free(in_between_coordinate, current_pieces_position)):
                        all_moves.append(possible_move_coordinate)
            if current_coordinate_number + 1 in range(1, 9):
                possible_move_coordinate = f"{current_coordinate_letter}{current_coordinate_number + 1}"
                if self.utils.end_position_is_free(possible_move_coordinate, current_pieces_position):
                    all_moves.append(possible_move_coordinate)
        else:
            if current_coordinate_number == 7:
                if current_coordinate_number - 2 in range(1, 9):
                    in_between_coordinate = f"{current_coordinate_letter}{current_coordinate_number - 1}"
                    possible_move_coordinate = f"{current_coordinate_letter}{current_coordinate_number - 2}"
                    if (self.utils.end_position_is_free(possible_move_coordinate, current_pieces_position)) and (
                            self.utils.end_position_is_free(in_between_coordinate, current_pieces_position)):
                        all_moves.append(possible_move_coordinate)
            if current_coordinate_number - 1 in range(1, 9):
                possible_move_coordinate = f"{current_coordinate_letter}{current_coordinate_number - 1}"
                if self.utils.end_position_is_free(possible_move_coordinate, current_pieces_position):
                    all_moves.append(possible_move_coordinate)
        all_moves = all_moves + \
                    self.take_diagonally_up(current_coordinate_number, current_coordinate_letter,
                                            current_pieces_position)
        en_passant_moves = list(self.en_passant(start_tag, all_turns_pieces_position, max_turn).keys())
        if len(en_passant_moves) > 0:
            all_moves += en_passant_moves
        print(f"all pown moves: {all_moves}")
        return all_moves

    def en_passant(self, start_tag, all_turns_pieces_position, max_turn):
        output = {}
        if max_turn == 0:
            return output
        number = int(self.utils.get_current_number(start_tag))
        letter = self.utils.get_current_letter(start_tag)
        current_pieces_position = all_turns_pieces_position[max_turn]
        previous_turn_pieces_position = all_turns_pieces_position[max_turn - 1]
        current_letter_number = self.utils.letter_to_number(letter)
        start_number_required = 4
        en_passant_move_number = number - 1
        if self.utils.is_white_moving(self.piece_moving):
            start_number_required = 5
            en_passant_move_number = number + 1
        previous_turn_number_required = number - 2
        if self.utils.is_white_moving(self.piece_moving):
            previous_turn_number_required = number + 2

        if number == start_number_required and (current_letter_number in range(2, 9)):
            same_line_left = f"{self.utils.number_to_letter(current_letter_number - 1)}{number}"
            piece_to_remove = same_line_left
            en_passant_move = f"{self.utils.number_to_letter(current_letter_number - 1)}{en_passant_move_number}"
            potential_initial_opponent_position = f"{self.utils.number_to_letter(current_letter_number - 1)}" \
                f"{previous_turn_number_required}"
            print(f"piece_to_remove on left: {piece_to_remove}")
            if ((same_line_left in all_turns_pieces_position[max_turn])
                    and (self.utils.end_position_contains_opponent_piece(self.piece_moving, same_line_left,
                                                                         current_pieces_position))
                    and (current_pieces_position[same_line_left].lower() == "p")
                    and (potential_initial_opponent_position in previous_turn_pieces_position.keys())
                    and (previous_turn_pieces_position[potential_initial_opponent_position].lower() == "p")):
                output[en_passant_move] = piece_to_remove
        if number == start_number_required and (current_letter_number in range(1, 8)):
            same_line_right = f"{self.utils.number_to_letter(current_letter_number + 1)}{number}"
            piece_to_remove = same_line_right
            print(f"piece_to_remove on right: {piece_to_remove}")
            en_passant_move = f"{self.utils.number_to_letter(current_letter_number + 1)}{en_passant_move_number}"
            potential_initial_opponent_position = f"{self.utils.number_to_letter(current_letter_number + 1)}" \
                f"{previous_turn_number_required}"
            if ((same_line_right in all_turns_pieces_position[max_turn])
                    and (self.utils.end_position_contains_opponent_piece(self.piece_moving, same_line_right,
                                                                         current_pieces_position))
                    and (current_pieces_position[same_line_right].lower() == "p")
                    and (potential_initial_opponent_position in previous_turn_pieces_position.keys())
                    and (previous_turn_pieces_position[potential_initial_opponent_position].lower() == "p")):
                output[en_passant_move] = piece_to_remove
        return output

    def take_diagonally_up(self, number, letter, pieces_position):
        moves = []
        current_letter_number = self.utils.letter_to_number(letter)
        if self.utils.is_white_moving(self.piece_moving):
            """ Take up left """
            if number + 1 in range(1, 9) and current_letter_number - 1 in range(1, 9):
                possible_coordinate = f"{self.utils.number_to_letter(current_letter_number - 1)}{number + 1}"
                if self.utils.end_position_contains_opponent_piece(self.piece_moving, possible_coordinate,
                                                                   pieces_position):
                    moves.append(possible_coordinate)
            """ Take up right """
            if number + 1 in range(1, 9) and current_letter_number + 1 in range(1, 9):
                possible_coordinate = f"{self.utils.number_to_letter(current_letter_number + 1)}{number + 1}"
                if self.utils.end_position_contains_opponent_piece(self.piece_moving, possible_coordinate,
                                                                   pieces_position):
                    moves.append(possible_coordinate)
        else:
            """ Take down left """
            if number - 1 in range(1, 9) and current_letter_number - 1 in range(1, 9):
                possible_coordinate = f"{self.utils.number_to_letter(current_letter_number - 1)}{number - 1}"
                if self.utils.end_position_contains_opponent_piece(self.piece_moving, possible_coordinate,
                                                                   pieces_position):
                    moves.append(possible_coordinate)
            """ Take down right """
            if number - 1 in range(1, 9) and current_letter_number + 1 in range(1, 9):
                possible_coordinate = f"{self.utils.number_to_letter(current_letter_number + 1)}{number - 1}"
                if self.utils.end_position_contains_opponent_piece(self.piece_moving, possible_coordinate,
                                                                   pieces_position):
                    moves.append(possible_coordinate)
        return moves
