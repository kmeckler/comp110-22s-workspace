"""Example of writing a function to search a list."""

# Define a function named contains.
# Parameters: 
#   1. Needle - the str we're searchign for
#   2. Haystack - the list of str vlues we're searching through
# Returns True if needle is found in haystack
# Algorithm for each item in haystack,
#   Test if equal to needle.
#       If so, return True.
#   Otherwise, False.


def main() -> None:
    guess: str = input("What is the code word? ")
    possible_answers: list[str] = ["lotion", "please", "abracadabra"]
    if contains(guess, possible_answers):
        print("Welcome!")
    else:
        print("Nope. Bye.")


def contains(needle: str, haystack: list[str]) -> bool:
    """Test if needle is found in haystack."""
    for item in haystack:
        if item == needle:
            return True
    return False


if __name__ == "__main__":
    main()