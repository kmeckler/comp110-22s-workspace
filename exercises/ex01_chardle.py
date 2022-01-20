"""EX01: Chardle - Input, Variables, and Conditionals."""
# The Wordle for 1/20/21 is ROBOT.

__author__ = "730231293"

chardle: str = input("Enter a 5-character word: ")
instances: int = 0

if len(chardle) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + chardle)

if chardle[0] == character:
    print(character + " found at index 0")
    instances = instances + 1
if chardle[1] == character:
    print(character + " found at index 1")
    instances = instances + 1
if chardle[2] == character:
    print(character + " found at index 2")
    instances = instances + 1
if chardle[3] == character:
    print(character + " found at index 3")
    instances = instances + 1
if chardle[4] == character:
    print(character + " found at index 4")
    instances = instances + 1
if instances > 1:
    print(str(instances) + " instances of " + character + " found in " + chardle)
else: 
    if instances == 1: 
        print(str(instances) + " instance of " + character + " found in " + chardle)
    else: 
        print("No instances of " + character + " found in " + chardle)

 