class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # returns a string representation of the card
    def show(self):
        return '{} of {}'.format(self.valToName(self.value), self.suit)

    # returns the card's name as a string based on its value
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

    # returns the card's value as a shortened string
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

    # returns the card's suit as a shortened string
    def getShortSuit(self):
        conversionDict = {
            "Hearts": "H",
            "Diamonds": "D",
            "Spades": "S",
            "Clubs":"C"
        }
        return conversionDict[self.suit]

# test cases
if __name__ == "__main__":
    c = Card("Clubs", 11)
    b = Card("Diamonds", 10)
    c.show()
    b.show()