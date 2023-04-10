def value_exists(dict_1: dict[str: int], num: int) -> bool:
    """is number in dictionary as value?"""
    is_in: bool = False
    for key in dict_1:
        if dict_1[key] == num:
            is_in = True
    return is_in

test_dict : dict [str ,int] = {"a": 2 , "b": 4 , "c": 7 , "d": 1}
test_val : int = 5
print(value_exists(test_dict, test_val))