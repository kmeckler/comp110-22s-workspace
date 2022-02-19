"""Testing the skeleton functions of utils.py."""

__author__ = "730231293"


from exercises.ex05.utils import only_evens, sub, concat


# For only_evens
#     Test that using an odd number results in an empty list
#     Test that using two even numbers results in two matching list items
#     Test that using one even and one odd only returns the even in a list


def test_only_evens_odd_only() -> None:
    """Tests that when given a list of odd values, an empty list is returned."""
    assert only_evens([13]) == []


def test_only_evens_even_only() -> None:
    """Tests that when given a list of even values, those same values are returned in a list."""
    assert only_evens([12, 14]) == [12, 14]


def test_only_evens_both() -> None:
    """Tests that when given both even and odd list values, only the even values are returned in a list."""
    assert only_evens([12, 13, 14]) == [12, 14]


# For sub
#     Test that when given indices within the length of the list, the correct subset is returned
#     Test that when given a start index that is too small and end index is too large, the entire list is returned
#     Test that when given an empty list, an empty list is returned


def test_sub_possible_values() -> None:
    """Tests that when given indices within the length of the list, the correct subset is returned."""
    assert sub([12, 13, 14], 0, 2) == [12, 13]


def test_sub_impossible_start_end() -> None:
    """Tests that when given a start index that is negative, the returned values are start at index 0 and stop before the upper index."""
    assert sub([12, 13, 14], -12, 14) == [12, 13, 14]


def test_sub_empty() -> None:
    """Tests that when given an empty list, an empty list is returned."""
    assert sub([], -12, 14) == []


# For concat
#     Test that two lists are concatendated
#     Test that when one list is empty, only the list that is not empty is returned
#     Test that when both lists are empty, an empty list is returned


def test_concat_two_lists() -> None:
    """Tests that two lists are concatendated when two are provided."""
    assert concat([12, 13], [14]) == [12, 13, 14]


def test_concat_one_empty() -> None:
    """Tests that when one list is empty, only the value-containing."""
    assert concat([], [12, 13, 14]) == [12, 13, 14]


def test_concat_both_empty() -> None: 
    """Test that when both input lists are empty, an empty list is returned."""
    assert concat([], []) == []