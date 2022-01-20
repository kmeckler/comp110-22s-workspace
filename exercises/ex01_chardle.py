"""EX01: Chardle - Input, Variables, and Conditionals"""
"""Wordle 1/20/21 is ROBOT."""

__author__ = "730231293"

"""Part 1: Prompting for Inputs"""
chardle: str = input("Enter a 5-character word")
character: str = input("Enter a single character")
print("Searching for " + character + " in " + chardle)


"""Part 2: Checking Indices for Matches"""
if chardle == "heels":
    if character == "h": 
        print("h found at index 0")
    else:
        if character == "e":
            print("e found at index 1")
            print("e found at index 2")
        else:
            if character == "l":
                print("l found at index 3")
            else: 
                if character == "s":
                    print("s found at index 4")
                else:
                    print("character not found")
else: 
    if chardle == "hello":
        if character == "h": 
            print("h found at index 0")
        else:
            if character == "e":
                print("e found at index 1")
            else:
                if character == "l":
                    print("l found at index 2")
                    print("l found at index 3")
                else: 
                    print("character not found")
    else: 
        print("try another word (hint: 'hello' or 'heels'")

"""Part 3: Counting Machine Indices"""