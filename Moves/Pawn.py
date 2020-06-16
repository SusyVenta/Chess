from Chess.Utils import Utils


class Pawn:
    def __init__(self, piece):
        self.piece = piece
        self.utils = Utils()

    def move_is_possible(self, start_tag, end_tag):
        return end_tag in self.get_all_allowed_moves(start_tag)

    def get_all_allowed_moves(self, start_tag):
        current_coordinate_number = int(self.utils.get_current_number(start_tag))
        print(f"current_coordinate_number: {current_coordinate_number}")
        current_coordinate_letter = self.utils.get_current_letter(start_tag)
        print(f"current_coordinate_letter: {current_coordinate_letter}")
        all_moves = []

        if self.is_white_moving():
            if current_coordinate_number == 2:
                if current_coordinate_number + 2 in range(1, 9):
                    all_moves.append(f"{current_coordinate_letter}{current_coordinate_number + 2}")
            if current_coordinate_number + 1 in range(1, 9):
                all_moves.append(f"{current_coordinate_letter}{current_coordinate_number + 1}")
        else:
            if current_coordinate_number == 7:
                if current_coordinate_number - 2 in range(1, 9):
                    all_moves.append(f"{current_coordinate_letter}{current_coordinate_number - 2}")
            if current_coordinate_number - 1 in range(1, 9):
                all_moves.append(f"{current_coordinate_letter}{current_coordinate_number - 1}")
        print(all_moves)

        #todo: add en passant
        # if white moving and num=5 and black pawn in num=5, letter +/- 1 and black just moved by 2.
        # if black moving and num=4 and white pawn in num=4, letter +/-1 and white just moved by 2
        return all_moves

    def is_white_moving(self):
        return self.piece.isupper()
