# Hangman FO
import random

def choose_word():
    word_list = ["python", "hangman", "program", "computer", "coding"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return f"\nYour currently guess is : {displayed_word.strip()}"

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        guessed_letters.append(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
            if attempts == 0:
                print("You ran out of attempts! The word was:", word)
                break
        else:
            print("Correct!")
        
        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)
        
        if "_" not in displayed_word:
            print("\nCongratulations! You guessed the word :  ", word.upper().replace("", " ")[1: -1],"\n\n\n")
            break

hangman()
