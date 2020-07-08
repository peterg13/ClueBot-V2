import tkinter as tk
from cards import card_handler

class MainApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        #this line is so we can use root as the base frame to easier understand the frame layouts
        root = self
        root.config(bg='#292929')
        root.title("ClueBot - V2")

        self.suspects, self.weapons, self.rooms= card_handler.loadCards()

        #Frame that holds the suspects, weapons and rooms ----------------
        swrFrameBG = "#292929"
        swrFrame = tk.Frame(root, bg=swrFrameBG)
        swrFrame.pack()

        #variables that get passed to the remove button.  These variables hold the current radio button selection.  
        #Need to declare before the button so it has access to these variables and need to declare the remove button
        #before radiobuttons due to formatting issues.
        self.rbVars = {
            "suspectVar" : tk.StringVar(),
            "weaponVar" : tk.StringVar(),
            "roomVar" : tk.StringVar()
        }

        #button to remove the selected options
        tk.Button(swrFrame, text="remove", command = lambda : self.removeFunction(), bg="#b3b3b3").pack(side=tk.BOTTOM, fill="x")

        #suspect section
        suspectFrame = tk.Frame(swrFrame, bg=swrFrameBG)
        suspectFrame.pack(side = tk.LEFT, fill="y", padx=1)

        #weapon section        
        weaponFrame = tk.Frame(swrFrame, bg=swrFrameBG)
        weaponFrame.pack(side = tk.LEFT, fill="y", padx=1)
        
        #room section        
        roomFrame = tk.Frame(swrFrame, bg=swrFrameBG)
        roomFrame.pack(side = tk.LEFT, fill="y", padx=1)

        self.rbFrames = {
            "suspectFrame" : suspectFrame,
            "weaponFrame" : weaponFrame,
            "roomFrame" : roomFrame
        }
        
        #creates the radiobutton GUI
        self.updateRadioButtons()

        #------------------------------------------------------------------------------------------------------------

        #Frame that will show the possible winning cards along with their percentage for being a winning card
        self.resultsFrame = tk.Frame(root, bg="black", borderwidth = 1, relief = "groove")
        self.resultsFrame.pack(side = tk.BOTTOM)

        #creates the ListBoxes GUI that shows the winning cards
        self.updateWinningLists()


    #function that gets called when the remove button gets click.  This will take the selections from the radio buttons, remove them from our saved
    #list of active cards and update the radiobutton list/chance list
    def removeFunction(self):
        #the following 3 loops will go through the three lists of cards and remove them from the radio buttons.
        for i in range(len(self.suspects)):
            if self.suspects[i].getName() == self.rbVars["suspectVar"].get():
                self.destroyRadioButton("suspect", self.suspects[i].getName())
                self.suspects.pop(i)
                break
        for i in range(len(self.weapons)):
            if self.weapons[i].getName() == self.rbVars["weaponVar"].get():
                self.destroyRadioButton("weapon", self.weapons[i].getName())
                self.weapons.pop(i)
                break
        for i in range(len(self.rooms)):
            if self.rooms[i].getName() == self.rbVars["roomVar"].get():
                self.destroyRadioButton("room", self.rooms[i].getName())
                self.rooms.pop(i)
                break

        #TODO: update the lists and %
        self.destroyWinningLists()
        self.updateCardWinningChance()
        self.updateWinningLists()
        
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
        buttonColor = "#ff5c87"
        selectColor = "#ffadbf"

        font = "Helvetica"
        fontSize = 15

        labelBG = "#d9c3c3"
        labelFont = "Helvetica"
        labelFontSize = 20
        labelWidth = 15
        labelPadding = 3

        tk.Label(self.rbFrames["suspectFrame"], text = "Suspects", font = (labelFont, labelFontSize, "bold"), bg = labelBG, width = labelWidth).pack(fill="x", pady=labelPadding, padx=labelPadding)
        for suspect in self.suspects:
            tk.Radiobutton(self.rbFrames["suspectFrame"], text = suspect.getName(), variable = self.rbVars["suspectVar"], value = suspect.getName(), bg=buttonColor, selectcolor=selectColor, indicatoron = 0, font=(font, fontSize)).pack(fill="x")
        
        tk.Label(self.rbFrames["weaponFrame"], text = "Weapons", font = (labelFont, labelFontSize, "bold"), bg = labelBG, width = labelWidth).pack(fill="x", pady=labelPadding, padx=labelPadding)
        for weapon in self.weapons:
            tk.Radiobutton(self.rbFrames["weaponFrame"], text = weapon.getName(), variable = self.rbVars["weaponVar"], value = weapon.getName(), bg=buttonColor, selectcolor=selectColor, indicatoron = 0, font=(font, fontSize)).pack(fill="x")

        tk.Label(self.rbFrames["roomFrame"], text = "Rooms", font = (labelFont, labelFontSize, "bold"), bg = labelBG, width = labelWidth).pack(fill="x", pady=labelPadding, padx=labelPadding)
        for room in self.rooms:
            tk.Radiobutton(self.rbFrames["roomFrame"], text = room.getName(), variable = self.rbVars["roomVar"], value = room.getName(), bg=buttonColor, selectcolor=selectColor, indicatoron = 0, font=(font, fontSize)).pack(fill="x")

    def updateWinningLists(self):
        #side they will align with. Using variable for easy changing later on
        textSide = tk.LEFT

        #the following 3 sections will create the list, loop through teh cards and add the text
        suspectList = tk.Listbox(self.resultsFrame)
        suspectList.pack(side = textSide)
        for suspect in self.suspects:
            text = suspect.getName() + " - " + str(suspect.getChance()) + '%'
            suspectList.insert(tk.END, text)

        weaponList = tk.Listbox(self.resultsFrame)
        weaponList.pack(side = textSide)
        for weapon in self.weapons:
            text = weapon.getName() + " - " + str(weapon.getChance()) + '%'
            weaponList.insert(tk.END, text)

        roomList = tk.Listbox(self.resultsFrame)
        roomList.pack(side = textSide)
        for room in self.rooms:
            text = room.getName() + " - " + str(room.getChance()) + '%'
            roomList.insert(tk.END, text)

    #simple method to clear the lists before we add the updated ones back
    def destroyWinningLists(self):
        for child in self.resultsFrame.winfo_children():
            child.destroy()

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



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()




#color pallet
#dark blue - #173f5f
#blue      - #20639b
#teal      - #3caea3
#yellow    - #f6d55c
#red       - #ed553b