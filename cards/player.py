from .card import Card

#class for the players
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def getName(self):
        return self.name

    def getCards(self):
        return self.cards
    
    def addCard(self, cardName):
        self.cards.append(Card(cardName))