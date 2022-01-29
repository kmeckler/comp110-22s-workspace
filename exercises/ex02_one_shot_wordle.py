"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730231293"

wordle: str = "python"
wordle_len: str = str((len(wordle)))
secret: str = input("What is your " + wordle_len + "-letter guess? ")
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
i: int = 0
result: str = ""


while len(secret) != len(wordle):
    secret = input("That was not " + wordle_len + " letters! Try again: ")

if secret != wordle:
    while i < len(wordle):
        if secret[i] != wordle[i]:
            j: int = 0
            match_test: bool = False
            while j < len(wordle):
                if secret[i] == wordle[j]:
                    match_test = True
                j = j + 1
            if match_test is True:
                result += yellow_box
            else:
                result += white_box
        else:
            result += green_box
        i = i + 1
    print(result)
    print("Not quite. Play again soon!")
else: 
    print(green_box * len(wordle))
    print("Woo! You got it!")