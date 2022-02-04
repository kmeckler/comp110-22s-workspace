"""EX03 - Structured Wordle."""

__author__ = "730231293"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


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
    """Returns a white box if False, a yellow if True but not a position match, and green if True and a position match."""
    assert len(guess) == len(wordle)
    j: int = 0
    result: str = ""
    while j < len(wordle):
        if guess[j] == wordle[j]:
            result += green_box
        else:
            if contains_char(wordle, guess[j]) is True:
                result += yellow_box
            else:
                result += white_box
        j += 1  
    return result   


def input_guess(expected_length: int) -> str:
    """Ensures guess of correct character length."""
    prompt = input("Enter a " + str(expected_length) + " character word: ")
    while len(prompt) != expected_length:
        prompt = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return prompt


def main() -> None:
    """The entrypoint of the program and main game loop."""
    n: int = 1
    print("=== Turn " + str(n) + "/6 ===")
    input_guess(6)