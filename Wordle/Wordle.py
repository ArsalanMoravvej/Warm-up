import sys
from random import choice

#clearing the last line in commandline.
def clear_last_line():
    sys.stdout.write("\033[F")  # Move the cursor to the previous line.
    sys.stdout.write("\033[K")  # Clear the line.

#this function is tailored to print colored format strings in the commandline.
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
    
    #condition for making a new line.
    if new_line:
        print("")

# getting user guess.
def get_guess(mode):

    #ensuring that it's in valid length.
    guess = ""
    while len(guess) != mode:
        guess = input(f"Input a {mode}-letter word: ")

        #clearing the last line after the user has entered their guess.
        clear_last_line()
    return guess

# checking the user guess, calculate the score and status list items.
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

    # returning calculated status and score.
    return status, score

# printing the user guess in a colored format.
def print_word(guess, status, mode):

    for i in range(mode):

        if status[i] == 2:

            print_with_background_color(" " + guess[i] + " ", 'green')
        
        elif status[i] == 1:

            print_with_background_color(" " + guess[i] + " ", 'yellow')

        else:

            print_with_background_color(" " + guess[i] + " ", 'red')

        print(" ", end="")

    print("\n\n", end="")

# game function (called when the game is initiated.).
def game(mode):

    # openinng a (.txt) file according to the specified mode consisting of 1000 words of len(mode).
    file_path = f"files/{mode}.txt"
    with open(file_path, "r") as file:
        contents = file.read()

    # chosing a pseudorandom word within the 1000 words.
    word = choice(contents.split("\n"))

    #allowing one more guess than the length of the word.
    guesses = mode + 1

    # game result (initialy False).
    won = False

    # print greeting, using ANSI color codes to demonstrate.
    print("")
    print("")
    print("             ", end="")
    print_with_background_color("This is WORDLE!", 'cyan', new_line=True)
    print("")
    print_with_background_color(f"You have {guesses} tries to guess the {mode}-letter word", 'magenta', new_line=True)
    print("")

    # main game loop, one iteration for each guess.
    for i in range(guesses):

        #obtaining user's guess.
        guess = get_guess(mode)

        #a list to hold guess status, initially set to zero.
        status = [0 for _ in range(mode)]

        # Calculate score and status for the guess.
        status, score = check_guess(guess, word, status, mode)

        # Print the guess.
        print(f"Guess {i+1} = ", end="")
        print_word(guess, status, mode)
        
        # if they guessed it exactly right, terminate loop.
        if score == mode * 2:
            won = True
            break
    
    #returning the result, number of attempts and the actual word.
    return [won, i, word]

#showing the results.
def show_results(res, i, word):
    if res:

        # Announcement of winnig and number of attempts.
        print(f"You won!\nNumber of attempt: {i + 1}")
    else:
        # # Announcement of defeat and the actual word.
        print(f"lose :(\nThe word was {word}")

# the main program.
def main():

    # making sure that there's only one commandline argument.
    if len(sys.argv) == 2:

        try:
            # making sure that it is an integer.
            initiate = int(sys.argv[1])
        except:
            # showing error and ending the program because the entry is not an integer.
            print_with_background_color("Invalid entry! try an integer between 5 - 8.", 'red', new_line=True)
            print_with_background_color("Usage: ./wordle.py [wordsize]", 'blue', new_line=True)
        else:

            if 8 >= initiate >= 5:
                # initiating the game with the chosen mode and showing the results.
                result, attepts , word = game(initiate)
                #showing the results
                show_results(result, attepts , word)
            else:
                # showing error and ending the program because the entry is not in the desired range.
                print_with_background_color("Invalid entry!", 'red', new_line=True)
                print_with_background_color("Error: wordsize must be either 5, 6, 7, or 8", 'blue', new_line=True)
    else:
            # showing error and ending the program because the number of commandline arguments is not valid.
            print_with_background_color("Invalid number of arguments!", 'red', new_line=True)
            print_with_background_color("Usage: ./wordle.py [wordsize]", 'blue', new_line=True)



if __name__ == '__main__':
    main()