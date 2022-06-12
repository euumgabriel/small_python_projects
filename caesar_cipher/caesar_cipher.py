try:
    import pyperclip
except:
    pass

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    show_intro()

    mode = get_user_option()
    key = get_key()
    message = get_message(mode)
    translated = translate(message, mode, key)

    print(translated)

    try:
        pyperclip.copy(translated)
        print(f"Full {mode}ed text copied to clipboard.")
    except:
        pass


def show_intro():
    print(
        """
The Caesar cipher encrypts letters by 
shifting them over by a key number. For 
example, a key of 2 means the letter A is
encrypted into C, the letter B encrypted 
into D, and so on.
    """
    )


def get_user_option():
    while True:
        response = input("Do you wanna to (e)ncrypt or (d)ecrypt? ").lower()

        if response.startswith("e"):
            return "encrypt"
        elif response.startswith("d"):
            return "decrypt"
        else:
            print("Please enter the letter e or d.")


def get_key():
    while True:
        max_key = len(SYMBOLS) - 1

        response = input(f"Please enter the key (0 to {max_key}): ")

        if not response.isdecimal():
            continue

        key = int(response)

        if 0 <= key < len(SYMBOLS):
            return key


def get_message(mode):
    return input(f"Enter the message to {mode}: ").upper()


def translate(message, mode, key):
    translated = ""

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)

            if mode == "encrypt":
                num += key
            else:
                num -= key

            if num >= len(SYMBOLS):
                num -= len(SYMBOLS)
            elif num < 0:
                num = num + len(SYMBOLS)

            translated += SYMBOLS[num]
        else:
            translated += symbol

    return translated


if __name__ == "__main__":
    main()
