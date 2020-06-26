from Chess.Utils import Utils


class Rook:
    def __init__(self, piece_moving):
        self.utils = Utils()
        self.piece_moving = piece_moving

    def move_is_possible(self, start_tag, end_tag):
        return end_tag in self.get_all_allowed_moves(start_tag)

    def get_all_allowed_moves(self, start_tag):
        """
        Rook can only move vertically or horizontally.
        Returns combination of all theoretically possible vertical or horizontal moves.
        """
        current_coordinate_number = int(self.utils.get_current_number(start_tag))
        print(f"current_coordinate_number: {current_coordinate_number}")
        current_coordinate_letter = self.utils.get_current_letter(start_tag)
        print(f"current_coordinate_letter: {current_coordinate_letter}")
        vertical_moves = self.get_vertical_moves_possible(current_coordinate_letter, current_coordinate_number)
        horizontal_moves = self.get_horizontal_moves_possible(current_coordinate_letter, current_coordinate_number)
        all_moves = vertical_moves + horizontal_moves
        print(all_moves)
        return all_moves

    def get_horizontal_moves_possible(self, current_coordinate_letter, current_coordinate_number):
        """ Horizontal move: letter changes, number remains the same. """
        all_letters_list = self.utils.all_letters_except_current_list(current_coordinate_letter)
        same_number_list = [str(current_coordinate_number) for i in range(7)]
        horizontal_moves = [str(a) + b for a, b in zip(all_letters_list, same_number_list)]
        return horizontal_moves

    def get_vertical_moves_possible(self, current_coordinate_letter, current_coordinate_number):
        """ Vertical move: letter stays the same, number can increase or decrease. """
        all_numbers_list = self.utils.all_numbers_except_current_list(current_coordinate_number)
        all_numbers_list_str = [str(x) for x in all_numbers_list]
        # print(all_numbers_list_str)
        same_letter_list = [current_coordinate_letter for i in range(7)]
        # print(same_letter_list)
        vertical_moves = [str(a) + b for a, b in zip(same_letter_list, all_numbers_list_str)]
        # print(vertical_moves)
        return vertical_moves


