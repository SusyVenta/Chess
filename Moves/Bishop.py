from Chess.Utils import Utils


class Bishop:
    def __init__(self):
        self.utils = Utils()

    def move_is_possible(self, start_tag, end_tag):
        return end_tag in self.get_all_allowed_moves(start_tag)

    def get_all_allowed_moves(self, start_tag):
        current_coordinate_number = int(self.utils.get_current_number(start_tag))
        current_coordinate_letter = self.utils.get_current_letter(start_tag)

        all_moves = self.move_up_rightwards(current_coordinate_number, current_coordinate_letter) \
            + self.move_up_leftwards(current_coordinate_number, current_coordinate_letter) \
            + self.move_down_leftwards(current_coordinate_number, current_coordinate_letter) \
            + self.move_down_rightwards(current_coordinate_number, current_coordinate_letter)
        print(all_moves)
        return all_moves

    def move_up_rightwards(self, current_coordinate_number, current_coordinate_letter):
        """ Moving diagonally up, toward right upper corner:
        - Number increases by 1, if within range 1, 8.
        - Letter 'increases' by 1, if within range 1, 8  """
        possible_moves = []
        current_number = current_coordinate_number
        current_letter_number = self.utils.letter_to_number(current_coordinate_letter)
        while current_number + 1 in range(1, 9) and current_letter_number + 1 in range(1, 9):
            possible_moves.append(f"{self.utils.number_to_letter(current_letter_number + 1)}{current_number + 1}")
            current_number += 1
            current_letter_number += 1
        return possible_moves

    def move_up_leftwards(self, current_coordinate_number, current_coordinate_letter):
        """ Moving diagonally up, toward left upper corner:
            - Number increases by 1, if within range 1, 8.
            - Letter 'decreases' by 1, if within range 1, 8  """
        possible_moves = []
        current_number = current_coordinate_number
        current_letter_number = self.utils.letter_to_number(current_coordinate_letter)
        while current_number + 1 in range(1, 9) and current_letter_number - 1 in range(1, 9):
            possible_moves.append(f"{self.utils.number_to_letter(current_letter_number - 1)}{current_number + 1}")
            current_number += 1
            current_letter_number -= 1
        return possible_moves

    def move_down_leftwards(self, current_coordinate_number, current_coordinate_letter):
        """ Moving diagonally up, toward left upper corner:
            - Number decreases by 1, if within range 1, 8.
            - Letter 'decreases' by 1, if within range 1, 8  """
        possible_moves = []
        current_number = current_coordinate_number
        current_letter_number = self.utils.letter_to_number(current_coordinate_letter)
        while current_number - 1 in range(1, 9) and current_letter_number - 1 in range(1, 9):
            possible_moves.append(f"{self.utils.number_to_letter(current_letter_number - 1)}{current_number - 1}")
            current_number -= 1
            current_letter_number -= 1
        return possible_moves

    def move_down_rightwards(self, current_coordinate_number, current_coordinate_letter):
        """ Moving diagonally up, toward left upper corner:
            - Number decreases by 1, if within range 1, 8.
            - Letter 'increases' by 1, if within range 1, 8  """
        possible_moves = []
        current_number = current_coordinate_number
        current_letter_number = self.utils.letter_to_number(current_coordinate_letter)
        while current_number - 1 in range(1, 9) and current_letter_number + 1 in range(1, 9):
            possible_moves.append(f"{self.utils.number_to_letter(current_letter_number + 1)}{current_number - 1}")
            current_number -= 1
            current_letter_number += 1
        return possible_moves
