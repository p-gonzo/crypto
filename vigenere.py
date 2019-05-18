from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    current_key_index = 0
    key_len = len(key)
    
    resulting_chars = []
    for idx, char in enumerate(text):
        if alphabet_position(char) != -1:
            resulting_chars.append(rotate_character(char, alphabet_position(key[current_key_index])))
            current_key_index = (current_key_index + 1) % key_len
        else:
            resulting_chars.append(char)
    return "".join(resulting_chars)



def main():
    text = input("Type a message: ")
    key = input("Encryption key: ")
    print(encrypt(text, key))

if __name__ == "__main__":
    main()
