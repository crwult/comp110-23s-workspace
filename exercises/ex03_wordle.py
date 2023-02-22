

def contains_char(guess: str, character: str) -> bool:
    """Checks if the character is in the string."""
    assert len(character) == 1
    yellow_i = 0
    yellow = False
    while yellow_i < len(guess):
        if guess[i] == SECRET[yellow_i]:
            yellow = True
        yellow_i = yellow_i + 1
    return yellow
print(contains_char("abc","b"))