"""Dictionary related utility functions."""

__author__ = ""

from csv import DictReader


# Define your functions below

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open handle of file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Read data as csv and not strings
    csv_reader = DictReader(file_handle)

    # Read csv line by line
    for row in csv_reader:
        result.append(row)

    # Close file
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)
    
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    
    return result
    

def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns n rows of given data."""
    result: dict[str, list[str]] = {}
    for column in table:
        values: list[str] = []
        if len(table[column]) < n:
            n = len(table[column])
        for i in range(n):
            values.append(table[column][i])
        result[column] = values
    return result


def select(table: dict[str, list[str]], choice: list[str]) -> dict[str, list[str]]:
    """Selecting columns from table."""
    result: dict[str, list[str]] = {}

    for label in choice:
        result[label] = table[label]

    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Joins two tables."""
    result: dict[str, list[str]] = {}
    for column1 in table1:
        result[column1] = table1[column1]
    
    for column2 in table2:
        if column2 in result:
            result[column2] += table2[column2]
        else:
            result[column2] = table2[column2]
    
    return result


def count(frequency_columns: list[str]) -> dict[str, int]:
    """Counts frequencies of values."""
    result: dict[str, int] = {}
    for i in frequency_columns:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result