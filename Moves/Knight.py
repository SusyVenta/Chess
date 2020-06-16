from Chess.Utils import Utils


class Knight:
    def __init__(self):
        self.utils = Utils()

    def move_is_possible(self, start_tag, end_tag):
        return end_tag in self.get_all_allowed_moves(start_tag)

    def get_all_allowed_moves(self, start_tag):
        current_coordinate_number = int(self.utils.get_current_number(start_tag))
        print(f"current_coordinate_number: {current_coordinate_number}")
        current_coordinate_letter = self.utils.get_current_letter(start_tag)
        print(f"current_coordinate_letter: {current_coordinate_letter}")
        current_letter_number = self.utils.letter_to_number(current_coordinate_letter)
        all_moves = []

        """ Combinations by 2 up """
        if current_coordinate_number + 2 in range(1, 9):
            """ Try 2 down, 1 right """
            if current_letter_number + 1 in range(1, 9):
                all_moves.append(
                    f"{self.utils.number_to_letter(current_letter_number + 1)}{current_coordinate_number + 2}")
            """ Try 2 down, 1 left """
            if current_letter_number - 1 in range(1, 9):
                all_moves.append(
                    f"{self.utils.number_to_letter(current_letter_number - 1)}{current_coordinate_number + 2}")
        """ Combinations by 2 down """
        if current_coordinate_number - 2 in range(1, 9):
            """ Try 2 down, 1 right """
            if current_letter_number + 1 in range(1, 9):
                all_moves.append(
                    f"{self.utils.number_to_letter(current_letter_number + 1)}{current_coordinate_number - 2}")
            """ Try 2 down, 1 left """
            if current_letter_number - 1 in range(1, 9):
                all_moves.append(
                    f"{self.utils.number_to_letter(current_letter_number - 1)}{current_coordinate_number - 2}")
        """ Combinations by 2 right"""
        if current_letter_number + 2 in range(1, 9):
            """ Try 2 right, 1 up """
            if current_coordinate_number + 1 in range(1, 9):
                all_moves.append(
                    f"{self.utils.number_to_letter(current_letter_number + 2)}{current_coordinate_number + 1}")
            """ Try 2 right, 1 down """
            if current_coordinate_number - 1 in range(1, 9):
                all_moves.append(
                    f"{self.utils.number_to_letter(current_letter_number + 2)}{current_coordinate_number - 1}")
        """ Combinations by 2 left"""
        if current_letter_number - 2 in range(1, 9):
            """ Try 2 left, 1 up """
            if current_coordinate_number + 1 in range(1, 9):
                all_moves.append(
                    f"{self.utils.number_to_letter(current_letter_number - 2)}{current_coordinate_number + 1}")
            """ Try 2 left, 1 down """
            if current_coordinate_number - 1 in range(1, 9):
                all_moves.append(
                    f"{self.utils.number_to_letter(current_letter_number - 2)}{current_coordinate_number - 1}")

        print(all_moves)
        return all_moves
