'''
Game logic:
    1) Generate a deck - done
    2) Shuffle the deck - done on deck generation
    3) Create 2 players - done
    4) Each player draws a card - done
    5) Whoever's card is better than the other's gets a point
    6) Once the deck is empty, the player with the most points wins
'''

from deck import Deck
from player import Player

#generate game objects
d = Deck()
p1 = Player("Alex")
p2 = Player("Chris")

test_count = 1

#while there are cards remaining in the deck
while (len(d.cards) > 0 and test_count > 0):
    #both players draw
    p1.draw(d)
    p2.draw(d)

    #compare draws

    #print first card in the hand for each player
    print p1.getHand(1)[0].show()
    print p2.getHand(1)[0].show()

    #make sure we dont enter an infinite loop
    test_count -= 1
