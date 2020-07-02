#class for the cards

class Card:
    def __init__(self, name):
        self.name = name
        self.chance = 100

    def getName(self):
        return self.name

    def getChance(self):
        return self.chance
    
    def setChance(self, newChance):
        self.chance = newChance

    