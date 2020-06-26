from Chess.Utils import Utils
from Chess.Moves.Rook import Rook
from Chess.Moves.Bishop import Bishop


class Queen:
    def __init__(self, piece_moving):
        self.utils = Utils()
        self.piece_moving = piece_moving

    def move_is_possible(self, start_tag, end_tag):
        return end_tag in self.get_all_allowed_moves(start_tag)

    def get_all_allowed_moves(self, start_tag):
        current_coordinate_number = int(self.utils.get_current_number(start_tag))
        print(f"current_coordinate_number: {current_coordinate_number}")
        current_coordinate_letter = self.utils.get_current_letter(start_tag)
        print(f"current_coordinate_letter: {current_coordinate_letter}")

        vertical_moves = Rook(self.piece_moving).get_vertical_moves_possible(current_coordinate_letter, current_coordinate_number)
        horizontal_moves = Rook(self.piece_moving).get_horizontal_moves_possible(current_coordinate_letter, current_coordinate_number)
        up_rightwards = Bishop(self.piece_moving).move_up_rightwards(current_coordinate_number, current_coordinate_letter)
        up_leftwards = Bishop(self.piece_moving).move_up_leftwards(current_coordinate_number, current_coordinate_letter)
        down_leftwards = Bishop(self.piece_moving).move_down_leftwards(current_coordinate_number, current_coordinate_letter)
        down_rightwards = Bishop(self.piece_moving).move_down_rightwards(current_coordinate_number, current_coordinate_letter)
        all_moves = vertical_moves + horizontal_moves + up_rightwards + up_leftwards + down_leftwards + down_rightwards
        print(all_moves)
        return all_moves

