class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.points = 0

    # draws a card from the specified deck
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    # prints the value of each card in the hand
    def showHand(self):
        res = []
        for card in self.hand:
            res.append(card.show())
        return res

    # discards the last card in the hand and returns it
    def discard(self):
        return self.hand.pop()

    # returns number of card X in the hand
    def getNumOfCard(self, card_val):
        count = 0
        for c in self.hand:
            if c.value == card_val:
                count += 1
        return count
