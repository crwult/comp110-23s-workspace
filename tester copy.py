def mimic_letter(my_words:str,letter_idx:int)->str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx <= len(my_words)-1:
        return(my_words[letter_idx])
    return("Too high of an index")

print(mimic_letter("hello world",40))