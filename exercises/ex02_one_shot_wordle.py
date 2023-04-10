"""Ex 02: One shot wordle."""
__author__ = "730552290"

SECRET: str = "python"
number_of_letters: int = len(SECRET)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
boxes = ""
i: int = 0

guess = str(input(f"What is your {number_of_letters}-letter guess? "))
while len(guess) != number_of_letters:
    guess = str(input(f"That was not {number_of_letters} letters! Try again: "))

while i < number_of_letters:
    if SECRET[i] == guess[i]:
        boxes = boxes + GREEN_BOX
    else:
        yellow_i = 0
        yellow = False
        while yellow_i < number_of_letters:
            if guess[i] == SECRET[yellow_i]:
                yellow = True
            yellow_i = yellow_i + 1
        if yellow is True:
            boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
    i = i + 1
print(boxes)
if guess == SECRET:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")