# A simple Rock, Paper, Scissors Game in Python
## Project Overview

This project is a simple implementation of the classic **Rock, Paper, Scissors** game using Python. The game allows a user to play against the computer, with both the user and the computer selecting one of three options: **rock**, **paper**, or **scissors**. The game then evaluates the choices and announces the winner or declares a draw. The game is built with ASCII art representations for each choice to enhance the user experience.

## Features

- **Simple User Interface**: The user is prompted to input their choice of **rock**, **paper**, or **scissors**.
- **Computer's Choice**: The computer randomly selects its choice from the same three options.
- **Game Logic**: The program evaluates the user's choice against the computer's choice and determines the winner based on the classic rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- **ASCII Art Representation**: Each option (rock, paper, and scissors) is displayed using an ASCII art design, making the game visually appealing.

## How the Game Works

1. **User Input**: The game prompts the user to input their choice. Valid inputs are "rock", "paper", or "scissors". The program automatically handles input case-sensitivity by converting the user's input to lowercase.
   
2. **Computer's Random Choice**: The computer's choice is randomly selected from the three options: rock, paper, or scissors. This is done using Python's `random.choice()` function, which picks a random item from a list.
   
3. **Display Choices**: Once both the user and the computer have selected their choices, the game prints the ASCII art for each option. The art is displayed in the console to make the game more visually engaging.

4. **Determine the Winner**: The game follows the traditional rules:
   - Rock crushes Scissors
   - Scissors cut Paper
   - Paper covers Rock
   The program compares the choices and announces who won or if the game is a draw.

5. **Invalid Input Handling**: If the user enters an invalid choice (anything other than "rock", "paper", or "scissors"), the game notifies them of the invalid input and prompts for a valid selection.

## ASCII Art Representations

To make the game more interactive, each option is represented using ASCII art. Here’s how each choice is displayed:

- **Rock**: Represented by a closed fist (symbolizing the hand in a rock shape).
  
    ```plaintext
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__.(___)
    ```

- **Paper**: Represented by an open hand with five fingers spread out, symbolizing paper.

    ```plaintext
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__.__________)
    ```

- **Scissors**: Represented by two fingers raised in a "V" shape, symbolizing scissors.

    ```plaintext
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__.(___)
    ```

## How to Play

1. **Run the Program**: Once the program is executed, you’ll be prompted to enter one of the three choices: **rock**, **paper**, or **scissors**.
   
2. **View Results**: After making your choice, the program will display:
   - The computer's random choice with its corresponding ASCII art.
   - Your own choice with its ASCII art.
   - The result of the game (win, lose, or draw).

3. **Continue Playing**: To play again, simply restart the program. Currently, the game does not loop automatically, but you can modify the code to allow multiple rounds.

## Example Gameplay

```bash
Enter your choice: rock, paper, or scissors: paper

Computer's choice: rock

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Your choice: paper

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

You won!
```

## How to Run the Game

1. **Clone the Repository**:
   To run the game on your local machine, clone the repository:
   ```bash
   git clone https://github.com/yourusername/rockpaperscissors.git
   cd rock-paper-scissors
   ```

2. **Run the Python Script**:
   Ensure you have Python installed. If you don't, you can download it from [here](https://www.python.org/downloads/).
   Run the game using the following command:
   ```bash
   python rockpaperscissors.py
   ```

## Customizations

- You can expand the game by adding additional choices thereby extending the game.
- You can modify the ASCII art to suit your own design preferences.
- To add multiple rounds or a scoring system, you can introduce a loop to repeatedly ask the user for input and track their wins, losses, and draws.

## Conclusion

This **Rock, Paper, Scissors** game is a fun way to practice Python programming, especially working with random selections, input validation, and ASCII art. It's a simple game that can be expanded with additional features like multiplayer support or more complex game logic.

Feel free to fork the repository, improve the game, and share your changes!

---
