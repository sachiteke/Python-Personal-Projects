from colorama import Fore
from words import choose_words
import re

username = ''

def name():     #get name of user
    global username
    print(Fore.RED + "\nNote for old users: \nIf you're replaying and don't want to change your name, type `REPLAY`.\n")
    user = input(Fore.WHITE + "Enter a username: ")
    u = user.lower()
    if u!='replay':
        username = user

def number_of_level():      #get number of levels the user would like to play
    while True:
        try:
            levels = int(input(Fore.WHITE + "\nHow many levels [3 or 4]?: "))
            if levels==3 or levels==4:
                return levels
        except:
            print("Enter an integer vale")

def guessing(hardness, chances):     #guessing word process
    word = choose_words(hardness)    
    print(Fore.BLUE + "\n{} LEVEL\n".format(hardness.upper()))
    word = word.upper()
    res = ["_" for i in range(len(word))]

    for i in ['A','E','I','O','U',' ']:
        vowel = [j.start() for j in re.finditer(r'{}'.format(re.escape(i)), word)]
        for k in vowel:
            res[k] = i

    print(Fore.YELLOW,*res,"\n")
    #print(word)

    i=1
    while i<chances+1:
        letter = input("Guess {}: ".format(i)).upper()
        while len(letter) != 1: 
            print(Fore.RED + "\nEnter one character at a time!")
            letter = input(Fore.YELLOW + "Guess {}: ".format(i)).upper()
        ind = [i.start() for i in re.finditer(r'{}'.format(re.escape(letter)), word)]
        for j in ind:
            res[j] = letter
        if '_' not in res:
            print(Fore.GREEN + "\nYou guessed it correctly! It is {}\n".format(word))
            break
        if letter not in word:
            i = i+1
        print(Fore.YELLOW,*res,"\n")

    if '_' in res:
        print(Fore.RED + "The word was {}".format(word))
        print("Better luck this time... restarting this level.")
        guessing(hardness, chances)
    return

def start_game(N):      #instructions and general information
    if N==3:
        print(Fore.GREEN + "\n\nLength of words for each level will be-\nLevel 1: 4-5\nLevel 2: 6-7\nLevel 3: 8-9\n")    
        print("No. of chances for each level are\nEasy: 5\nMedium: 7\nHard: 10\n\n")
    else:
        print(Fore.GREEN + "\n\nLength of words for each level will be-\nLevel 1: 4-5\nLevel 2: 6-7\nLevel 3: 8-9\nLevel 4: 10+\n")    
        print("No. of chances for each level are\nEasy: 5\nMedium: 7\nHard: 10\nExtreme: 15\n\n")
    print(Fore.WHITE + "Game is starting....\n\n")
    guessing('easy', 5)
    guessing('medium', 7)
    guessing('hard', 10)
    if N==4:
        guessing('extreme', 15)
    return

if __name__ == '__main__':
    while True:
        name()
        print(Fore.CYAN + "\n\nHello {}! Ready for the game? Just loading!".format(username))
        levels = number_of_level()
        start_game(levels)
        exiting = input(Fore.WHITE + '\nWant another around?[y/n]: ').lower()
        if exiting == 'n' or exiting == 'no':
            break
    print(Fore.CYAN + '\nExited\n')