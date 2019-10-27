from Util import *
from Pieces import *


class Pawn(Pieces):
    def get_unicode_symbols(self):
        return {"P": u"♙", "p": u"♟"}

    def possible_moves(self, current_tag_position):
        current_number = get_current_number(current_tag_position)
        current_letter = get_current_letter(current_tag_position)
