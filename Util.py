def get_current_letter(tag_position):
    return tag_position[0]


def get_current_number(tag_position):
    return tag_position[1]


def letter_to_number(letter):
    letters_and_numbers = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    return letters_and_numbers[letter]


def number_to_letter(number):
    numbers_and_letters = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
    return numbers_and_letters[number]
