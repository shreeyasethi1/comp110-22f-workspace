"""EX02 - One-shot Wordle."""

__author__ = "730553668"

secret_word: str = "python" 
guess: str = input(f"What is your {len(secret_word)} letter guess?")
#is the guessed word the correct number of characters
while len(guess) != len(secret_word): 
    guess = input(f"That is not {len(secret_word)} letters! Try again: ")
# variables definition used in the while loop
index = 0 
emoji = ""
green = "\U0001F7E9"
yellow = "\U0001F7E8"
white = "\U00002B1C" 
# green, yellow, white emoji 
while index < len(secret_word):
    match_character = False
    secret_index = 0 
    # if the character in guess and secret_word in the same index is the same, printing green block 
    # else going into a while loop to find out if the guess character matches the character of the secret_word on a different index
    # if neither, printing the white block 
    if guess[index] == secret_word[index]:
        emoji += green
    else:
        while match_character == False and secret_index < len(secret_word):
            if secret_word[secret_index] == guess[index]:
                match_character = True
            else:
                secret_index += 1

        if match_character == True:
            emoji += yellow
        else:
            emoji += white
    
    index += 1 

print(emoji)

if guess != secret_word:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")             
