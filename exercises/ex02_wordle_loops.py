"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730231293"

secret: str = input("What is your 6-letter guess? ")
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
wordle: str = "python"
i = 0
result = str = ""

while len(secret) != 6:
    secret = input("That was not 6 letters! Try again: ")

if secret != wordle:
    while i < len(wordle):
        if secret[i] != wordle[i]:
            result = result + white_box
        else: 
            result = result + green_box
        i = i + 1
    print(result)
    print("Not quite. Play again soon!")
else: 
    print(green_box * 6)
    print("Woo! You got it!")