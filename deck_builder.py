from __future__ import annotations

deck = []

# Saves acii art of cards into respective variables
fire_card = """.++-----------+
.+| FIRE   ## |
.+|     \033[38;5;208m).+     |
.+|    \033[38;5;208m) \.+    |
.+|   \033[38;5;208m/ ) (.+   |
.+|   \033[38;5;208m\(_)/.+   |
.+| ##   FIRE |
.++-----------+\033[0m"""

ice_card = """.++-----------+
.+| ICE    ## |
.+|  \033[0m__/\__.+   |
.+|  \033[0m\_\/_/.+   |
.+|  \033[0m/_/\_\.+   |
.+|    \033[0m\/.+     |
.+| ##    ICE |
.++-----------+\033[0m"""

water_card = """.++-----------+
.+| WATER  ## |
.+|    \033[36m/\.+     |
.+|   \033[36m/  \.+    |
.+|  \033[36m||  ||.+   |
.+|  \033[36m\\\__//.+   |
.+| ##  WATER |
.++-----------+\033[0m"""


class Card:
    '''Card'''

    def __init__(self, type: str, color: str, number: int, acii: str):
        '''Init'''
        self.type = type
        self.color = color
        self.number = number
        self.acii = acii

    # Compares cards that have been played to determine the winner, returning a boolean relative to the user's chosen card or a string if it is a draw
    def battle(self, challenger: Card):
        '''Card Comparison'''
        if self.type == challenger.type:
            if self.number == challenger.number:
                return "Draw"
            return self.number > challenger.number
        if self.type == "Fire":
            return challenger.type == "Ice"
        if self.type == "Ice":
            return challenger.type == "Water"
        if self.type == "Water":
            return challenger.type == "Fire"


# Builds the deck with instantiations of the Card Class using unique combinations of attributes
def deck_builder():
    '''Deck Builder'''
    types = ["Fire", "Ice", "Water"]
    colors = ["Red", "Green", "Yellow", "Blue"]
    numbers = [5, 6, 7, 8, 9, 10, 11, 12]
    for t in types:
        for c in colors:
            for n in numbers:
                acii_card = ""
                if t == "Fire":
                    acii_card = fire_card
                elif t == "Ice":
                    acii_card = ice_card
                elif t == "Water":
                    acii_card = water_card
                if c == "Red":
                    acii_card = acii_card.replace(".+", "\033[91m")
                elif c == "Green":
                    acii_card = acii_card.replace(".+", "\033[32m")
                elif c == "Yellow":
                    acii_card = acii_card.replace(".+", "\033[33m")
                elif c == "Blue":
                    acii_card = acii_card.replace(".+", "\033[34m")
                if n <= 9:
                    acii_card = acii_card.replace("##", f"0{str(n)}")
                else:
                    acii_card = acii_card.replace("##", str(n))
                deck.append(Card(t, c, n, acii_card))


deck_builder()
