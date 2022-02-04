"""EX03 - Structured Wordle."""

__author__ = "730231293"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(wordle: str, character: str) -> bool:
    """Returns True if the character is found at any index of the guess, otherwise False."""
    assert len(character) == 1
    i: int = 0
    while i < len(wordle):
        if wordle[i] == character:
            return True
        i = i + 1
    return False


def emojified(guess: str, wordle: str) -> str:
    """Returns a white box if contains_char is False, a yellow if True but not a position match, and green if True and a position match."""
    assert len(guess) == len(wordle)
    j: int = 0
    result: str = ""
    while j < len(wordle):
        if guess[j] == wordle[j]:
            result += GREEN_BOX
        else:
            if contains_char(wordle, guess[j]) is True:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        j += 1  
    return result   


def input_guess(expected_length: int) -> str:
    """Ensures user inputs a guess of the correct character length."""
    prompt = input("Enter a " + str(expected_length) + " character word: ")
    while len(prompt) != expected_length:
        prompt = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return prompt


def main() -> None:
    """The entrypoint of the program and main game loop."""
    n: int = 1
    wordle: str = "codes"
    len_wordle: int = len(wordle)
    won: bool = False
    while n < len(wordle) + 2 and not won:
        print("=== Turn " + str(n) + "/" + str(len_wordle + 1) + "===")
        guess: str = input_guess(len_wordle)
        print(emojified(guess, wordle))
        if guess == wordle:
            print("You won in " + str(n) + "/" + str(len_wordle + 1) + " turns!")
            won = True
            return
        else:
            n += 1
    print("X/" + str(len_wordle + 1) + "- Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()