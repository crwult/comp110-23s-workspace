"""Remaking list utils."""
__author__ = "730552290"

def all(checked_list: list[int], match: int) -> bool:
    """Checks list to see if it's all the same number"""
    idx: int = 0
    while idx < len(checked_list):
        if checked_list[idx] != match:
            return False
        idx += 1
    return True

def max(max_list: list[int]) -> int:
    """When given a list, returns the maximum value in the list"""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    else :
        max_idx = 1
        filler = max_list[0]
        while max_idx < len(max_list):
            if max_list[max_idx] > filler:
                filler = max_list[max_idx]
            max_idx += 1
        return filler

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if two lists are deeply equivalent."""
    if len(list_1) != len(list_2):
        return False
    else:
        equal_idx: int = 0
        while equal_idx < len(list_1):
            if list_1[equal_idx] != list_2[equal_idx]:
                return False
            equal_idx += 1
        return True