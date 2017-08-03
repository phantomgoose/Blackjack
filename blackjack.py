"""
#####MVP#####
###GAME SETUP###

Create deck - done
Shuffle deck - done on deck creation
Create 1 player and a dealer
Each play is dealt two cards



###GAMEPLAY###
Set value of fade cards to 10
Set initial value of Ace Cards to 11
If total hand value exceeds 21, Ace value is changed to 1
Player decides to get another card or pass

Dealer must keep drawing new card until total hand value reaches minimum of 17
Once dealer reaches 17-21 game ends
If player hasn't exceeded 21 and has a higher hand value than the dealer, the player wins



#####ADD ONS#####
Add ability to bet poker chips
Add card counter, in order to make the Dealer more competitive
Add GUI, rather than running in console
Add ability for the player to choose their name
 """

from deck import Deck
from player import Player

#generate game objects
d = Deck()
player = Player("Hamilton")
dealer = Player("Dealer")

#have both player and dealer draw 2 cards
player.draw(d).draw(d)
dealer.draw(d).draw(d)

#calculate player's points
def calcPoints(p):
    pts = 0
    for c in p.hand:
        if c.value < 10:
            pts += c.value
        elif c.value >= 10:
            pts += 10
        else:
            print "invalid card value"
    p.points += pts
calcPoints(player)
calcPoints(dealer)
print player.points
print dealer.points
