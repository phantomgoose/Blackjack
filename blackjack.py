from deck import Deck
from player import Player

# generate game objects
DECK = Deck()
PLAYER = Player("Alex")
DEALER = Player("Dealer")

# sets default Ace value (can be 1 or 11 in Blackjack)
DEFAULT_ACE_VALUE = 11

# have both player and dealer draw 2 cards
PLAYER.draw(DECK).draw(DECK)
DEALER.draw(DECK).draw(DECK)

# calculate player's points
def calcPoints(p):
    # set initial points to zero
    pts = 0
    for c in p.hand:
        if c.value < 10:
            pts += c.value
        elif c.value < 14:
            pts += 10
        elif c.value == 14:
            pts += DEFAULT_ACE_VALUE
    
    # if the player goes over 21 and has aces in their hand, sets the value of aces to 1 (by subtracting 10 pts for each ace) until the player is under 21 points
    aces_in_hand = p.getNumOfCard(14)
    if pts > 21 and aces_in_hand > 0:
        ignored_ace_count = 0
        while pts > 21 and ignored_ace_count < aces_in_hand:
            pts -= 10
            ignored_ace_count += 1

    # finally update the player's points
    p.points = pts

# returns true if both dealer and player are at 21 or more points
def isGameOver(p, d):
    if (p.points >= 21 and d.points >= 21):
        return True
    return False

# calculate starting points for both player and dealer
calcPoints(PLAYER)
calcPoints(DEALER)

# these global variables keep track of current game state and dealer's and player's decision to Stand and cease drawing cards
playerStand = False
dealerStand = False
gameOver = False

'''
functions for server comm
'''

def getPlayerState():
    if not playerStand and not gameOver:
        return "playing"
    else:
        return "standing"

def getPlayerCards():
    return PLAYER.hand

def getDealerCards():
    return DEALER.hand

# returns a string that explains the current state of the game
def getGameState():
    if not gameOver:
        if not playerStand:
            return "Still playing. Dealer points: " + str(DEALER.points) + ". Your points: " + str(PLAYER.points) + "."
        else:
            return "Dealer is still drawing. Dealer points: " + str(DEALER.points) + ". Your points: " + str(PLAYER.points) + ". Click 'continue' to move on."
    else:
        if PLAYER.points > 21 and DEALER.points > 21:
            return "Nobody wins! Dealer points: " + str(DEALER.points) + ". Your points: " + str(PLAYER.points) + "."
        elif (PLAYER.points > DEALER.points or DEALER.points > 21) and PLAYER.points <= 21:
            return "YOU WIN! Dealer points: " + str(DEALER.points) + ". Your points: " + str(PLAYER.points) + "."
        else:
            return "YOU LOSE! Dealer points: " + str(DEALER.points) + ". Your points: " + str(PLAYER.points) + "."

# main game method. Takes a string as a parameter, which determines player's action
def play(choice):
    global playerStand
    global dealerStand
    global gameOver

    # player goes first
    # ensure player didn't choose to stand before
    if not playerStand:
        if choice == "hit" and PLAYER.points < 21:
            PLAYER.draw(DECK)
        else:
            playerStand = True

    # dealer draws until they have at least 17 points, but will draw past that if the player chose to stand and has more points
    if not gameOver and (DEALER.points < 17 or (playerStand and DEALER.points < 21 and DEALER.points < PLAYER.points)):
        DEALER.draw(DECK)
    else:
        dealerStand = True

    # recalculate points for both dealer and player every time this method runs
    calcPoints(PLAYER)
    calcPoints(DEALER)

    # end the game if neither the player nor the dealer are willing to draw cards OR if both parties have 21 or more points
    if (dealerStand and playerStand) or isGameOver(PLAYER, DEALER):
        gameOver = True
