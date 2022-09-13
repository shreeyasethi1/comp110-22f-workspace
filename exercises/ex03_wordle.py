"""Ex03-Wordle."""

__author__ = "730553668"


def contains_char(main_string: str, one_char: str) -> bool: 
    # main_string is the string being searched through while one_char is the string being searched for. 
    """Looking for the presence of a charcater in a longer string."""
    assert len(one_char) == 1 
    index: int = 0
    while index < len(main_string):
        # checking for the one character and exiting the while loop when the main_string ends
        if main_string[index] == one_char:
            return True 
        else: 
            index += 1 
    return False 


# string code for the three color emojis
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"
white: str = "\U00002B1C" 


def emojified(guess: str, secret: str) -> str:  
    """To test for the codification of a yellow or white box."""
    assert len(guess) == len(secret)
    i: int = 0 
    emoji: str = ""
    while i < len(secret): 
        if guess[i] == secret[i]: 
            emoji += green 
        elif contains_char(secret, guess[i]): 
        # if the character is found in the word but the index isn't the same yellow box is printed
            emoji += yellow 
        else: 
            emoji += white
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
    # defining required variables 
    secret: str = "codes"
    turn: int = 0
    win: bool = False
    while turn < 6 and not win:
        turn += 1 
        print("=== Turn " + str(turn) + "/6 " + "===")
        entered_word: str = input_guess(5)
        emojis: str = emojified(entered_word, secret)
        # when the guessed word is equal to the secret word
        if entered_word == secret:
            win = True
        print(emojis)         
    
    if win: 
        print("You won in " + str(turn) + " /6 turns!")
    else: 
        print("Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()    