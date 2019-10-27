class Pieces:
    def __init__(self):
        self.current_configuration = {}
        self.all_configurations = {}

    def get_possible_moves(self, piece_tag):
        