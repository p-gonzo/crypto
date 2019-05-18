from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    return "".join([rotate_character(char, rot) for char in text])


def main():
    text = input("Type a message: ")
    rot = int(input("Rotate by: "))
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()
