"""
Wordle project with a signup/login feature
"""
import random as r
import sys
import os
from colorama import Fore, Back, Style

not_logged = True

def menu():
    if not_logged:
        while True:
            ans = input("Would you like to log in to score your data? [y]es or [n]o?:  ")
            if ans[0].lower() == "y":
                print("works")
                break
            elif ans[0].lower() == "n":
                print("also works")
                break
            else:
                print("please enter yes or no")
    
    print("Let's play Wordle:\nType a 5 letter word and hit enter!\n")

def read_random_word():
    with open("words.txt") as w:
        words = w.read().splitlines()
        return r.choice(words)

def on_entered_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

play_again = ""
streak = 0

while play_again != "q":

    os.system('clear')
    menu()
    word = "files"
    guess_list = []

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
        guess_list.append(guess)
    
        print()
        if guess == word:
            print(Style.RESET_ALL + Fore.GREEN + "Congrats! You got the wordle in " + str(attempt) + " attempt(s)!")
            streak = streak + 1
            
            break
            
    if guess != word:
        print(Style.RESET_ALL + Fore.RED + "So sorry, you didn't get the word...\n\nThe word was " + word)
        streak = 0

    data = [guess_list, word, streak]
        
    play_again = input(Style.RESET_ALL + "\nenter q if you would like to quit, press enter to play again")
