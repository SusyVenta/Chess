from Chess.Utils import Utils


class Rook:
    def __init__(self, piece_moving):
        self.utils = Utils()
        self.piece_moving = piece_moving

    def move_is_possible(self, start_tag, end_tag, all_turns_pieces_position, max_turn):
        return end_tag in self.get_all_allowed_moves(
            start_tag=start_tag, all_turns_pieces_position=all_turns_pieces_position, max_turn=max_turn)

    def get_all_allowed_moves(self, start_tag, all_turns_pieces_position, max_turn, piece=None):
        """
        Rook can only move vertically or horizontally.
        Returns combination of all theoretically possible vertical or horizontal moves.
        """
        current_coordinate_number = int(self.utils.get_current_number(start_tag))
        current_coordinate_letter = self.utils.get_current_letter(start_tag)
        vertical_moves = self.get_vertical_moves_possible(current_coordinate_letter, current_coordinate_number,
                                                          all_turns_pieces_position[max_turn])
        horizontal_moves = self.get_horizontal_moves_possible(current_coordinate_letter, current_coordinate_number,
                                                              all_turns_pieces_position[max_turn])
        all_moves = vertical_moves + horizontal_moves
        print(f"all rook moves: {all_moves}")
        return all_moves

    def get_horizontal_moves_possible(self, current_coordinate_letter, current_coordinate_number, pieces_position):
        """ Horizontal move: letter changes, number remains the same. """
        start_tag_letter_number = int(self.utils.letter_to_number(current_coordinate_letter))
        # print("start_tag_letter_number: {}".format(start_tag_letter_number))
        # print("end_tag_letter_number: {}".format(end_tag_letter_number))
        possible_moves = []
        if 1 <= start_tag_letter_number < 8:
            """ Look at available moves to the right """
            for i in range(start_tag_letter_number + 1, 9, +1):
                # print("i: {}".format(i))
                move = f"{self.utils.number_to_letter(i)}{current_coordinate_number}"
                print(f"move: {move}")
                if self.utils.end_position_is_free(move, pieces_position):
                    print(f"self.utils.end_position_is_free(move, pieces_position): {self.utils.end_position_is_free(move, pieces_position)}")
                    possible_moves.append(move)
                elif self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position):
                    print(f"self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position): {self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position)}")
                    possible_moves.append(move)
                    break
                else:
                    break
        if 1 < start_tag_letter_number <= 8:
            """ Look at available moves to the left """
            for i in range(start_tag_letter_number - 1, 0, -1):
                move = f"{self.utils.number_to_letter(i)}{current_coordinate_number}"
                # print(move)
                if self.utils.end_position_is_free(move, pieces_position):
                    print("self.utils.end_position_is_free(move, pieces_position): {}".format(self.utils.end_position_is_free(move, pieces_position)))
                    possible_moves.append(move)
                elif self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position):
                    print("self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position): {}".format(self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position)))
                    possible_moves.append(move)
                    break
                else:
                    break
        return possible_moves

    def get_vertical_moves_possible(self, current_coordinate_letter, current_coordinate_number, pieces_position):
        """ Vertical move: letter stays the same, number can increase or decrease. """
        possible_moves = []
        if 1 <= current_coordinate_number < 8:
            """ Look at available moves upwards """
            # print("end_tag_letter_number > start_tag_letter_number: {}".format(end_tag_letter_number > start_tag_letter_number))
            for i in range(current_coordinate_number + 1, 9, +1):
                # print("i: {}".format(i))
                move = f"{current_coordinate_letter}{i}"
                print(f"move: {move}")
                if self.utils.end_position_is_free(move, pieces_position):
                    print(f"self.utils.end_position_is_free(move, pieces_position): {self.utils.end_position_is_free(move, pieces_position)}")
                    possible_moves.append(move)
                elif self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position):
                    print(f"self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position): {self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position)}")
                    possible_moves.append(move)
                    break
                else:
                    break
        if 1 < current_coordinate_number <= 8:
            """ Look at available moves downwards """
            # print("end_tag_letter_number < start_tag_letter_number")
            for i in range(current_coordinate_number - 1, 0, -1):
                move = "{}{}".format(current_coordinate_letter, i)
                # print(move)
                if self.utils.end_position_is_free(move, pieces_position):
                    print("self.utils.end_position_is_free(move, pieces_position): {}".format(self.utils.end_position_is_free(move, pieces_position)))
                    possible_moves.append(move)
                elif self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position):
                    print("self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position): {}".format(self.utils.end_position_contains_opponent_piece(self.piece_moving, move, pieces_position)))
                    possible_moves.append(move)
                    break
                else:
                    break
        return possible_moves


