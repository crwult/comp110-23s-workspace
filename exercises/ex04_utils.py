"""Remaking list utils."""
__author__ = "730552290"

<<<<<<< HEAD

def all(checked_list: list[int], match: int) -> bool:
    """Checks list to see if it's all the same number."""
    if len(checked_list) == 0:
        return False
=======
def all(checked_list: list[int], match: int) -> bool:
    """Checks list to see if it's all the same number"""
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
    idx: int = 0
    while idx < len(checked_list):
        if checked_list[idx] != match:
            return False
        idx += 1
    return True

<<<<<<< HEAD

def max(max_list: list[int]) -> int:
    """When given a list, returns the maximum value in the list."""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
=======
def max(max_list: list[int]) -> int:
    """When given a list, returns the maximum value in the list"""
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    else :
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
        max_idx = 1
        filler = max_list[0]
        while max_idx < len(max_list):
            if max_list[max_idx] > filler:
                filler = max_list[max_idx]
            max_idx += 1
        return filler

<<<<<<< HEAD

=======
>>>>>>> 98d20176a9ea5b957532c2fc41bb320a194a0d80
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