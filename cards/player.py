from .card import Card
import operator

#class for the players
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.verifiedCards = []

    def getName(self):
        return self.name

    def getCards(self):
        return self.cards

    def getVerifiedCards(self):
        return self.verifiedCards
    
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

    def removeCard(self, cardName):
        for i in range(len(self.cards)):
            if self.cards[i].getName() == cardName:
                self.cards.pop(i)
                break

    #when we see that a player has a specific card we verify it.  This is seperate from the regular cards as we know for a fact they have it.
    def verifyCard(self, cardName):
        cardAlreadyVerified = False
        #if the card has already been verified we do nothing
        for card in self.verifiedCards:
            if card.getName() == cardName:
                cardAlreadyVerified = True
                break
        #if it is not yet verified we need to add it to our verified list.  We will also then need to go through our main list of cards and remove it from
        #the list if it was in the possible cards.
        if cardAlreadyVerified == False:
            newCard = Card(cardName)
            newCard.incrementOccurrence()
            self.verifiedCards.append(newCard)

            for i in range(len(self.cards)):
                if self.cards[i].getName() == cardName:
                    self.cards.pop(i)
                    break