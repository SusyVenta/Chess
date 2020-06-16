from Chess.Moves.Rook import Rook
from Chess.Moves.Bishop import Bishop
from Chess.Moves.King import King
from Chess.Moves.Knight import Knight
from Chess.Moves.Pawn import Pawn
from Chess.Moves.Queen import Queen


class Moves:
    def move_is_possible(self, piece, start_tag, end_tag):
        return self.get_piece_class(piece).move_is_possible(start_tag, end_tag)

    def get_all_possible_moves(self, piece, start_tag):
        return self.get_piece_class(piece).get_all_allowed_moves(start_tag)

    def get_piece_class(self, piece):
        piece_letter_to_class_map = {
            "r": Rook(),
            "k": Knight(),
            "b": Bishop(),
            "q": Queen(),
            "ki": King(),
            "p": Pawn()
        }
        return piece_letter_to_class_map[piece.lower()]
