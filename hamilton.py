from deck import Deck
from player import Player

#generate game objects
d = Deck()
p1 = Player("Hamilton")
p2 = Player("Burr")

#while there are cards remaining in the deck
while (len(d.cards) > 0):
    #both players draw
    p1.draw(d)
    p2.draw(d)

    #print first card in the hand for each player
    print p1.name + " drew a " + p1.getHand(1)[0].show()
    print p2.name + " drew a " + p2.getHand(1)[0].show()

    #compare draws
    if p1.getHand(1)[0].value > p2.getHand(1)[0].value:
        #if the first player draws the higher value card, grant him a pointw
        print "***" + p1.name + " wins this round"
        p1.addPts()
    elif p1.getHand(1)[0].value < p2.getHand(1)[0].value:
        #if the second player draws the higher value card, grant him a point
        print "***" + p2.name + " wins this round"
        p2.addPts()
    elif p1.getHand(1)[0].value == p2.getHand(1)[0].value:
        #no points for anyone
        print "***Nobody wins this round!"
    else:
        input("invalid card values for the two players, press Enter to stop playing")
        break

    #both players discard their hand before drawing again
    p1.discard()
    p2.discard()

#announce the winner
if p1.points > p2.points:
    print "Game over. " + p1.name + " wins with " + str(p1.points) + " points! " + p2.name + " had " + str(p2.points) + " points."
elif p1.points < p2.points:
    print "Game over. " + p2.name + " wins with " + str(p2.points) + " points! " + p1.name + " had " + str(p1.points) + " points."
elif p1.points == p2.points:
    print "Game over. It's a draw! Both players have " + str(p1.points) + " points."
else:
    input("Something broke with the points. Press Enter to exit.")
