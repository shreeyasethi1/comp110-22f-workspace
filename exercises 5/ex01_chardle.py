"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730553668"

word: str = input("Enter a 5-character word: ")
length_word = len(word) 
if length_word < 5: 
    print("Error: Word must contain 5 characters")
    exit()
if length_word > 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")
length_character = len(character)
if length_character != 1: 
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + word)

count = 0 
if character == word[0]:
    print(character + " found at index 0")
    count += 1
if character == word[1]: 
    print(character + " found at index 1")
    count += 1
if character == word[2]:
    print(character + " found at index 2")
    count += 1
if character == word[3]:
    print(character + " found at index 3")
    count += 1
if character == word[4]:
    print(character + " found at index 4")
    count += 1

if count == 0: 
    print("No instances of " + character + " found in " + word)
if count == 1:
    print(count, "instance of " + character + " found in " + word)
if count > 1:
    print(count, "instances of " + character + " found in " + word)