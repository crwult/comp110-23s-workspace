"""Storing the functions for data wrangling."""
__author__ = "730552290"


def read_csv_rows(filename:str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts ith header key"""
    from csv import DictReader
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str,str]], header:str) -> list [str]:
    """Returns values in a table under a certain header"""
    result: list[str] = []
    #step through table
    #save every value under the key header
    for diction in table:
        result.append(diction[header])
    return result

def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys"""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result

def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produces a column based table of just the first n rows of the input table."""
    empty_dict: dict[str, list[str]] = {}
    for key in table:
        empty_list: list[str] = []
        table_list: list[str] = table[key]
        for num in range (0, rows):
            empty_list.append(table_list[num])
        empty_dict[key] = empty_list
    return empty_dict


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produces a column based table of just the specified columns of an input variable."""
    empty_dict: dict[str, list[str]] = {}
    for elem in columns:
        empty_dict[elem] = table[elem]
    return empty_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column based tables"""
    empty_dict: dict[str, list[str]] = {}
    for key in table_1:
        empty_dict[key] = table_1[key]
    for key in table_2:
        if key in empty_dict:
            empty_dict[key] = empty_dict[key] + table_2[key]
        else:
            empty_dict[key] = table_2[key]
    return empty_dict

def count(count_list: list[str]) -> dict[str, int]:
    """Counts how many of each value is in a list."""
    new_dict: dict[str, int] = {}
    for elem in count_list:
        new_dict[elem] = 0
    for elem in count_list:
        new_dict[elem] += 1
    return new_dict
