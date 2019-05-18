alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(letter):
    letter = letter.lower()
    return alphabet.find(letter)


def rotate_character(char, rot):
    is_upper = char.isupper()
    original_position = alphabet_position(char)
    if original_position == -1:
        return char
    new_position = (original_position + rot) % 26
    new_char = alphabet[new_position]
    return new_char.upper() if is_upper else new_char
