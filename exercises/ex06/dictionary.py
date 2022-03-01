"""Dictionary Functions."""

__author__ = 730231293


def invert(x: dict[str, str]) -> dict[str, str]:
    """Inverts the provided dictionary so that the new dictionary has the initial dictionary's key as its value and value as its key."""
    new_dictionary: dict[str, str] = {}
    for key in x:
        new_dictionary[x[key]] = key
    if len(new_dictionary) < len(x):
        raise KeyError("Duplicate value.")
    return new_dictionary


def favorite_color(x: dict[str, str]) -> str:
    """Returns the most common value in a dictionary, in this case, a color. If two values are equal and highest, it returns the first of the two."""
    if x == {}:
        return ""
    color_list: list[str] = []
    count_dictionary: dict[str, int] = {}
    final_dictionary: dict[int, str] = {}
    for key in x:
        color_list.append(x[key])
    for item in color_list:
        count_dictionary[item] = 0
    for item in color_list:
        if item in count_dictionary:
            count_dictionary[item] += 1
    for key in count_dictionary:
        final_dictionary[count_dictionary[key]] = key
    max_count: int = max(final_dictionary)
    for key in count_dictionary:
        if count_dictionary[key] == max_count:
            return str(key)


def count(x: list[str]) -> dict[str, int]:
    """Counts the number of times each unique string item occurs in a string, and places this into a dictionary where the key is the item and the value is the occurrence."""
    new_dictionary: dict[str, int] = {}
    for item in x:
        if item in new_dictionary:
            new_dictionary[item] += 1
        else:
            new_dictionary[item] = 1
    return new_dictionary