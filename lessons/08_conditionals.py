"""Conditional (if-else) Statements."""

SECRET: int = 3

print("I'm thinking of a value between 1 and 5, what is it?")
guess: int = int(input("What is your guess?"))

if guess == SECRET: 
    print("You guessed correctly!!!")
    print("Have a wonderful day.")
else: 
    print("Incorrect.")
    if guess > SECRET:
        print("Too high.")
    else: 
        print("Too low.")

print("Game over.")