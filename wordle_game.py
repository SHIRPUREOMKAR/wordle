import random
import os
import subprocess

def remote_game_engine(original, test):
    sol = []
    yellows = []
    greens = []
    test_print = []
    original_print = []
    for j in range(5):
        test_print.append(test[j])
        original_print.append(original[j])
    for j in range(5):
        if test_print[j] == original_print[j]:
            greens.append(j)
            original_print[j] = 0
    for j in range(5):
        if test_print[j] in original_print:
            index = original_print.index(test_print[j])
            original_print[index] = 0
            yellows.append(j)
    for j in range(5):
        if j in greens:
            sol.append(2)
        elif j in yellows:
            sol.append(1)
        else:
            sol.append(0)
    return sol

def engine():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
    red = "\033[31m"
    green = "\033[42m"
    yellow = "\033[43m"
    reset = "\033[0m"
    game_finished = False
    chances = 0

    word_list = []
    with open('dtb/valid_solutions.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            word_list.append(line[0:5])
        f.close()

    word = random.choice(word_list)
    while chances < 6:
        sol = []
        greens = []
        yellows = []
        finished = 0

        test = input(f'Enter your {chances + 1}th guess: ')
        if(len(test) != 5):
            print(f'{red}Invalid word length..!!{reset}')
            continue
        test_print = []
        print()
        for char in test:
            test_print.append(char)
        word_print = []
        for char in word:
            word_print.append(char)

        for j in range(5):
            if test_print[j] == word_print[j]:
                greens.append(j)
                word_print[j] = 0
        for j in range(5):
            if test_print[j] in word_print:
                index = word_print.index(test_print[j])
                word_print[index] = 0
                yellows.append(j)
                
        for j in range(5):
            if j in greens:
                print(f'{green}{test[j]}{reset}', end='')
                sol.append(2)
                finished += 1
            elif j in yellows:
                print(f'{yellow}{test[j]}{reset}', end='')
                sol.append(1)
            else:
                print(f'{test[j]}', end = '')
                sol.append(0)
        print()
        print()
        
        if finished == 5:
            print(f'{green}You won..!!!{reset}')
            game_finished = True
            break
        chances += 1

    if not game_finished:
        print()
        print(f'{red}You lose!! The word was "{word}"{reset}')
        
if __name__ == '__main__':
    engine()
