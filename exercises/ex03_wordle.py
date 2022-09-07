"""EX 3 Structured Wordle."""

__author__: str = "730575704"


def contains_char(secret_word: str, guess_char: str) -> bool:
    """To search for guess_char in any indices of secret_word."""
    assert len(guess_char) == 1  # Ensure one char parameter passed
    i: int = 0  # Loop index
    while i < len(secret_word):
        if secret_word[i] == guess_char:  # Comparing guess char to secret word chars
            return True
        i += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Assembles emoji string based on guess accuracy."""
    assert len(guess_word) == len(secret_word)  # Ensuring guess word was correct length
    WHITE_BOX: str = "\U00002B1C"  # Establish emoji boxes
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_string: str = ""
    wi: int = 0  # word index
    while wi < len(secret_word):  # Loop to check for character accuracy
        if guess_word[wi] == secret_word[wi]:
            emoji_string = emoji_string + GREEN_BOX
        elif contains_char(secret_word, guess_word[wi]):  # Draws on contains_char to check for yellow boxes
            emoji_string = emoji_string + YELLOW_BOX 
        else:
            emoji_string = emoji_string + WHITE_BOX 
        wi += 1
    return emoji_string


def input_guess(exp_length: int) -> str:
    """Ask for user guess and ensure it is the correct length."""
    guess: str = input(f"Enter a {exp_length} character word: ")  # Inputs guess
    while len(guess) != exp_length:
        guess = input(f"That wasn't {exp_length} chars! Try again: ")  # Loop to ensure guess length
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"  # Secret word established
    turn: int = 1  # Turn counter variable
    win_condition: bool = False  # True if game won
    while turn <= 6 and not win_condition:  # While loop to run the game using guess and emoji functions
        print(f"=== Turn {turn}/6 ===")
        guessed: str = input_guess(len(SECRET))
        print(emojified(guessed, SECRET))
        if guessed == SECRET:
            win_condition = True
            turn -= 1  # Turn added at end of while loop, corrects win output
        turn += 1
    
    if win_condition:
        return print(f"You won in {turn}/6 turns!")  # Win message
    else:
        return print("X/6 - Sorry, try again tomorrow!") # Lose message


if __name__ == "__main__":
    main()