from Chess.Utils import Utils


class King:
    def __init__(self):
        self.utils = Utils()

    def move_is_possible(self, start_tag, end_tag):
        return end_tag in self.get_all_allowed_moves(start_tag)

    def get_all_allowed_moves(self, start_tag):
        current_coordinate_number = int(self.utils.get_current_number(start_tag))
        print(f"current_coordinate_number: {current_coordinate_number}")
        current_coordinate_letter = self.utils.get_current_letter(start_tag)
        print(f"current_coordinate_letter: {current_coordinate_letter}")
        all_moves = self.horizontal_moves(current_coordinate_number, current_coordinate_letter) + \
            self.vertical_moves(current_coordinate_number, current_coordinate_letter) + \
            self.diagonal_moves(current_coordinate_number, current_coordinate_letter)
        print(all_moves)
        return all_moves

    def horizontal_moves(self, number, letter):
        moves = []
        current_letter_number = self.utils.letter_to_number(letter)
        if current_letter_number + 1 in range(1, 9):
            moves.append(f"{self.utils.number_to_letter(current_letter_number + 1)}{number}")
        if current_letter_number - 1 in range(1, 9):
            moves.append(f"{self.utils.number_to_letter(current_letter_number - 1)}{number}")
        return moves

    def vertical_moves(self, number, letter):
        moves = []
        if number + 1 in range(1, 9):
            moves.append(f"{letter}{number + 1}")
        if number - 1 in range(1, 9):
            moves.append(f"{letter}{number - 1}")
        return moves

    def diagonal_moves(self, number, letter):
        moves = []
        current_letter_number = self.utils.letter_to_number(letter)
        """ Up - rightwards: letter + 1, number + 1 """
        if current_letter_number + 1 in range(1, 9) and number + 1 in range(1, 9):
            moves.append(f"{self.utils.number_to_letter(current_letter_number + 1)}{number + 1}")
        """ down - leftwards: letter - 1, number - 1 """
        if current_letter_number - 1 in range(1, 9) and number - 1 in range(1, 9):
            moves.append(f"{self.utils.number_to_letter(current_letter_number - 1)}{number - 1}")
        """ up - leftwards: letter - 1, number + 1 """
        if current_letter_number - 1 in range(1, 9) and number + 1 in range(1, 9):
            moves.append(f"{self.utils.number_to_letter(current_letter_number - 1)}{number + 1}")
        """ down - rightwards: letter + 1, number - 1 """
        if current_letter_number + 1 in range(1, 9) and number - 1 in range(1, 9):
            moves.append(f"{self.utils.number_to_letter(current_letter_number + 1)}{number - 1}")
        return moves



