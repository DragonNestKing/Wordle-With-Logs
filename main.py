"""
Wordle project with a signup/login feature
"""
import random as r
import sys
import os
from colorama import Fore, Back, Style

def menu():
    print("Let's play Wordle:\nType a 5 letter word and hit enter!\n")

def read_random_word():
    with open("words.txt") as w:
        words = w.read().splitlines()
        return r.choice(words)

def on_entered_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

play_again = ""

while play_again != "q":

    os.system('clear')
    menu()
    word = read_random_word()

    # need to fix this cause tutorial is strange and allows user to enter too big or too small words
    for attempt in range(1, 7):
        file = open("words.txt")
        data = file.read()
        while True:
            guess = input(Style.RESET_ALL).lower()
            on_entered_line()
            
            if guess in data:
                break
            else: 
                print("Sorry! we don't have that word...")
    
        for i in range( min(len(guess), 5) ):
            if guess[i] == word[i]:
                print(Back.GREEN + guess[i], end = "")
            elif guess[i] in word:
                print(Back.YELLOW + guess[i], end = "")
            else:
                print(Back.BLACK + guess[i], end = "") 
    
        print()
        if guess == word:
            print(Style.RESET_ALL + "Congrats! You got the wordle in " + str(attempt) + " attempt(s)!")
            
            break
            
    if guess != word:
        print(Style.RESET_ALL + "So sorry, you didn't get the word...\n\nThe word was " + word)
        
    play_again = input("\nenter q if you would like to quit, press enter to play again")
