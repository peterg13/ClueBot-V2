import tkinter as tk
from cards import card_handler

class MainApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        #main bg color for the whole app
        self.mainAppBgColor = "#292929"

        #this line is so we can use root as the base frame to easier understand the frame layouts
        root = self
        root.config(bg=self.mainAppBgColor)
        root.title("ClueBot - V2")

        self.initCards()
        self.initPlayers()

        #Frame that holds the suspects, weapons and rooms ----------------
        swrFrame = tk.Frame(root, bg=self.mainAppBgColor, borderwidth = 5, relief = "solid")
        swrFrame.pack(side = tk.TOP)

        #variables that get passed to the remove button.  These variables hold the current radio button selection.  
        #Need to declare before the button so it has access to these variables and need to declare the remove button
        #before radiobuttons due to formatting issues.
        self.rbVars = {
            "suspectVar" : tk.StringVar(),
            "weaponVar" : tk.StringVar(),
            "roomVar" : tk.StringVar(),
            "playerVar" : tk.StringVar()
        }

        #button to remove the selected options
        self.buttonFrame = tk.Frame(root, bg=self.mainAppBgColor)
        self.buttonFrame.pack(side=tk.TOP)
        self.initButtons()

        #suspect section
        suspectFrame = tk.Frame(swrFrame, bg=self.mainAppBgColor)
        suspectFrame.pack(side = tk.LEFT, fill="y", padx=1)

        #weapon section        
        weaponFrame = tk.Frame(swrFrame, bg=self.mainAppBgColor)
        weaponFrame.pack(side = tk.LEFT, fill="y", padx=1)
        
        #room section        
        roomFrame = tk.Frame(swrFrame, bg=self.mainAppBgColor)
        roomFrame.pack(side = tk.LEFT, fill="y", padx=1)

        #player section        
        playerFrame = tk.Frame(swrFrame, bg=self.mainAppBgColor)
        playerFrame.pack(side = tk.LEFT, fill="y", padx=1)

        self.rbFrames = {
            "suspectFrame" : suspectFrame,
            "weaponFrame" : weaponFrame,
            "roomFrame" : roomFrame,
            "playerFrame" : playerFrame
        }
        
        #creates the radiobutton GUI
        self.updateRadioButtons()
        self.updatePlayerCheckboxes()

        #------------------------------------------------------------------------------------------------------------
        #this section is for the players
        self.playersFrame = tk.Frame(root, bg=self.mainAppBgColor, borderwidth = 1, relief = "solid")
        self.playersFrame.pack(side=tk.TOP, pady=5)

        self.updatePlayers()



        #------------------------------------------------------------------------------------------------------------

        #Frame that will show the possible winning cards along with their percentage for being a winning card
        self.resultsFrame = tk.Frame(root, bg=self.mainAppBgColor, borderwidth = 5, relief = "solid")
        self.resultsFrame.pack(side = tk.TOP)

        #creates the ListBoxes GUI that shows the winning cards
        #self.updateWinningLists()

    #inits the buttons for removing radio buttons and adding cards to a player  
    def initButtons(self):

        buttonBg = "#707070"
        buttonFont = "Helvetica"
        buttonFontSize = 25

        #button to remove a card (will color it red to indicate that it is eliminated as a possibility)
        tk.Button(self.buttonFrame, text="REMOVE", command = lambda : self.removeFunction(), bg=buttonBg, font=(buttonFont, buttonFontSize), width = 20).pack(side=tk.LEFT, pady=5, padx=1)
        #button to add the selected card(s) to the selected player(s)
        tk.Button(self.buttonFrame, text="Add To Player", command = lambda : self.addToPlayer(), bg=buttonBg, font=(buttonFont, buttonFontSize), width = 20).pack(side=tk.LEFT, pady=5, padx=1)
        #button to verify the card on the player (for when you see a specific card on a player)
        tk.Button(self.buttonFrame, text="Verify", command = lambda : self.verifyCardOnPlayer(), bg=buttonBg, font=(buttonFont, buttonFontSize), width = 10).pack(side=tk.LEFT, pady=5, padx=1)
        #button to clear all selections if we need to
        tk.Button(self.buttonFrame, text="Clear", command = lambda : self.clearSelections(), bg=buttonBg, font=(buttonFont, buttonFontSize), width = 10).pack(side=tk.LEFT, pady=5, padx=1)

    #method that gets called when the remove button gets click.  This will take the selections from the radio buttons, remove them from our saved
    #list of active cards and update the radiobutton list/chance list
    def removeFunction(self):
        #the following 3 loops will go through the three lists of cards and remove them from the radio buttons.
        for i in range(len(self.suspects)):
            if self.suspects[i].getName() == self.rbVars["suspectVar"].get():
                self.eliminateCard("suspect", self.suspects[i].getName())
                self.suspects.pop(i)
                break
        for i in range(len(self.weapons)):
            if self.weapons[i].getName() == self.rbVars["weaponVar"].get():
                self.eliminateCard("weapon", self.weapons[i].getName())
                self.weapons.pop(i)
                break
        for i in range(len(self.rooms)):
            if self.rooms[i].getName() == self.rbVars["roomVar"].get():
                self.eliminateCard("room", self.rooms[i].getName())
                self.rooms.pop(i)
                break

    #new function to replace the old remove.  Since we no longer want to remove a card we will instead mark it in red to represent that it is eliminated
    def eliminateCard(self, cardType, cardName):
        if cardType == "suspect":
            for child in self.rbFrames["suspectFrame"].children.values():
                if child.cget("text") == cardName:
                    child.config(bg="#c2938e")
                    self.rbVars["suspectVar"].set("")
                    break
        elif cardType == "weapon":
            for child in self.rbFrames["weaponFrame"].children.values():
                if child.cget("text") == cardName:
                    child.config(bg="#c2938e")
                    self.rbVars["weaponVar"].set("")
                    break
        elif cardType == "room":
            for child in self.rbFrames["roomFrame"].children.values():
                if child.cget("text") == cardName:
                    child.config(bg="#c2938e")
                    self.rbVars["roomVar"].set("")
                    break

    #LEGACY
    #given the name of the card this fucntion finds the radio button with the same name and removes it from the GUI
    def destroyRadioButton(self, cardType, cardName):
        if cardType == "suspect":
            for child in self.rbFrames["suspectFrame"].children.values():
                if child.cget("text") == cardName:
                    child.destroy()
                    break
        elif cardType == "weapon":
            for child in self.rbFrames["weaponFrame"].children.values():
                if child.cget("text") == cardName:
                    child.destroy()
                    break
        elif cardType == "room":
            for child in self.rbFrames["roomFrame"].children.values():
                if child.cget("text") == cardName:
                    child.destroy()
                    break

    #method to display the radio buttons.  creating a seperate method to help clearn up code a bit.
    #also adds a label above each section to function as a title
    def updateRadioButtons(self):
        #selection colors
        buttonColor = "#bcc8c9"
        selectColor = "#c9c0bc"

        font = "Helvetica"
        fontSize = 20

        labelBG = "#82acb0"
        labelFont = "Helvetica"
        labelFontSize = 25
        labelWidth = 15
        labelXPadding = 2
        labelYPadding = 5

        tk.Label(self.rbFrames["suspectFrame"], text = "Suspects", font = (labelFont, labelFontSize, "bold"), bg = labelBG, width = labelWidth).pack(fill="x", pady=labelYPadding, padx=labelXPadding)
        for suspect in self.suspects:
            tk.Radiobutton(self.rbFrames["suspectFrame"], text = suspect.getName(), variable = self.rbVars["suspectVar"], value = suspect.getName(), bg=buttonColor, selectcolor=selectColor, indicatoron = 0, font=(font, fontSize)).pack(fill="x")
        
        tk.Label(self.rbFrames["weaponFrame"], text = "Weapons", font = (labelFont, labelFontSize, "bold"), bg = labelBG, width = labelWidth).pack(fill="x", pady=labelYPadding, padx=labelXPadding)
        for weapon in self.weapons:
            tk.Radiobutton(self.rbFrames["weaponFrame"], text = weapon.getName(), variable = self.rbVars["weaponVar"], value = weapon.getName(), bg=buttonColor, selectcolor=selectColor, indicatoron = 0, font=(font, fontSize)).pack(fill="x")

        tk.Label(self.rbFrames["roomFrame"], text = "Rooms", font = (labelFont, labelFontSize, "bold"), bg = labelBG, width = labelWidth).pack(fill="x", pady=labelYPadding, padx=labelXPadding)
        for room in self.rooms:
            tk.Radiobutton(self.rbFrames["roomFrame"], text = room.getName(), variable = self.rbVars["roomVar"], value = room.getName(), bg=buttonColor, selectcolor=selectColor, indicatoron = 0, font=(font, fontSize)).pack(fill="x")  

    #method that handles the GUI for the section that shows the playuer checkboxes
    def updatePlayerCheckboxes(self):
        labelBG = "#82acb0"
        labelFont = "Helvetica"
        labelFontSize = 25
        labelWidth = 15
        labelXPadding = 2
        labelYPadding = 5
        checkBoxFont = "Helvetica"
        checkBoxFontSize = 21
        checkBoxColor = "#bcc8c9"
        selectColor = "#c9c0bc"

        tk.Label(self.rbFrames["playerFrame"], text = "Players", font = (labelFont, labelFontSize, "bold"), bg = labelBG, width = labelWidth).pack(fill="x", pady=labelYPadding, padx=labelXPadding)
        for player in self.players:
            tk.Checkbutton(self.rbFrames["playerFrame"], text = player.getName(), variable = self.playerVars[player.getName()], font = (checkBoxFont, checkBoxFontSize), bg = checkBoxColor, selectcolor=selectColor, indicatoron = 0).pack(fill = "x")

    #main source for the player GUI.  Creates a set of frames for each player and displays their possible cards
    def updatePlayers(self):
        labelFont = "Helvetica"
        labelFontSize = 25
        labelBG = "#82acb0"

        listFont = "Helvetica"
        listFontSize = 15
        listFontColor = "#bcc8c9"


        #this loop will go through each player added to the game
        #first it creates a new frame for each player and in the frame creates a label for their name and a list of the cards associated with the player
        for player in self.players:
            playerFrame = tk.Frame(self.playersFrame, borderwidth = 3, relief = "solid")
            playerFrame.pack(side = tk.LEFT)

            #label with players name
            tk.Label(playerFrame, bg=labelBG, text=player.getName(), width = 9, font = (labelFont, labelFontSize)).pack(side=tk.TOP, fill="x")
            #listbox for the players verified cards
            playerVerifiedCardList = tk.Listbox(playerFrame, justify = tk.LEFT, font = (listFont, listFontSize), bg=self.mainAppBgColor, fg=listFontColor, height=3)
            playerVerifiedCardList.pack(side = tk.TOP)
            for card in player.getVerifiedCards():
                text = card.getName() + " - Verified"
                playerVerifiedCardList.insert(tk.END, text)
            #listbox for the players possible cards
            playerPossibleCardList = tk.Listbox(playerFrame, justify = tk.LEFT, font = (listFont, listFontSize), bg=self.mainAppBgColor, fg=listFontColor, height=15)
            playerPossibleCardList.pack(side = tk.TOP)
            for card in player.getCards():
                text = card.getName() + " - " + str(card.getOccurrence())
                playerPossibleCardList.insert(tk.END, text)

    #removes the players lists so that we can dispaly it again with updated values
    def destroyPlayers(self):
        for child in self.playersFrame.winfo_children():
            child.destroy()

    #adds the selected cards to the selected players
    def addToPlayer(self):
        suspectCard = self.rbVars["suspectVar"].get()
        weaponCard = self.rbVars["weaponVar"].get()
        roomCard = self.rbVars["roomVar"].get()

        for player in self.players:
            if self.playerVars[player.getName()].get() == 1:  
                if suspectCard != "":
                    player.addCard(suspectCard)
                if weaponCard != "":
                    player.addCard(weaponCard)
                if roomCard != "":
                    player.addCard(roomCard)

                self.playerVars[player.getName()].set(0)
                

        self.destroyPlayers()
        self.updatePlayers()

        for var in self.rbVars:
            self.rbVars[var].set("")

    #LEGACY
    #function called which will handle the gui for the wining card list.  This shows the available cards and their % of being a winning card
    def updateWinningLists(self):
        #side they will align with. Using variable for easy changing later on
        textSide = tk.LEFT
        textFont = "Helvetica"
        textSize = 20
        textColor = "#bcc8c9"

        #the following 3 sections will create the list, loop through teh cards and add the text
        suspectList = tk.Listbox(self.resultsFrame, justify=tk.LEFT, font=(textFont, textSize), bg=self.mainAppBgColor, fg=textColor)
        suspectList.pack(side = textSide)
        for suspect in self.suspects:
            text = str(suspect.getChance()) + "% - " + suspect.getName()
            suspectList.insert(tk.END, text)

        weaponList = tk.Listbox(self.resultsFrame, justify=tk.LEFT, font=(textFont, textSize), bg=self.mainAppBgColor, fg=textColor)
        weaponList.pack(side = textSide)
        for weapon in self.weapons:
            text = str(weapon.getChance()) + "% - " + weapon.getName()
            weaponList.insert(tk.END, text)

        roomList = tk.Listbox(self.resultsFrame, justify=tk.LEFT, font=(textFont, textSize), bg=self.mainAppBgColor, fg=textColor)
        roomList.pack(side = textSide)
        for room in self.rooms:
            text = str(room.getChance()) + "% - " + room.getName()
            roomList.insert(tk.END, text)
    
    #LEGACY
    #simple method to clear the lists before we add the updated ones back
    def destroyWinningLists(self):
        for child in self.resultsFrame.winfo_children():
            child.destroy()
    
    #LEGACY
    #simple method to loop through each remaining card and update their win %
    def updateCardWinningChance(self):
        suspectSize = len(self.suspects)
        weaponSize = len(self.weapons)
        roomSize = len(self.rooms)

        for i in range(suspectSize):
            self.suspects[i].setChance(int(100 / suspectSize))

        for i in range(weaponSize):
            self.weapons[i].setChance(int(100 / weaponSize))

        for i in range(roomSize):
            self.rooms[i].setChance(int(100 / roomSize))

    #if you see a specific card on a player you can use this function to verify that card on the player.  It will add the card to the players
    #verified list
    def verifyCardOnPlayer(self):
        suspectCard = self.rbVars["suspectVar"].get()
        weaponCard = self.rbVars["weaponVar"].get()
        roomCard = self.rbVars["roomVar"].get()

        for player in self.players:
            if self.playerVars[player.getName()].get() == 1:  
                if suspectCard != "":
                    self.eliminateCard("suspect", suspectCard)
                    player.verifyCard(suspectCard)
                    self.playerVars[player.getName()].set(0)
                    break
                elif weaponCard != "":
                    self.eliminateCard("weapon", weaponCard)
                    player.verifyCard(weaponCard)
                    self.playerVars[player.getName()].set(0)
                    break
                elif roomCard != "":
                    self.eliminateCard("room", roomCard)
                    player.verifyCard(roomCard)
                    self.playerVars[player.getName()].set(0)
                    break
        
        self.destroyPlayers()
        self.updatePlayers()
        self.clearSelections()
                
    #clears all of the selected cards and/or players
    def clearSelections(self):
        self.rbVars["suspectVar"].set("")
        self.rbVars["weaponVar"].set("")
        self.rbVars["roomVar"].set("")

        for player in self.players:
            self.playerVars[player.getName()].set(0)

    #basic init to create the global variables for the three sets of cards
    def initCards(self):
        self.suspects, self.weapons, self.rooms= card_handler.loadCards()

    #basic init to create all of the player classes of people playing the game
    def initPlayers(self):
        self.players = card_handler.initPlayers()

        #vars for the player checkboxes
        self.playerVars = {}
        for player in self.players:
            self.playerVars[player.getName()] = tk.IntVar()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

#TODO: When we verify a card it needs to be removed from all other players as well.
#TODO: Increase width slightly on listboxes