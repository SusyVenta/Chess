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

        
        vertical_moves = self.get_vertical_moves_possible(current_coordinate_letter, current_coordinate_number)
        print(vertical_moves)
        horizontal_moves = self.get_horizontal_moves_possible(current_coordinate_letter, current_coordinate_number)
        print(horizontal_moves)
        all_moves = vertical_moves + horizontal_moves
        print(all_moves)
        return all_moves
