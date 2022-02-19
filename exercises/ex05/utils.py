"""Setting up skeleton functions."""

__author__ = "730231293"


def only_evens(x: list[int]) -> list[int]:
    """Given a list of ints, returns a list containing only those input ints that are even."""
    subset: list[int] = list()
    i: int = 0
    while i < len(x):
        if x[i] % 2 == 0:
            subset.append(x[i])
        i += 1
    return subset


def sub(y: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints and two indices, returns a list with only the values from the input list which fall between the indices."""
    subset: list[int] = list()
    i: int = start
    if start < 0:
        i = 0
    if end > len(y):
        end = len(y)
    if len(y) == 0 or start > len(y) or end <= 0:
        return []
    while start <= i < end:
        subset.append(y[i])
        i += 1
    return subset


def concat(a: list[int], b: list[int]) -> list[int]:
    """Concatenates the values of two input lists into one list."""
    concatenated: list[int] = list()
    i: int = 0
    j: int = 0
    while i < len(a):
        concatenated.append(a[i])
        i += 1
    while j < len(b):
        concatenated.append(b[j])
        j += 1
    return concatenated