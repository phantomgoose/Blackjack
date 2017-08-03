class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []

    #draws a card from deck.cards
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    #prints the value of each card in the hand
    def showHand(self):
        for card in self.hand:
            card.show()

    #discards the last card in the hand
    def discard(self):
        return self.hand.pop()
