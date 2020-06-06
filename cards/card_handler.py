import json
from .card import Card

#loads the cards from a json file, creates a card object for each from the card class, returns the lists of the cards
def loadCards():
    url = "./cards/cards.json"
    with open(url) as f:
        data = json.load(f)

    suspectCards, weaponCards, roomCards = [], [], []

    for suspect in data["suspects"]:
        suspectCards.append(Card(suspect["name"]))
    for weapon in data["weapons"]:
        weaponCards.append(Card(weapon["name"]))
    for room in data["rooms"]:
        roomCards.append(Card(room["name"]))
    
    return suspectCards, weaponCards, roomCards
