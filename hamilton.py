'''
Game logic:
    1) Generate a deck
    2) Shuffle the deck
    3) Create 2 players
    4) Each player draws a card
    5) Whoever's card is better than the other's gets a point
    6) Once the deck is empty, the player with the most points wins
'''

from deck import Deck

d = Deck()
d.show()
