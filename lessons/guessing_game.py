"""Asks user for a number, goes until they get it right."""
SECRET: int = 4
guess: int = int(input("Guess a number!" ))

playing: bool = True
number_of_guesses: int = 0
while playing:
    if number_of_guesses == 3:
        playing=False
    if guess == SECRET:
        print("YAY! You got it right!")
        playing = False
    else:
        print("Wrong number :(")
        if guess%2 == 1:
            print("your guess is odd. The answer is even")
        else:
            if guess > SECRET:
                print("Your guess is too high")
            else:
                print("Your Guess is too low")
        guess= int(input("Make another guess."))
    number_of_guesses=number_of_guesses + 1