"""Testing dictionary functions."""
__author__ = "730552290"


from exercises.ex07.dictionary import count, invert, favorite_color
import pytest


def test_invert_icecream() -> None:
    """Use Case: Inverts dictionary with people and their favorite icecream."""
    normal_dict: dict[str, str] = {"me": "chocolate", "Bennett": "Mint Chocolate Chip", "Sergiy": "Ranch?"}
    inverted_dict: dict[str, str] = {"chocolate": "me", "Mint Chocolate Chip": "Bennett", "Ranch?": "Sergiy"}
    assert invert(normal_dict) == inverted_dict


def test_invert_movie() -> None:
    """Use Case: Inverts dictionary with people and their favorite movies."""
    normal_dict: dict[str, str] = {"me": "Miracle", "Bennett": "Get Out", "Sergiy": "Barbie Maraposa"}
    inverted_dict: dict[str, str] = {"Miracle": "me", "Get Out": "Bennett", "Barbie Maraposa": "Sergiy"}
    assert invert(normal_dict) == inverted_dict


def test_invert_show() -> None:
    """Edge Case: Check if two repeated values gives a KeyError."""
    with pytest.raises(KeyError):
        normal_dict: dict[str, str] = {"me": "Community", "Bennett": "Riverdale", "Sergiy": "Riverdale"}
        invert(normal_dict)


def test_fav_col_1() -> None:
    """Use Case: Checks if the favorite color is blue."""
    normal_dict: dict[str, str] = {"me": "blue", "Bennett": "blue", "Sergiy": "blue"}
    assert favorite_color(normal_dict) == "blue"


def test_fav_col_2() -> None:
    """Use Case: Checks if the favorite color is blue.."""
    normal_dict: dict[str, str] = {"me": "blue", "Bennett": "blue", "Sergiy": "red"}
    assert favorite_color(normal_dict) == "blue"


def test_fav_col_equal() -> None:
    """Edge Case: Checks if the favorite color is blue, if the first person picks blue and the rest choose something different."""
    normal_dict: dict[str, str] = {"me": "blue", "Bennett": "red", "Sergiy": "yellow"}
    assert favorite_color(normal_dict) == "blue"


def test_count_movies() -> None:
    """Use Case: counts movies in a list."""
    normal_dict: list[str] = {"Miracle", "Get Out", "Barbie Maraposa"}
    count_dict: dict[str, int] = {"Miracle": 1, "Get Out": 1, "Barbie Maraposa": 1}
    assert count(normal_dict) == count_dict


def test_count_shows() -> None:
    """Use Case: counts shows in a list."""
    normal_dict: list[str] = ["Community", "Community", "You", "Riverdale"]
    count_dict: dict[str, int] = {"Community": 2, "Riverdale": 1, "You": 1}
    assert count(normal_dict) == count_dict


def test_count_empty() -> None:
    """Edge Case: Sees if counting an empty list results in an empty dictionary."""
    normal_dict: dict[str, str] = {}
    count_dict: dict[str, int] = {}
    assert count(normal_dict) == count_dict