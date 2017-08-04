class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    #prints the card value to console
    def show(self):
        return '{} of {}'.format(self.valToName(self.value), self.suit)

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

    def getShortValue(self):
        conversionDict = {
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "J",
            12: "Q",
            13: "K",
            14: "A"
        }
        return conversionDict[self.value]

    def getShortSuit(self):
        conversionDict = {
            "Hearts": "H",
            "Diamonds": "D",
            "Spades": "S",
            "Clubs":"C"
        }
        return conversionDict[self.suit]

#test cases
if __name__ == "__main__":
    c = Card("Clubs", 11)
    b = Card("Diamonds", 10)
    c.show()
    b.show()
