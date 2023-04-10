def odd_and_even(input_list: list[int]) -> list[int]:
    """Takes a list and outputs a list with the odd numbers with an even index."""
    new_list: list[int] = []
    i: int = 0
    for elem in input_list:
        if i % 2 == 0:
            if elem % 2 == 1:
                new_list.append(elem)
        i += 1
    return new_list

print(odd_and_even([1,2,3,4,5,6,7]))

