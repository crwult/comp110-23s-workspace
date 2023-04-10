"""Wordle on repeat: Practice with Function."""
__author__ = "730552290"

def main() -> None:
    """The entrypoint of the program and main game loop."""
    win: bool = False
    guess_number: int = 1
    SECRET_WORD = "codes"
    while (win == False) and (guess_number <= 6):
        print (f"=== Turn {guess_number}/6 ===")
        correct_guess = input_guess(len(SECRET_WORD))
        print(emojified(correct_guess, SECRET_WORD))
        if correct_guess == SECRET_WORD:
            win = True
            print(f"You won in {guess_number}/6 turns")
        guess_number += 1
    if guess_number == 7:
        print("X/6 - Sorry, try again tomorrow!")


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
        emoji_i += 1
    return(boxes)

def input_guess(SECRET_length: int) -> str:
    """When a number is put it, it puts out inputs with the same amount of characters"""
    correct_length = False
    initial_input = str(input(f"Enter a {SECRET_length} character word: "))
    if len(initial_input) == SECRET_length:
        correct_length = True
    while correct_length == False:
        initial_input = str(input(f"That wasn't {SECRET_length} chars! Try agian: "))
        if len(initial_input) == SECRET_length:
            correct_length = True
    return(initial_input)

if __name__ == "__main__":
    main()