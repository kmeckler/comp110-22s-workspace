"""Eight Ball."""

# An oracle that predicts the future.
# Syntactical sugar: relative reassignment operators and elif statements

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0, 3)

if response == 0: 
    print("most definitely")
elif response == 1:
    print("likely")
elif response == 2:
    print("ask again later")
else:
    print("not a chance")