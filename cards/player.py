from .card import Card
import operator

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
            self.sortCards()
        else:
            #if the player already has cards then it goes through to see if the new card is already in the list
            #if so it increments the card, otherwise it adds a new one
            cardInPlayer = False
            for card in self.getCards():
                if card.getName() == cardName:
                    card.incrementOccurrence()
                    cardInPlayer = True
                    self.sortCards()
                    break
            
            if cardInPlayer == False:
                newCard = Card(cardName)
                newCard.incrementOccurrence()
                self.cards.append(newCard)
                self.sortCards()

    #sorts all the cards on the player by their occurence number from highest to lowest
    def sortCards(self):
        self.cards.sort(reverse=True, key=operator.attrgetter('occurrence'))