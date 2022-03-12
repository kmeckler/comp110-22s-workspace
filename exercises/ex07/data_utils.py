"""Dictionary related utility functions."""

__author__ = "730231293"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a stored CSV file into a list of rows, each row represented as a dict[str, str], into memory."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
   
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
   
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table (list[dict[str, str]]) to a column-oriented table (dict[str, list[str]])."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Given a column-based table, generate a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in column_table: 
        i: int = 0
        column_selection: list[str] = []
        if rows >= len(column_table[column]):
            rows = len(column_table[column]) - 1
        while i < rows:
            item: str = column_table[column][i]
            column_selection.append(item)
            i += 1
        result[column] = column_selection
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Given a column-based table, generate a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in column_names: 
        result[item] = column_table[item]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a single, combined column-based table from two, separate column-based tables."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else: 
            result[column] = table_2[column]
    return result


def count(list: list[str]) -> dict[str, int]:
    """Given a list of strings, produce a dictionary where each key is equal to an item in the string and each value is the count of the number of times that item appeared in the input list."""
    result: dict[str, int] = {}
    for item in list:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result