"""
Wordle project with a signup/login feature


"""

# Imports all required libraries for the code to function
import random as r
from time import sleep
import sys
import os
from colorama import Fore, Back, Style

not_logged = True


# Checks if the user's Username and Password are in the masterfile
def login(divided_file):
    
    while True:
        
        usern = input("Please enter your username:  ")
        passw = input("Please enter your password:  ")
        for i in range(len(divided_file)):

            if usern == divided_file[i][0] and passw == divided_file[i][1]:
                
                print("User found")
                sleep(2)
                os.system("clear")
                return i
        print("\nPlease try again after making sure you're typing the right account information\n")
        sleep(3)
        os.system("clear")


#Adds the account information into the masterfile that allows the user to login
def register():
    os.sys("clear")
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

# Creates the menu that the player sees at the start of every game    
def menu():
    global not_logged, account_num
            
    if not_logged:
        
        while True:
            with open("masterfile.txt", "r") as mf:
                divided_file = mf.read().split('\n')
        
                for i in range(len(divided_file)):
                    divided_file[i] = str(divided_file[i]).split(', ')
                    
            ans = input("Would you like to log in to score your data? [y]es, [n]o?, or do you need to [s]ign up:  ")
            
            if ans[0].lower() == "y":
                os.system("clear")
                account_num = login(divided_file)
                not_logged = False
                os.system("clear")
                print("Let's play Wordle:\nType a 5 letter word and hit enter!\n")
                return account_num + 1
                
            elif ans[0].lower() == "s":
                register()
                print("Thank you for registering with us!\n\n")
                sleep(3)
                continue
                
            elif ans[0].lower() == "n":
                os.system("clear")
                break
                
            else:
                print("please enter yes or no")
    
    print("Let's play Wordle:\nType a 5 letter word and hit enter!\n")
    return

# Sets a random word from the words file
def read_random_word():
    
    with open("words.txt") as w:
        words = w.read().splitlines()
        
        return r.choice(words)

# Uses system codes to make the code write on the previous line that was written, allows for the colors to appear on the text.
def on_entered_line():
    
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

play_again = ""
streak = 0

# The running loop that allows the game to play
while play_again != "q":
    
    account_num = menu()
    word = read_random_word()
    guess_list = []

    for attempt in range(1, 7):
        
        file = open("words.txt")
        data = file.read()
        
        while True:
            
            guess = input(Style.RESET_ALL).lower()
            on_entered_line()
            
            if guess in data and len(guess) == 5:
                break

            elif len(guess) != 5:
                print("Please type a 5 letter word.")
                
            else: 
                print("Sorry! we don't have that word...")

                
        for i in range( min(len(guess), 5)):
                    
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

    print("\n You currently have a streak of " + str(streak) + ". Continue playing to get a higher streak!\n")
    
    play_again = input(Style.RESET_ALL + "\nenter q if you would like to quit, press enter to play again")
    
    os.system("clear")