import random

class Deck(object):
    def __init__(self):
        self.cards = []
        self.create()
        self.shuffle() #shuffling off the bat, if that's what we want?

    #generates the deck of cards
    def create(self):
        #for each suit
        for x in ['Hearts','Diamonds','Spades','Clubs']:
            #generates cards from 2 to 14 (14 being Ace)
            for y in range(2,15):
                #pushes the generated card object to deck.cards
                self.cards.append(Card(x,y))

    #prints the value of each card in the deck
    def show(self):
        for z in self.cards:
            z.show()

    #shuffles the deck
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    #draws a card from the end of deck.cards list and removes it
    def drawCard(self):
        return self.cards.pop()
