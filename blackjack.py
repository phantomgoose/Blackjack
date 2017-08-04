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
    print "****************************************************************************************"
    player_choice = raw_input("HIT OR STAND? ")
    if player_choice != "hit" and player_choice != "stand":
        print "Invalid input, try again"
        getPlayerChoice()
    else:
        return player_choice

def showGameState():
    print "You have " + str(player.points) + " points. Your hand consists of: ", player.showHand()
    print "Dealer has " + str(dealer.points) + " points. Their hand consists of: ", dealer.showHand()

#calculate starting points for both player and dealer
calcPoints(player)
calcPoints(dealer)

global playerStand
playerStand = False
global dealerStand
dealerStand = False
global gameOver
gameOver = False

'''
functions for server comm
'''

def getDealerCard():
    return dealer.getHand()[0].show()

def getPlayerCards():
    return player.showHand()

def getPlayerPoints():
    return player.points

def getDealerCards():
    return dealer.showHand()

def getDealerPoints():
    return dealer.points

def setPlayerChoice(choice):
    if not playerStand:
        if choice == "hit":
            print "YOU DRAW A CARD"
            player.draw(d)
        else:
            playerStand = True

def getGameState():
    print gameOver
    if gameOver != True:
        return "Game is not over yet, still playing. You have " + str(getPlayerPoints()) + " points."
    else:
        if player.points > 21 and dealer.points > 21:
            return "Nobody wins! Dealer's hand: " + str(getDealerCards()) + " dealer points " + str(getDealerPoints()) + " Your points: " + str(getPlayerPoints())
        elif (player.points > dealer.points or dealer.points > 21) and player.points <= 21:
            return "YOU WIN! Dealer's hand: " + str(getDealerCards()) + " dealer points " + str(getDealerPoints()) + " Your points: " + str(getPlayerPoints())
        else:
            return "YOU LOSE! Dealer's hand: " + str(getDealerCards()) + " dealer points " + str(getDealerPoints()) + " Your points: " + str(getPlayerPoints())

def play(choice):

    #print game state information
    print "Dealer's first card: " + dealer.getHand()[0].show()
    print "YOU HAVE " + str(player.points).upper() + " POINTS. Your hand consists of: ", player.showHand()

    #player goes first
    #first we get their choice
    if not playerStand:
        if choice == "hit":
            print "YOU DRAW A CARD"
            player.draw(d)
        else:
            global playerStand
            playerStand = True

    #dealer always draws until they have at least 17 points
    if dealer.points < 17:
        print "DEALER DRAWS A CARD"
        dealer.draw(d)
    else:
        print "DEALER DOESN'T DRAW ANYMORE"
        global dealerStand
        dealerStand = True

    #recalculate points for both dealer and player every loop
    calcPoints(player)
    calcPoints(dealer)

    #end the game if neither the player nor the dealer are willing to draw cards
    if (dealerStand and playerStand) or isGameOver(player, dealer):
        global gameOver
        gameOver = True
        print "Game over"
        print getDealerCards()
        print getDealerPoints()
'''
    #after the game ends
    print "***************GAME OVER***************"

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
'''
