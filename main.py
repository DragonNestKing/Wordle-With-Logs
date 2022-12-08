"""
Wordle project with a signup/login feature
"""
import random as r
import sys
import os
from colorama import Fore, Back, Style

not_logged = True

def login():
    while True:
        usern = input("Please enter your username:  ")
        passw = input("Please enter your password:  ")

        with open("masterfile.txt", "r") as mf:
            


def register():
    print("Welcome to the Wordle family!")
    while True:
        while True:
            usern = input("Please enter your username:  ")
            ans = input("Are you sure you want " + usern + " to be your username? [y]es or [n]o?:  ")
    
            if ans[0].lower() == "y":
                break
            elif ans[0].lower() == "n":
                continue
            else:
                print("please enter a yes or a no.")

        while True:
            passw = input("Please enter your password:  ")
            ans = input("Are you sure you want " + passw + " to be your password? [y]es or [n]o?:  ")

            if ans[0].lower() == "y":
                break
            elif ans[0].lower() == "n":
                continue
            else:
                print("please enter a yes or a no.")

        user_list = ", ".join([usern, passw], )
        with open("masterfile.txt", "a") as mf:
            mf.write(user_list + "\n")
        os.system('clear')
        return
    
def menu():
    global not_logged
    if not_logged:
        while True:
            ans = input("Would you like to log in to score your data? [y]es, [n]o?, or do you need to [s]ign up:  ")
            if ans[0].lower() == "y":
                os.system("clear")
                while True:
                    break
                break
            elif ans[0].lower() == "s":
                register()
                print("Thank you for registering with us! Please use the login feature to login to your account.\n\n")
                break
            elif ans[0].lower() == "n":
                not_logged = False
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
    word = read_random_word()
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