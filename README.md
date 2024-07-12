# Guess The Number
This is a simple game where a random number is to be guessed either by the user or the computer.

### Game Modes
- Human Guess
    - Random Number to be guessed by human.
- Computer Guess
    - Random Number to be guessed by computer.

### How to Play
1. **Human Guess**
    - Prompts the user to enter a `lower range` and `upper range`.
    - Generates a random number between `lower range` and `upper range`.
    - Prompts the user to guess the number.
    - If guess is lower than random number:
        - If guess is close to the random number, displays `Close!, Guess a little higher`, else displays `Your guess is too low`.
    - If guess is higher than random number`:
        - If guess is close to the random number, displays `Close! Guess a little lower`, else displays `Your guess is too high`.
    - If guess is correct, displays `Congratulations! You guessed the number in x tries`.
2. **Computer Guess**
    - Prompts the user to enter a `lower range` and `upper range`.
    - Prompts the user to enter a `number` to be guessed by the computer.
    - Computer generates a random number between `lower range` and `upper range`.
    - Prompts the user to give feedback on the guess.
        - If guess is too low than the number, enter `l`.
        - If guess is too high than the number, enter `h`.
        - If guess is correct, enter `c` and displays `Congratulations! Computer guessed the number in x tries`.

3. After the game ends, prompts the user to play again or exit.
    - If user chooses to play again `y`, the game restarts.
    - If user chooses to exit `n`, the game exits.

## Run Locally
Clone the project
```bash
git clone https://github.com/pathiik/guess-the-number.git
```
### Prerequisites
- `Python 3.11.9`

### Support
If you like this project, give it a ⭐ and share it with friends!

### Feedback
If you have any feedback or queries, please reach out to me at pathik.b45@gmail.com

###### Pathik Bhattarai