"""Practice with Dictionaries."""
__author__ = "730552290"


def count(d: dict[str, str]) -> dict[str, int]:
    """Counts how many of each value is in a dictionary."""
    new_dict = {}
    for elem in d:
        new_dict[d[elem]] = 0
    for elem in d:
        new_dict[d[elem]] += 1
    return new_dict



def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    count_dict = count(d)
    for elem in count_dict:
        if count_dict[elem] != 1:
            raise KeyError("there are duplicate values. This dictionary cannot be inverted.")
    new_d = {}
    for elem in d:
        new_d[d[elem]] = elem
    return new_d

def favorite_color(d: dict[str,str]) -> str:
    """Gets names and favorite colors and returns which color is the most popular."""
    count_d: dict[str, int] = count(d)
    winning_number = 0
    for elem in count_d:
        if count_d[elem] > winning_number:
            fav_color = elem
            winning_number = count_d[elem]
    return fav_color

print(count({"me": "Community", "Bennett": "Riverdale", "Sergiy": "Riverdale"}))
