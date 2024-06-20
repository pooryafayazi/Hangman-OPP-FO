# Hangman OOP
import random

class Hangman:
    def __init__(self):
        self.word_list = ["python", "hangman", "program", "computer", "coding"]
        self.word = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6
    
    def choose_word(self):
        return random.choice(self.word_list)
    
    def display_word(self):
        displayed_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return f"\nYour currently guess is : {displayed_word.strip()}"
    
    def play(self):
        print("Welcome to Hangman!")
        print(self.display_word())
        
        while True:
            guess = input("Guess a letter: ").lower()
            if guess in self.guessed_letters:
                print("You already guessed that letter!")
                continue
            self.guessed_letters.append(guess)
            
            if guess not in self.word:
                self.attempts -= 1
                print(f"Incorrect! You have {self.attempts} attempts left.")
                if self.attempts == 0:
                    print("You ran out of attempts! The word was:", self.word)
                    break
            else:
                print("Correct!")
            
            displayed_word = self.display_word()
            print(displayed_word)
            
            if "_" not in displayed_word:
                print("\nCongratulations! You guessed the word :  ", self.word.upper().replace("", " ")[1: -1],"\n\n\n")
                break

game = Hangman()
game.play()
