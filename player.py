class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.points = 0

    #draws a card from deck.cards
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    #prints the value of each card in the hand
    def showHand(self):
        res = []
        for card in self.hand:
            res.append(card.show())
        return res

    #returns x cards from the hand, default all
    def getHand(self, num=None):
        res = []
        #make sure we dont go out of range and also set a default num
        if num > len(self.hand) or num == None:
            num = len(self.hand)
        for c in range(num):
            res.append(self.hand[c])
        return res

    #discards the last card in the hand
    def discard(self):
        return self.hand.pop()

    #add point(s), 1 point by default
    def addPts(self, pts=1):
        self.points += pts
