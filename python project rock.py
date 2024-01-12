import random

# Initialize variables to keep track of user and computer wins, and ties
user_wins = 0
computer_wins = 0
tie = 0

# Define the available options for the game
options = ['rock', 'paper', 'scissors']

# Main game loop
while True:
    # Get user input for rock, paper, or scissors, and allow quitting with 'q'
    user_input = input('Type Rock / Paper / Scissors OR Q to Quit: ').lower()
    
    # Check if the user wants to quit
    if user_input == 'q':
        break

    # Check if the user input is a valid option, otherwise, prompt for input again
    if user_input not in options:
        continue

    # Generate a random number to represent the computer's choice
    random_number = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2 = scissors.
    computer_pick = options[random_number]
    print('Computer picked', computer_pick + '.')

    # Compare user input with computer's choice and determine the winner
    if user_input == computer_pick:
        print('That is a tie.')
        tie += 1
        continue
    elif (user_input == 'rock' and computer_pick == 'scissors') or \
         (user_input == 'paper' and computer_pick == 'rock') or \
         (user_input == 'scissors' and computer_pick == 'paper'):
        print('You Won!')
        user_wins += 1
    else:
        print('You lost.')
        computer_wins += 1

# Display final results after the game ends
print('You Won', user_wins, 'times.')
print('The computer won', computer_wins, 'times.')
print('There were', tie, 'ties.')
print('Goodbye!')
