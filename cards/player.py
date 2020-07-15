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
        if len(self.getCards()) == 0:
            newCard = Card(cardName)
            newCard.incrementOccurrence()
            self.cards.append(newCard)
        else:
            for card in self.getCards():
                if card.getName() == cardName:
                    card.incrementOccurrence()
                    break