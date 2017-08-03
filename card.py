class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self):
        print '{} of {}'.format(self.valToName(self.value), self.suit)

    #converts card's value (1-14) to its name (2 -> Ace)
    def valToName(self, val):
        conversionDict = {
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace"
        }
        return conversionDict[val]

if __name__ == "__main__":
    c = Card("Clubs", 11)
    b = Card("Diamonds", 10)
    c.show()
    b.show()
