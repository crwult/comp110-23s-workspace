"""Learning to make list functions."""
__author__ = "730552290"


def only_evens(even_list: list[int]) -> list[int]:
    """returns only the even elements of a list"""
    copy_list: list[int] = []
    for elem in even_list:
        if elem % 2 == 0:
            copy_list.append(elem)
    return copy_list


def concat(list_1: list[int], list_2:list[int]) -> list[int]:
    """When two lists are parameters, it returns a list with all elements of both"""
    new_list = []
    for elem_1 in list_1:
        new_list.append(elem_1)
    for elem_2 in list_2:
        new_list.append(elem_2)
    return new_list


def sub(sub_list: list[int],start: int, end: int) -> list[int]:
    """subset of the given list, between the specified start index and the end index"""
    return_list = []
    if start < 0:
        start = 0
    if end > len(sub_list):
        end = len(sub_list)
    if (start >= len(sub_list) - 1) or (end < 1) or (start >= end - 1):
        return return_list
    for idx in range (start, end):
        return_list.append(sub_list[idx])
    return return_list

