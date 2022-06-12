import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    show_rules()

    while True:
        secret_num = get_secret_num()

        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.\n")

        guesses_made = 1

        while guesses_made <= MAX_GUESSES:
            guess = get_guess(guesses_made)

            clues = get_clues(guess, secret_num)

            print(clues + "\n")

            guesses_made += 1

            if guess == secret_num:
                break
            if guesses_made > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}.")

        if not input("Do you wanna play again? y/n: ").lower().startswith("y"):
            break

        print("\n")

    print("Thanks for playing!")


def show_rules():
    print(
        f"""
I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:

When I say:    That means:
Pico           One digit is correct but in the wrong position.
Fermi          One digit is correct and in the right position.
Bagels         No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.
    """
    )


def get_secret_num():
    numbers = [str(i) for i in range(10)]
    random.shuffle(numbers)
    secret_num = "".join(numbers[:3])

    return secret_num


def get_guess(guesses_made):
    guess = ""

    while len(guess) != NUM_DIGITS or not guess.isdecimal():
        guess = input(f"Guess #{guesses_made}: ")

    return guess


def get_clues(guess, secret_num):
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()

        return " ".join(clues)


if __name__ == "__main__":
    main()
