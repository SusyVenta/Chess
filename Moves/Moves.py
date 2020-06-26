from Chess.Moves.Rook import Rook
from Chess.Moves.Bishop import Bishop
from Chess.Moves.King import King
from Chess.Moves.Knight import Knight
from Chess.Moves.Pawn import Pawn
from Chess.Moves.Queen import Queen


class Moves:
    def move_is_possible(self, piece, start_tag, end_tag, all_turns_pieces_position, max_turn):
        if piece.lower() != "p":
            return self.get_piece_class(piece).move_is_possible(start_tag, end_tag,
                                                                all_turns_pieces_position[max_turn])
        else:
            return self.get_piece_class(piece).move_is_possible(start_tag, end_tag,
                                                                all_turns_pieces_position, max_turn)

    def get_all_possible_moves(self, piece, start_tag):
        return self.get_piece_class(piece).get_all_allowed_moves(start_tag)

    def get_piece_class(self, piece):
        """ Piece moving needs to be passed to know if white or black is moving and see if path is free  """
        piece_letter_to_class_map = {
            "r": Rook(piece),
            "k": Knight(),
            "b": Bishop(piece),
            "q": Queen(piece),
            "ki": King(),
            "p": Pawn(piece)
        }
        return piece_letter_to_class_map[piece.lower()]
