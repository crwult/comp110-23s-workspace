def short_words(list_1: list[str]) -> list[str]:
    """removes short words from list"""
    new_list: list[str] = []
    for elem in list_1:
        if len(elem) < 5:
            new_list.append(elem)
        else:
            print(f"{elem} is too long!")
    return new_list

my_list : list [str ] = ["sun", "cloud", "sky"]
print(short_words ( my_list ))
