# This code utilizes the tabulate library


from deck_builder import deck, Card
from random import shuffle
from itertools import combinations
from tabulate import tabulate
import itertools
import sys

# Shuffles the deck and splits it in half for the user and computer
shuffle(deck)
player_deck = deck[len(deck) // 2 :]
ai_deck = deck[: len(deck) // 2]


class Game:
    """Game"""

    def __init__(self):
        """Init"""

        self.ai_winning_cards = {"Fire": [], "Ice": [], "Water": []}
        self.player_winning_cards = {"Fire": [], "Ice": [], "Water": []}
        self.ai_winning_display = [[], [], []]
        self.player_winning_display = [[], [], []]
        self.player_winning_set = []
        self.ai_winning_set = []

    # Prompts user for input
    def user_choice(self):
        """User Choice"""

        answer = input("1) Play Card\n2) Show Winning Cards\n3) Exit\nEnter Choice: ")
        return answer

    # Provides user with selection of the three first cards from their deck to choose from and removes it from their deck when chosen
    def select_card(self):
        """Card Choice"""

        for line1, line2, line3 in zip(
            player_deck[0].acii.splitlines(),
            player_deck[1].acii.splitlines(),
            player_deck[2].acii.splitlines(),
        ):
            print(f"{line1}     {line2}     {line3}")
        print("      1                 2                 3")
        choice = input("Choose Card: ")

        # Ensures that the input is a valid selection
        try:
            if int(choice) not in [1, 2, 3]:
                print("\nInvalid Choice\n")
        except:
            print("\nInvalid Choice\n")
        card_choice = player_deck[int(choice) - 1]

        # Displays the cards played by the user and the computer
        print("\nYou play:         I play:")
        for line1, line2 in zip(
            card_choice.acii.splitlines(), ai_deck[0].acii.splitlines()
        ):
            print(f"{line1}     {line2}")
        print("")
        return card_choice

    # Decides which card has won, if any, and displays an appropriate message to let user know
    def round_win(self, card_choice: Card):
        """Determines Round Winner"""

        if card_choice.battle(ai_deck[0]) == "Draw":
            print("IT WAS A DRAW\n")
        elif card_choice.battle(ai_deck[0]):
            print("YOUR CARD WINS\n")
            self.winning_card_append(
                card_choice, self.player_winning_cards, self.player_winning_display
            )
            self.game_win(
                card_choice, self.player_winning_cards, self.player_winning_set
            )
        else:
            print("MY CARD WINS\n")
            self.winning_card_append(
                ai_deck[0], self.ai_winning_cards, self.ai_winning_display
            )
            self.game_win(ai_deck[0], self.ai_winning_cards, self.ai_winning_set)
        return

    # Appends the winning card to the winning cards dictionary and a list for their display
    def winning_card_append(
        self, card: Card, winning_cards: dict, display_list: list[list]
    ):
        """Appends Winning Card"""

        winning_cards[card.type].append(card)
        if card.type == "Fire":
            display_list[0].append(card.acii)
        if card.type == "Ice":
            display_list[1].append(card.acii)
        if card.type == "Water":
            display_list[2].append(card.acii)
        return

    # Determines if there is a winner, informs the user, and displays the winning cards
    def game_win(self, card: Card, winning_cards: dict, winning_set: list):
        """Determines Game Winner"""

        if (
            len(winning_cards["Fire"]) >= 1
            and len(winning_cards["Ice"]) >= 1
            and len(winning_cards["Water"]) >= 1
        ):
            card_combinations = list(itertools.product(*winning_cards.values()))
            for t in card_combinations:
                if (
                    t[0].color != t[1].color
                    and t[0].color != t[2].color
                    and t[1].color != t[2].color
                ):
                    winning_set.extend([t[0], t[1], t[2]])
                    break
        if len(winning_cards[card.type]) >= 3:
            card_combinations = []
            card_combinations += list(combinations(winning_cards[card.type], 3))
            for t in card_combinations:
                if (
                    t[0].color != t[1].color
                    and t[0].color != t[2].color
                    and t[1].color != t[2].color
                ):
                    winning_set.extend([t[0], t[1], t[2]])
                    break

        if len(self.player_winning_set) == 3:
            print("Congratulations, you've won!\nYour winning set:")
            self.display_set(self.player_winning_set)
        if len(self.ai_winning_set) == 3:
            print("You've lost.\nMy winning set:")
            self.display_set(self.ai_winning_set)
        return

    # Displays the winning set
    def display_set(self, winning_set: list[Card]):
        """Displays Winning Set"""

        for line1, line2, line3 in zip(
            winning_set[0].acii.splitlines(),
            winning_set[1].acii.splitlines(),
            winning_set[2].acii.splitlines(),
        ):
            print(f"{line1}     {line2}     {line3}")
        sys.exit()

    # Displays the winning cards
    def display_winning_cards(self):
        """Displays Winning Cards"""

        print("\nYour winning cards:")
        print(tabulate(self.player_winning_display))
        print("My winning cards:")
        print(tabulate(self.ai_winning_display) + "\n")


game = Game()

# Explains how the game is played
print(
    """In this card game, each card possesses three attributes: type, number, and color. The type can be Fire, Ice, or Water. During each round, 
you will be presented with a selection of three cards to choose from. Upon making a selection, the computer will play a card as well. The comparison 
process begins with the types of the cards: Fire beats Ice, Ice beats Water, and Water beats Fire. If the types are the same, the numbers on the 
cards are compared, with the higher number prevailing. In case of a tie in both type and number, the round ends without a winner. To win the game, a 
player must acquire a specific set of three cards. The winning set is determined by both type and color. If a player possesses either three cards of 
the same type or one card of each type, and the colors of all three cards are distinct, that player is declared the winner."""
)

while True:
    answer = game.user_choice()
    if answer == "1":
        card_choice = game.select_card()
        game.round_win(card_choice)
        player_deck.pop(player_deck.index(card_choice))
        ai_deck.pop(0)
    elif answer == "2":
        game.display_winning_cards()
    elif answer == "3":
        print("Goodbye")
        sys.exit()
    else:
        print("\nInvalid Input\n")
