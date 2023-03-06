"""Testing my new util functions."""
__author__ = "730552290"

from exercises.ex05.utils import only_evens, sub, concat

def test_one_to_five_evens() -> None:
    """Use case seeing if only evens returns evens from the list of 1-5"""
    one_to_five: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(one_to_five) == [2,4]

def test_six_to_ten_evens() -> None:
    """Use case seeing if only evens returns evens from the list of 6-10"""
    six_to_ten: list[int] = [6, 7, 8, 9, 10]
    assert only_evens(six_to_ten) == [6, 8, 10]

def test_empty_evens() -> None:
    """edge case seeing if only_evens returns an empty list when an empty list is inputted"""
    empty_list: list[int] = []
    assert only_evens(empty_list) == []

def test_even_concat() -> None:
    """Use case seeing if I can get lists 2,4 + 6,8,10 to be 2,4,6,8,10"""
    concat_evens_1: list[int] = [2, 4]
    concat_evens_2: list[int] = [6, 8, 10]
    assert concat(concat_evens_1, concat_evens_2) == [2, 4, 6, 8, 10]

def test_odd_concat() -> None:
    """Use case seeing if I can get lists 1,3,5+7,9 to be 1,3,5,7,9"""
    concat_odds_1: list[int] = [1, 3, 5]
    concat_odds_2: list[int] = [7, 9]
    assert concat(concat_odds_1, concat_odds_2) == [1, 3, 5, 7, 9]

def test_empty_concat() -> None:
    """Edge case: Will using concat on two empty lists return an empty list"""
    concat_empty_1: list[int] = []
    concat_empty_2: list[int] = []
    assert concat(concat_empty_1, concat_empty_2) == []

def test_even_sub() -> None:
    """Use case: Will sub work correctly for beginning of even list"""
    sub_even: list[int] = [2, 4, 6, 8, 10]
    assert sub(sub_even, 0, 2) == [2, 4]

def test_odd_sub() -> None:
    """Use case: Will sub work correctly for end of odd list"""
    sub_odd: list[int] = [1, 3, 5, 7, 9]
    assert sub(sub_odd, 2, 5) == [5, 7, 9]

def test_start_too_high() -> None:
    """Edge case: Will sub return empty list if the start index is way too high"""
    evens: list[int] = [2, 4, 6, 8, 10]
    assert sub(evens, 6, 2) == []