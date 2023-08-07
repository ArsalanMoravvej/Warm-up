import sys
from random import choice


def print_with_background_color(text, background_color, new_line = False):
    colors = {
        'black': '\033[40m',
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[94m',
        'magenta': '\033[45m',
        'cyan': '\033[46m',
        'white': '\033[47m'
    }
    reset = '\033[0m'
    sys.stdout.write(colors[background_color] + text + reset)
    sys.stdout.flush()
    if new_line:
        print("\n", end="")


def get_guess(mode):
    guess = ""
    while len(guess) != mode:
        guess = input(f"Input a {mode}-letter word: ")
    return guess

def check_guess(guess, word, status, mode):
    score = 0
    for i in range(mode):
        for j in range(mode):
            if guess[i] == word[i]:
                status[i] = 2
                break
            elif guess[i] == word[j]:
                status[i] = 1
        score += status[i]
    return status, score

def print_word():
    pass

def game(mode):

    file_path = f"files/{mode}.txt"
    with open(file_path, "r") as file:
        contents = file.read()

    word = choice(contents.split("\n"))
    print(word)

    guesses = mode + 1
    won = False

    print_with_background_color("This is WORDLE!", 'cyan', new_line=True)
    print_with_background_color(f"You have {guesses} tries to guess the {mode}-letter word", 'magenta', new_line=True)

    for i in range(guesses):
        guess = get_guess(mode)
        status = [0 for _ in range(mode)]
        status, score = check_guess(guess, word, status, mode)
        print(f"Guess {i+1} = ", end="")
        print_word()







try:

    initiate = int(sys.argv[1])
except:

    print_with_background_color("Invalid entry!", 'red', new_line=True)
    print_with_background_color("Usage: ./wordle.py [wordsize]", 'blue', new_line=True)
else:

    if 8 >= initiate >= 5:
        game(initiate)
    else:
        print_with_background_color("Invalid entry!", 'red', new_line=True)
        print_with_background_color("Error: wordsize must be either 5, 6, 7, or 8", 'blue', new_line=True)