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
def calcPoints(p, ace_value = 11):
    pts = 0
    p.points = 0
    for c in p.hand:
        if c.value < 10:
            pts += c.value
        elif c.value < 14:
            pts += 10
        elif c.value == 14:
            pts += ace_value
        else:
            print "invalid card value"
    p.points += pts

def isGameOver(p, d):
    if (p.points >= 21 or d.points >= 21):
        return True
    return False

def getPlayerChoice():
    player_choice = raw_input("hit or stand?")
    if player_choice != "hit" and player_choice != "stand":
        print "Invalid input, try again"
        getPlayerChoice()
    else:
        return player_choice


#calculate starting points for both player and dealer
calcPoints(player)
calcPoints(dealer)

playerStand = False

#run this loop until
while not isGameOver(player, dealer):

    #print game state information
    print "Dealer's first card: " + dealer.getHand()[0].show()
    print "You have " + str(player.points) + " points. Your hand consists of: "
    print player.showHand()

    #player goes first
    #first we get their choice
    if not playerStand:
        if getPlayerChoice() == "hit":
            player.draw(d)
        else:
            playerStand = True

    #dealer always draws... for now
    dealer.draw(d)

    #recalculate points for both dealer and player every loop
    calcPoints(player)
    calcPoints(dealer)

#after the game ends
print "*****GAME OVER*****"

if player.points > 21 and dealer.points > 21:
    #REFACTOR THIS MESS
    print "NOBODY WINS!"
    print "You have " + str(player.points) + " points. Your hand consists of: "
    print player.showHand()
    print "Dealer has " + str(dealer.points) + " points. Their hand consists of: "
    print dealer.showHand()
elif (player.points > dealer.points or dealer.points > 21) and player.points <= 21:
    print "YOU WIN!"
    print "You have " + str(player.points) + " points. Your hand consists of: "
    print player.showHand()
    print "Dealer has " + str(dealer.points) + " points. Their hand consists of: "
    print dealer.showHand()
else:
    print "YOU LOSE!"
    print "You have " + str(player.points) + " points. Your hand consists of: "
    print player.showHand()
    print "Dealer has " + str(dealer.points) + " points. Their hand consists of: "
    print dealer.showHand()
