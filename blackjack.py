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

ace_value = 11

#have both player and dealer draw 2 cards
player.draw(d).draw(d)
dealer.draw(d).draw(d)

#calculate player's points
def calcPoints(p):
    #reset points to zero
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
    #if you go over 21 and you have aces in your hand that haven't been ignored yet, ignore an ace and recalculate the points
    aces_in_hand = p.getNumOfCard(14)
    if pts > 21 and aces_in_hand > 0:
        ignored_ace_count = 1
        while pts > 21 and ignored_ace_count <= aces_in_hand:
            pts -= 10
            ignored_ace_count += 1

    #finally update the player's points
    p.points += pts

def isGameOver(p, d):
    if (p.points >= 21 or d.points >= 21):
        return True
    return False

def getPlayerChoice():
    player_choice = raw_input("hit or stand? ")
    if player_choice != "hit" and player_choice != "stand":
        print "Invalid input, try again"
        getPlayerChoice()
    else:
        return player_choice

def showGameState():
    print "You have " + str(player.points) + " points. Your hand consists of: "
    print player.showHand()
    print "Dealer has " + str(dealer.points) + " points. Their hand consists of: "
    print dealer.showHand()

#calculate starting points for both player and dealer
calcPoints(player)
calcPoints(dealer)

playerStand = False
dealerStand = False

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
            print "YOU DRAW A CARD"
            player.draw(d)
        else:
            playerStand = True

    #dealer always draws... for now
    if dealer.points < 17:
        print "DEALER DRAWS A CARD"
        dealer.draw(d)
    else:
        print "DEALER DOESN'T DRAW ANYMORE"
        dealerStand = True

    #recalculate points for both dealer and player every loop
    calcPoints(player)
    calcPoints(dealer)

    #end the game if neither the player nor the dealer are willing to draw cards
    if dealerStand and playerStand:
        break

#after the game ends
print "*****GAME OVER*****"

if player.points > 21 and dealer.points > 21:
    #REFACTOR THIS MESS
    print "NOBODY WINS!"
    showGameState()
elif (player.points > dealer.points or dealer.points > 21) and player.points <= 21:
    print "YOU WIN!"
    showGameState()
else:
    print "YOU LOSE!"
    showGameState()
