def zip(list_1:list[str], list_2: list[int]) -> dict[str, int]:
    """Returns list where keys are items of first list and values are items of second"""
    output_dict = {}
    if len(list_1) != len(list_2):
        return output_dict
    if len(list_1) == 0:
        return output_dict
    for idx in range (len(list_1)):
        output_dict[list_1[idx]] = list_2[idx]
    return output_dict

