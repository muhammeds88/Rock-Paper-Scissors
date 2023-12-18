import random

user_wins = 0
computer_wins = 0
tie = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Type Rock / Paper / Scissors OR  Q to Quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # 0 = rock , 1 = paper, 2 = scissors.
    computer_pick = options[random_number]
    print('computer_picked', computer_pick + '.')
    if user_input == computer_pick:
        print('That is a tie.')
        tie += 1
        continue
    if user_input == 'rock' and computer_pick == 'scissors':
        print('You Won!')
        user_wins += 1
        continue
    if user_input == 'paper' and computer_pick == 'rock':
        print('You Won!')
        user_wins += 1
        continue
    if user_input == 'scissors' and computer_pick == 'paper':
        print('You Won!')
        user_wins += 1
        continue
    else:
        print('You lost.')
        computer_wins += 1

print('You Won ',user_wins ,'times.')
print('The computer won ',computer_wins ,'times.')
print('There is ',tie ,'tie')
print('Good Bye!')