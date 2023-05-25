# Card Game

This is a simple card game implemented in Python. Each card in the game has three attributes: type, number, and color. The objective of the game is to be the first player to obtain a specific set of three cards.

## Game Rules

- The type of a card can be one of Fire, Ice, or Water.
- The number on a card can be any integer from 5 to 12.
- The color of a card can be Red, Green, Yellow, or Blue.
- At the beginning of the game, the deck is shuffled and divided equally between the player and the computer.
- In each round, the player is presented with a selection of three cards to choose from.
- The computer also plays a card.
- The comparison process starts with comparing the types of the cards. Fire beats Ice, Ice beats Water, and Water beats Fire.
- If the types are the same, the numbers on the cards are compared, with the higher number winning.
- In case of a tie in both type and number, the round ends without a winner.
- If a player wins a round, their winning card is saved.
- To win the game, a player must collect a specific set of three cards.
- The winning set is determined by both type and color. The player must have either three cards of the same type or one card of each type, with distinct colors.

## Project Structure

- `deck_builder.py`: This file contains the code for building the deck of cards.
- `card_game.py`: This file contains the main game logic, including the Game class and the game flow.

## Dependencies

The project relies on the following dependencies:

- `tabulate`: A Python library used for generating nicely formatted tables.

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the `tabulate` library by running the following command: `pip install tabulate`.
3. Run the `card_game.py` file using Python: `python card_game.py`.
4. Follow the prompts to play the card game.
5. Choose a card from the selection provided and see the result of the round.
6. The game will continue until a player wins or you choose to exit.

Enjoy playing the card game!