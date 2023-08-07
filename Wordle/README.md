# Wordle Game

## Introduction
Wordle is a simple word-guessing game. The game prompts the player to guess a word of a specified length. The player has a limited number of attempts to guess the word correctly. The game provides feedback on each guess to help the player narrow down the correct answer.

## Prerequisites
- Python 3.8 or above
- Random module (included in Python standard library)

## How to Play
1. Open the terminal or command prompt.
2. Navigate to the directory where the game script is located.
3. Run the script using the Python interpreter: `python wordle.py <word_length>`
    
    - Replace `<word_length>` with an integer value between 5 and 8 (inclusive). This specifies the length of the word to be guessed.

4. The game will start and prompt you to enter a word of the specified length.
5. Enter your guess and press Enter.
6. The game will provide feedback on each guess and prompt you to make another guess.
7. Keep guessing until you either guess the word correctly or run out of attempts.
8. The game will announce whether you won or lost, and show the number of attempts made.

## Code Explained
The code is a simple game called "Wordle". Here's a breakdown of what it does:

1. It imports the <span style=\"color: yellow;\">", sys, "</span> module and the choice function from the random module.
2. It defines two helper functions: clear_last_line and print_with_background_color.

    - clear_last_line clears the last line in the command line interface.
    - print_with_background_color prints a text with a specified background color in the command line interface.
3. It defines a function get_guess that prompts the user to enter a word of a specified length and returns the user's input.
4. It defines a function check_guess that takes a guess, the target word, a status list, and the mode as inputs. It checks the guess against the target word and updates the status list accordingly. It also calculates the score and returns the updated status list and the score.
5. It defines a function print_word that takes a guess, a status list, and the mode as inputs. It prints the guess in a colored format based on the status of each letter of the guess.
6. It defines the main logic of the game in the function game. It reads a file containing a list of words of a specified length, chooses a random word from the list, and initializes the number of guesses allowed. It then enters a loop where the user can make guesses. For each guess, it calls the get_guess function, checks the guess using the check_guess function, and prints the guess using the print_word function. If the user guesses the word correctly, the loop breaks and the function returns True as the result along with the number of attempts and the actual word. Otherwise, it returns False as the result along with the number of attempts and the actual word.
7. It defines a function show_results that takes the game result (True or False), the number of attempts, and the actual word as inputs. It prints a message announcing whether the player won or lost and the corresponding information.
8. It defines the main program logic in the main function. It checks if there is a command line argument. If there is, it checks if it is a valid integer between 5 and 8 (inclusive). If it is, it calls the game function with the specified mode and shows the results using the show_results function. If it is not a valid integer or not in the desired range, it prints an error message. If there is no command line argument or the number of arguments is not valid, it also prints an error message.
9. Finally, it calls the main function if the script is run as the main module.
