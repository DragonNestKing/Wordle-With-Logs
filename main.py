"""
Wordle project with a signup/login feature
"""
import random as r
import sys
from colorama import Fore, Back, Style

def menu():
    print("Let's play Wordle:\nType a 5 letter word and hit enter!")

def read_random_word():
    with open("words.txt") as w:
        words = w.read().splitlines()
        return r.choice(words)

menu()
word = "fives"
# need to fix this cause tutorial is strange and allows user to enter too big or too small words
for attempt in range(1, 7):
    guess = input().lower()

    for i in range( min(len(guess), 5) ):
        if guess[i] == word[i]:
            print(Fore.GREEN + guess[i], end = "")
        elif guess[i] in word:
            print(Fore.YELLOW + guess[i], end = "")
        else:
            print(Fore.BLACK + guess[i], end = "")
    