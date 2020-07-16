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
        #if the player has no cards then it auto adds it to the list
        if len(self.getCards()) == 0:
            newCard = Card(cardName)
            newCard.incrementOccurrence()
            self.cards.append(newCard)
        else:
            #if the player already has cards then it goes through to see if the new card is already in the list
            #if so it increments the card, otherwise it adds a new one
            cardInPlayer = False
            for card in self.getCards():
                if card.getName() == cardName:
                    card.incrementOccurrence()
                    cardInPlayer = True
                    break
            
            if cardInPlayer == False:
                newCard = Card(cardName)
                newCard.incrementOccurrence()
                self.cards.append(newCard)