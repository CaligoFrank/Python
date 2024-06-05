import requests
import random


def print_board(tries):
    hangman_parts = [
    """
        +---+
        |   |
            |
            |
            |
            |
    =========
    """,
    """
        +---+
        |   |
        O   |
            |
            |
            |
    =========
    """,
    """
        +---+
        |   |
        O   |
        |   |
            |
            |
    =========
    """,
    """
        +---+
        |   |
        O   |
        /|  |
            |
            |
    =========
    """,
    """
        +---+
        |   |
        O   |
        /|\ |
            |
            |
    =========
    """,
    """
        +---+
        |   |
        O   |
        /|\  |
        /    |
            |
    =========
    """,
    """
        +---+
        |   |
        O   |
        /|\ |
        / \ |
            |
    =========
    """
    ]
    
    return hangman_parts[tries]





url = 'https://random-word-api.herokuapp.com/word'
word = requests.get(url)
word_text = word.text
tries = 0

empty_guess = ''
print(word_text)
#while tries != 6:
   
print(print_board(tries))
for letter in word_text:
    empty_guess += '_'
print(empty_guess)




user_guess = input("Enter your guess:\n")

for index, letter in word_text[0]:
    if letter == ltter in user_guess:
        empty_guess[index] = ltter

# if user_guess != word_text:
#     print("Try again!")
#     tries += 1
          
        
    
    
    

        
    






