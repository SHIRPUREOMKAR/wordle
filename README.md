
# Wordle-Solver


## Run Locally

Clone the project

```bash
  git clone https://github.com/SHIRPUREOMKAR/wordle_solver.git
```

## wordle-game.py
 This file contains a fully functional wordle game. Run:
 ```bash
 python ./wordle_game.py
 ```
- #### Usage
 Just enter the `guess_word` and it returns the color code for the given wordle word.
 
- It also contains a function `remote_game_engine()`

 such that, for eg:
 ```python
 remote_game_engine(original_word, guess_word):
    ...
    ...
    return [0, 2, 1, 0, 1]
 ```
  for the use in `auto_player()` function of `wordle_solver.py` for `n` random cases

## wordle_solver.py
> **_NOTE:_**  This may **sometimes** produce *late / inaccurate* results, since recalculates the previous top choices list and doesn't consider new unique choices.

This file contains the wordle solver. Run: 

```bash
python ./wordle_solver.py
```


 - #### Usage
 It outputs the top word choices *(default = 10)* along with the scores *(the minimum the better)*.
 Just enter the `guess_word` and the `code / pattern` you received

for eg:
```
Enter the guess_word: clown
Enter the received pattern: bggyb
```
where, `b - black/grey`, `g - green`, `y - yellow`

and it gives the updated top guesses based on the info received.
