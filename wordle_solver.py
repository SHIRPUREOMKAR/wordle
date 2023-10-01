import random
import os
import subprocess
import wordle_game

red = "\033[31m"
green = "\033[32m"
greenbg = "\033[42m"
yellow = "\033[33m"
reset = "\033[0m"

words_list = []
with open('dtb/valid_solutions.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        words_list.append(line[0:5])
    f.close()

def filter_words(guess_word, result, words_list):
    okay_letters_dict = []
    nono_letters_list = []
    kinda_okay_letters_list = []
    filter1 = []
    filter2 = []
    filter3 = []
    okay_nono_pos = {}
    okay_kinda_pos = []

    for i in range(5):
        if result[i] == 2:
            okay_letters_dict.append((guess_word[i], i))
        if result[i] == 1:
            kinda_okay_letters_list.append(guess_word[i])
        if result[i] == 0:
            nono_letters_list.append(guess_word[i])

    for i in okay_letters_dict:
        for nonos in nono_letters_list:
            if i[0] == nonos:
                okay_nono_pos[i[0]] = i[1]
        if i[0] in kinda_okay_letters_list:
            okay_kinda_pos.append((i[0], i[1]))

    for word in words_list:
        check = 1
        for i in okay_letters_dict:
            if not i[0] == word[i[1]]:
                check = 0
        if check:
            filter1.append(word)

    for word in filter1:
        check = 1
        for i in range(5):
            if word[i] in nono_letters_list:
                if word[i] in kinda_okay_letters_list:
                    continue
                if word[i] in okay_nono_pos.keys():
                    if i == okay_nono_pos[word[i]]:
                        pass
                    else:
                        check = 0
                else:
                    check = 0
        if check:
            filter2.append(word)

    if not len(kinda_okay_letters_list) == 0:
        for word in filter2:
            temp = []
            for i in range(5):
                if all(i != tup[1] for tup in okay_kinda_pos):
                    temp.append(word[i])
            for k in temp:
                if k in kinda_okay_letters_list:
                    filter3.append(word)
                    break
    else:
        filter3 = filter2
    return filter3

def letter_frequency(possible_words):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    arr = {}
    for c in alphabet:
        freq = [0, 0, 0, 0, 0]
        for i in range(0, 5):
            for w in possible_words:
                if w[i] == c:
                    freq[i] += 1
        arr.update({c: freq})
    return arr

def scores_list(possible_words, frequencies):
    words = []
    max_freq = [0, 0, 0, 0, 0]
    for c in frequencies:
        for i in range(0, 5):
            if max_freq[i] < frequencies[c][i]:
                max_freq[i] = frequencies[c][i]
    total = 0
    for w in possible_words:
        score = 1
        for i in range(0, 5):
            c = w[i]
            score *= 1 + (frequencies[c][i] - max_freq[i]) ** 2
        score /= 1e3
        total += score
        words.append((w, score))
    best_scores = sorted(words, key=lambda x: x[1])
    return best_scores, total

def auto_player(n, isRandom):
    score = 0
    for i in range(n):
        words_list = []
        with open('dtb/valid_solutions.csv', 'r') as f:
            lines = f.readlines()
            for line in lines:
                words_list.append(line[0:5])
            f.close()
        # subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
        if isRandom:
            word = random.choice(words_list)
        else:
            word = words_list[i]
        print(f'Running tests for {i + 1} / {n} cases for "{word}": ')

        game_completed = False
        counter = 0
        already_guessed = []
        while counter < 6 and not game_completed:
            guesses = scores_list(words_list, letter_frequency(words_list))
            if not guesses or not guesses[0]:
                break
            guess = guesses[0][0][0]
            while guess in already_guessed:
                guesses[0].pop(0)
                if not guesses[0]:
                    break
                guess = guesses[0][0][0]
            if not guesses[0]:
                break
            
            already_guessed.append(guess)
            if len(guess) != 5:
                break
            result = wordle_game.game(word, guess)
            if result == [2, 2, 2, 2, 2]:
                print(f'{green}{guess}{reset}')
                game_completed = True
                break
            print(guess)
            words_list = filter_words(guess, result, words_list)
            counter += 1
        score += counter

    print(f'Average score: {score / (n + 1)}')
        
def display_recos(words_list):
    print(f'\nRecommended words: ')
    reco_words, total = scores_list(words_list, letter_frequency(words_list))
    for word, score in reco_words[:10]:
        print(f'\t{word} - {score / 1e5}')
    print(f'Best choice: {greenbg}{reco_words[0][0]}{reset}\n')

def game_engine_manual(words_list):
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
    game_completed = False
    counter = 0
    print(f'eg: Input guess as: snail')
    print(f'eg: Input received pattern as: byggb')
    print(f'where: y - {yellow}yellow{reset}, g - {green}green{reset}, b - black/grey.')
    display_recos(words_list)
    while counter < 6 and not game_completed:
        guess = input("Enter your guess: ")
        if len(guess) != 5:
            print(f'{yellow}Invalid length!!{reset}')
            continue
        result = []
        pattern = input("Enter received pattern: ")
        if pattern == "ggggg":
            game_completed = True
            print(f'\n{green}You guessed it in the {counter + 1}th attempt..!!!{reset}')
            return
        sum = 0
        for i in pattern:
            if i == 'b':
                result.append(0)
                sum += 1
            elif i== 'y':
                result.append(1)
                sum += 1
            elif i == 'g':
                result.append(2)
                sum += 1

        if sum != 5:
            print(f'{red}Enter correct pattern{reset}')
            continue
        words_list = filter_words(guess, result, words_list)
        display_recos(words_list)

        counter += 1

if __name__ == "__main__":
    # game_engine_manual(words_list)
    auto_player(100, 1)