"""Wordle on repeat: Practice with Function."""
__author__ = "730552290"

def contains_char(yellow_guess: str, character: str) -> bool:
    """Checks if the character is in the string."""
    assert len(character) == 1
    yellow_i = 0
    yellow = False
    while yellow_i < len(yellow_guess):
        if character == yellow_guess[yellow_i]:
            yellow = True
        yellow_i = yellow_i + 1
    return yellow
print(contains_char("abc","a"))

def emojified(guess: str, SECRET: str) -> str:
    """Turns two stings into a string of wordle emojis."""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    boxes = ""
    assert len(guess) == len(SECRET)
    emoji_i = 0
    while emoji_i < len(guess):
        if guess[emoji_i] == SECRET[emoji_i]:
            boxes += GREEN_BOX
        else:
            if contains_char(SECRET, guess[emoji_i]):
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX
emojified("hello","olleh")

