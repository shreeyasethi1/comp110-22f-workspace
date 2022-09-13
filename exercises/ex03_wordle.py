"""Ex03-Wordle."""

__author__ = "730553668"


def contains_char(main_string: str, one_char: str) -> bool: 
    """Looking for the presence of a charcater in a longer string."""
    assert len(one_char) == 1 
    index: int = 0
    while index < len(main_string):
        if main_string[index] == one_char:
            return True 
        else: 
            index += 1 
    return False 


GREEN: str = "\U0001F7E9"
YELLOW: str = "\U0001F7E8"
WHITE: str = "\U00002B1C" 


def emojified(guess: str, secret: str) -> str:  
    """To test for the codification of a yellow or white box."""
    assert len(guess) == len(secret)
    i: int = 0 
    emoji: str = ""
    while i < len(secret): 
        if contains_char(secret, guess[i]): 
            if secret[i] == guess[i]:
                emoji += GREEN 
            else: 
                emoji += YELLOW
        else: 
            emoji += WHITE 
        i += 1
    return emoji


def input_guess(guess_expected_len: int) -> str:
    """To determine the word given matches the length expected."""
    entered_word = input("Enter a " + str(guess_expected_len) + " character word: ") 
    while len(entered_word) != guess_expected_len:
        entered_word = input("That wasn't " + str(guess_expected_len) + " chars! Try again: ")
    return entered_word   


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    while turn < 7:
        print("=== Turn " + str(turn) + "/6 " + "===")
        entered_word: str = input_guess(len(secret))
        print(emojified(entered_word, secret))
        if entered_word == secret:
            print("You won in " + str(turn) + "/6 turns!")
            return None
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()    