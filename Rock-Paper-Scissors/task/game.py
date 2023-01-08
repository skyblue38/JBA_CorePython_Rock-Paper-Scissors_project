# JBA Core Python course
# Rock-Paper-Scissors project - https://hyperskill.org/projects/78
# Submitted by Chris Freeman  - 3 of 5 - 08JAN2023

import random


winning_move = {}
move_list = []
default_moves = ['rock', 'paper', 'scissors']
user_d = {}         # dictionary of user scores

your_name, *filler = input('Enter your name: ').split()   # get user's name(s)
print(f'Hello, {your_name}')    # Greet user by name by first name
while True:                     # get game moves
    move_line = input()         # filter the list of moves
    if move_line == '':
        move_list = default_moves   # blank means default
        break
    move_list = move_line.strip().lower().split(',')
    if len(move_list)//2:       # move_list must be odd length
        break
# Build dictionary of winning moves
# each key has a list of values that will defeat it
# so if the cpu guess is in this list, you lose...
maxx = len(move_list)
span = maxx//2
for n in range(len(move_list)):
    for p in range(span):
        winning_move.setdefault(move_list[n], []).append(move_list[(n + p + 1) % maxx])
# Read the user ratings from file
try:
    with open('rating.txt', 'r', encoding='utf-8') as file:
        for line in file:                   # read next line
            name, score, *filler = line.strip().split()  # remove spaces and newline
            user_d[name] = int(score)       # save the name with score
except Exception as e:
    print('Error reading user ratings file:', e)    # Oops! Something broke...
your_score = user_d.setdefault(your_name, 0)    # get user score and set zero as default
print("Okay, let's start")
while True:
    while True:                                 # get your move
        your_move = input().lower()
        if your_move == '!exit' or your_move == '!rating' or your_move in move_list:
            break                               # move on if valid...
        print('Invalid input')
    if your_move == '!exit':                    # proceed to exit...
        break
    if your_move == '!rating':                  # show current score
        print(f'Your rating: {your_score}')
        continue
    cpu_move = random.choice(move_list)         # get a random computer move
    if your_move == cpu_move:                               # draw
        your_score += 50
        print(f'There is a draw ({cpu_move})')
    elif cpu_move in winning_move[your_move]:               # cpu win
        print(f'Sorry, but the computer chose {cpu_move}')
    elif your_move in winning_move[cpu_move]:               # you win
        your_score += 100
        print(f'Well done. The computer chose {cpu_move} and failed')
    else:
        print('Undecided!')         # What?? should not get here...
user_d[your_name] = your_score      # update user score dictionary
# ...here is where we could save the scores dictionary to a file...
print('Bye!')
