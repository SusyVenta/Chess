class Utils:
    def get_current_letter(self, tag_position):
        return tag_position[0]

    def get_current_number(self, tag_position):
        return tag_position[1]

    def letter_to_number(self, letter):
        letters_and_numbers = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        return letters_and_numbers[letter]

    def number_to_letter(self, number):
        numbers_and_letters = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}
        return numbers_and_letters[number]

    def all_numbers_except_current_list(self, current_number):
        all_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        all_numbers.remove(current_number)
        return all_numbers

    def all_letters_except_current_list(self, current_letter):
        all_letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        all_letters.remove(current_letter)
        return all_letters

    def end_position_is_free(self, end_coordinates, pieces_position):
        if end_coordinates in pieces_position.keys():
            return False
        return True

    def end_position_contains_opponent_piece(self, piece_moved, end_coordinates, pieces_position):
        if end_coordinates in pieces_position.keys():
            if (piece_moved.islower() and pieces_position[end_coordinates].isupper()) or (
                    piece_moved.isupper() and pieces_position[end_coordinates].islower()):
                return True
        return False

    def is_white_moving(self, piece_moved):
        return piece_moved.isupper()
