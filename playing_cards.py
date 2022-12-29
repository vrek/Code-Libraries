"""A series of classes to work with playing cards"""
import random
class PlayingCard(object):
    """Class to handle individual playing cards
    inputs are suit and value, all lower case"""
    def __init__(self, suit, face_value):
        suits = ('hearts', 'diamonds', 'spades', 'clubs')
        face_values = ('one','two','three','four','five','six','seven','eight','nine','ten','jack','queen', 'king', 'ace')
        if suit in suits:
            self.suit = suit
        else:
            raise TypeError
        if face_value in face_values:
            self.face_value = face_value
        else:
            raise TypeError
    def show(self):
        print(f"{self.face_values} of {self.suit}")

class Deck:
    """Class """
    suits = ('hearts', 'diamonds', 'spades', 'clubs')
    face_values = ('one','two','three','four','five','six','seven','eight','nine','ten','jack','queen', 'king', 'ace')
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in self.suits:
            for v in self.face_values:
                self.cards.append(PlayingCard(s,v))
    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def drawCard(self):
        return self.cards.pop()
    def show(self):
        for c in self.cards:
            c.show()

class Player:
    def __init__(self):
        self.hand = []
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    def showHand(self):
        for card in self.hand:
            card.show()
