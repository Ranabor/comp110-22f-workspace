"""EX01 - One Shot Wordle."""

__author__ = "730575704"

SECRET: str = "python"  # declaring word to be guessed as a constant
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess: str = input(f"What is your {len(SECRET)} letter guess?")  # requesting guess

while len(guess) != len(SECRET):  # checking guess length
    guess = input(f"That was not {len(SECRET)} letters! Try again: ")

gi: int = 0  # guess index
word_check: str = ""  # printed string of boxes based on checks

while gi < len(SECRET):  # while loop to check guess
    if guess[gi] == SECRET[gi]:  # correct guess
        word_check = word_check + GREEN_BOX
    else:  # checking for wrong place
        wrong_place: bool = False
        wpi: int = 0  # wrong place index
        while not wrong_place and wpi < len(SECRET):  # adds yellow box if finds character
            if guess[gi] == SECRET[wpi]:
                wrong_place = True
            wpi += 1
        if wrong_place:
            word_check = word_check + YELLOW_BOX
        else:
            word_check = word_check + WHITE_BOX
    gi += 1

print(word_check)  # output

if guess == SECRET:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")