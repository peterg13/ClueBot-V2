import tkinter as tk
from cards import card_handler

class MainApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        #this line is so we can use root as the base frame to easier understand the frame layouts
        root = self
        self.suspects, self.weapons, self.rooms= card_handler.loadCards()

        #Frame that holds the suspects, weapons and rooms ----------------
        swrFrameBG = "black"
        swrFrame = tk.Frame(root, bg=swrFrameBG, borderwidth = 5, relief = "solid")
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
        tk.Button(swrFrame, text="remove", command = lambda : self.removeFunction()).pack(side=tk.BOTTOM, fill="x")

        #suspect section
        suspectFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
        suspectFrame.pack(side = tk.LEFT, fill="y")

        #weapon section        
        weaponFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
        weaponFrame.pack(side = tk.LEFT, fill="y")
        
        #room section        
        roomFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
        roomFrame.pack(side = tk.LEFT, fill="y")

        self.rbFrames = {
            "suspectFrame" : suspectFrame,
            "weaponFrame" : weaponFrame,
            "roomFrame" : roomFrame
        }
        
        self.updateRadioButtons()

        #------------------------------------------------------------------------------------------------------------

        #Frame that will show the possible winning cards along with their percentage for being a winning card
        resultsFrame = tk.Frame(root, bg="black", borderwidth = 1, relief = "groove")
        resultsFrame.pack(side = tk.BOTTOM)

        #side they will align with. Using variable for easy changing later on
        textSide = tk.LEFT

        suspectList = tk.Listbox(resultsFrame)
        suspectList.pack(side = textSide)
        for suspect in self.suspects:
            text = suspect.getName() + " - " + str(suspect.getChance()) + '%'
            suspectList.insert(tk.END, text)

        weaponList = tk.Listbox(resultsFrame)
        weaponList.pack(side = textSide)
        for weapon in self.weapons:
            text = weapon.getName() + " - " + str(weapon.getChance()) + '%'
            weaponList.insert(tk.END, text)

        roomList = tk.Listbox(resultsFrame)
        roomList.pack(side = textSide)
        for room in self.rooms:
            text = room.getName() + " - " + str(room.getChance()) + '%'
            roomList.insert(tk.END, text)

    #function that gets called when the remove button gets click.  This will take the selections from the radio buttons, remove them from our saved
    #list of active cards and update the radiobutton list/chance list
    def removeFunction(self):
        #the following 3 loops will go through the three lists of cards and remove them.
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

        #TODO: update the lists
        
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

    def updateRadioButtons(self):
        #selection colors
        suspectBG = "#8bf7ec"
        weaponsBG = "#e18bf7"
        roomBG = "#bcf78b"

        for suspect in self.suspects:
            tk.Radiobutton(self.rbFrames["suspectFrame"], text = suspect.getName(), variable = self.rbVars["suspectVar"], value = suspect.getName(), bg=suspectBG, indicatoron = 0).pack(fill="x")
        
        for weapon in self.weapons:
            tk.Radiobutton(self.rbFrames["weaponFrame"], text = weapon.getName(), variable = self.rbVars["weaponVar"], value = weapon.getName(), bg=weaponsBG, indicatoron = 0).pack(fill="x")

        for room in self.rooms:
            tk.Radiobutton(self.rbFrames["roomFrame"], text = room.getName(), variable = self.rbVars["roomVar"], value = room.getName(), bg=roomBG, indicatoron = 0).pack(fill="x")

        

    def updateListBoxes(self):
        pass

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()