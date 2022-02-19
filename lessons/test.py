"""Test."""

# sound: str = ""
# i: int = 1  
# while i < 20: 
#     count: int = 0  # each time the outer loop runs, count is reassigned to 0
#     while count < 4:
#         i *= 2  # increase the value in i, the counter variable for the outer loop
#         count += 1  # increment count, the counter variable for the inner loop
#         sound += "e"
#     sound += "-iii-"
# sound += "oh"

# print(sound)  # will print the string "eeee-iii-eeee-iii-oh"


# # a function writing exercise
# def only(word: str) -> str:
#     """only the word!"""
#     new_word: str = ""
#     i: int = 0
#     while i < len(word):
#         if word[i] != " ":
#             new_word = new_word + word[i]
#         i = i + 1
#     return new_word

# x: float = 5.0
# y: float = 3.0

# x = x - 1
# if x < y:
#     z = x ** y / 2
# else:
#     if x == y: 
#         z = y % x
#     else: 
#         x = x / 2
#         z = y - x
#     z = z + 1
# print(z)

# ys: list[int] = [110, 120]
# for y in ys: 
#     print(y)

i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
    y: int = ys[i]
    print(y)
    i += 1