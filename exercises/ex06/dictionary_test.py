"""Unit tests of dictionary functions from dictionary.py."""

__author__ = 730231293


from exercises.ex06.dictionary import invert, favorite_color, count
import pytest


def test_invert_use1() -> None: 
    """Use 1: Tests that when given a dictionary of 2 key-value pairs, the outputted dictionary has 2 key-value pairs with the initial dictionary's key as its value and value as its key."""
    dict0: dict[str, str] = {'A': 'B', 'C': 'D'}
    assert invert(dict0) == {'B': 'A', 'D': 'C'}


def test_invert_use2() -> None: 
    """Use 2: Tests that when given a dictionary of 6 key-value pairs, the outputted dictionary has 6 value-pairs with the initial dictionary's key as its value and value as its key."""
    dict1: dict[str, str] = {'Apple': 'Banana', 'Carrot': 'Delicious', "Eggplant": "Fruit", "Garbage": "Hello", "Ice": "Jelly", "Kiwi": "Lemon"}
    assert invert(dict1) == {'Banana': 'Apple', 'Delicious': 'Carrot', 'Fruit': 'Eggplant', 'Hello': 'Garbage', 'Jelly': 'Ice', 'Lemon': 'Kiwi'}


def test_invert_edge1() -> None:
    """Edge 1: Tests that when given an empty dictionary, an empty dicitonary is returned."""
    dict2: dict[str, str] = {}
    assert invert(dict2) == {}


def test_invert_optional() -> None:
    """Optional: Tests that when two matching values are input, KeyError is returned."""
    with pytest.raises(KeyError):
        dictx: dict[str, str] = {"B": "A", "C": "A"}
        invert(dictx)


def test_count_use1() -> None:
    """Use 1: Tests that the function, when given a list of 10 total values and 4 unique values, returns a dictionary with 4 key-value pairs which uses the value to count the number of times each unique string item occurs."""
    list0: list[str] = ["A", "B", "B", "C", "C", "C", "D", "D", "D", "D"]
    assert count(list0) == {'A': 1, 'B': 2, 'C': 3, 'D': 4}


def test_count_use2() -> None: 
    """Use 2: Tests that the function, when given a list of str values, returns a dictionary which counts the number of times each unique string item occurs as the value for a key which matches each unique string item."""
    list1: list[str] = ["D", "A", "B", "C", "D", "B", "C", "D", "C", "D"]
    assert count(list1) == {'A': 1, 'B': 2, 'C': 3, 'D': 4}


def test_count_edge1() -> None: 
    """Edge 1: Tests that when given an empty list, an empty dictionary is returned."""
    list2: list[str] = []
    assert count(list2) == {}


def test_favorite_color_use1() -> None:
    """Use 1: Tests that when given a dictionary of key names and color values, the color that occurs most frequently is returned."""
    dict0: dict[str, str] = {"Adam": "Blue", "Bradley": "Dark Green", "Carter": "Dark Green"}
    assert favorite_color(dict0) == "Dark Green"


def test_favorite_color_use2() -> None:
    """Use 2: Tests that when two colors are represented an equal and highest amount of times, the first color encountered is returned."""
    dict1: dict[str, str] = {"Adam": "Blue", "Bradley": "Dark Green", "Carter": "Dark Green", "Damien": "Blue"}
    assert favorite_color(dict1) == "Blue"


def test_favorite_color_edge1() -> None:
    """Use 3: Tests that when given an empty dictionary, an empty string is returned."""
    dict2: dict[str, str] = {}
    assert favorite_color(dict2) == ""