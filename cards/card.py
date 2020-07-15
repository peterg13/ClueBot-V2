#class for the cards

class Card:
    def __init__(self, name):
        self.name = name
        self.chance = 100
        self.occurrence = 0 #this variable is only used when this class is part of a player.

    def getName(self):
        return self.name

    def getChance(self):
        return self.chance
    
    def setChance(self, newChance):
        self.chance = newChance

    def getOccurrence(self):
        return self.occurrence

    def incrementOccurrence(self):
        self.occurrence += 1

    def resetOccurrence(self):
        self.occurrence = 0

    