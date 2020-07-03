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
        suspectVar = tk.StringVar()
        weaponVar = tk.StringVar()
        roomVar = tk.StringVar()

        #button to remove the selected options
        tk.Button(swrFrame, text="remove", command = lambda : self.removeFunction(suspectVar, weaponVar, roomVar)).pack(side=tk.BOTTOM, fill="x")

        #suspect section
        suspectBG = "#8bf7ec"
        suspectFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
        suspectFrame.pack(side = tk.LEFT, fill="y")
        for suspect in self.suspects:
            tk.Radiobutton(suspectFrame, text = suspect.getName(), variable = suspectVar, value = suspect.getName(), bg=suspectBG, indicatoron = 0).pack(fill="x")

        #weapon section        
        weaponsBG = "#e18bf7"
        weaponFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
        weaponFrame.pack(side = tk.LEFT, fill="y")
        for weapon in self.weapons:
            tk.Radiobutton(weaponFrame, text = weapon.getName(), variable = weaponVar, value = weapon.getName(), bg=weaponsBG, indicatoron = 0).pack(fill="x")


        #room section        
        roomBG = "#bcf78b"
        roomFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
        roomFrame.pack(side = tk.LEFT, fill="y")
        for room in self.rooms:
            tk.Radiobutton(roomFrame, text = room.getName(), variable = roomVar, value = room.getName(), bg=roomBG, indicatoron = 0).pack(fill="x")

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
    def removeFunction(self, suspectVar, weaponVar, roomVar):
        #the following 3 loops will go through the three lists of cards and remove them.
        for i in range(len(self.suspects)):
            if self.suspects[i].getName() == suspectVar.get():
                self.suspects.pop(i)
                break
        for i in range(len(self.weapons)):
            if self.weapons[i].getName() == weaponVar.get():
                self.weapons.pop(i)
                break
        for i in range(len(self.rooms)):
            if self.rooms[i].getName() == roomVar.get():
                self.rooms.pop(i)
                break

        #once we update the lists we need to update the GUI

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()