import tkinter as tk
from cards import card_handler

class MainApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        #this line is so we can use root as the base frame to easier understand the frame layouts
        root = self
        suspects, weapons, rooms = card_handler.loadCards()

        #Frame that holds the suspects, weapons and rooms ----------------
        swrFrameBG = "black"
        swrFrame = tk.Frame(root, bg=swrFrameBG, borderwidth = 5, relief = "solid")
        swrFrame.pack()

        #button to remove the selected options
        tk.Button(swrFrame, text="remove", command = self.removeFunction).pack(side=tk.BOTTOM, fill="x")

        #suspect section
        suspectVar = tk.StringVar()
        suspectBG = "#8bf7ec"
        suspectFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
        suspectFrame.pack(side = tk.LEFT, fill="y")
        for suspect in suspects:
            tk.Radiobutton(suspectFrame, text = suspect.getName(), variable = suspectVar, value = suspect.getName(), bg=suspectBG, indicatoron = 0).pack(fill="x")

        #weapon section
        weaponVar = tk.StringVar()
        weaponsBG = "#e18bf7"
        weaponFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
        weaponFrame.pack(side = tk.LEFT, fill="y")
        for weapon in weapons:
            tk.Radiobutton(weaponFrame, text = weapon.getName(), variable = weaponVar, value = weapon.getName(), bg=weaponsBG, indicatoron = 0).pack(fill="x")


        #room section
        roomVar = tk.StringVar()
        roomBG = "#bcf78b"
        roomFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
        roomFrame.pack(side = tk.LEFT, fill="y")

        for room in rooms:
            tk.Radiobutton(roomFrame, text = room.getName(), variable = roomVar, value = room.getName(), bg=roomBG, indicatoron = 0).pack(fill="x")

        #------------------------------------------------------------------------------------------------------------

        #Frame that will show the possible winning cards
        resultsFrame = tk.Frame(root, bg="black", borderwidth = 1, relief = "groove")
        resultsFrame.pack(side = tk.BOTTOM)

        suspectList = tk.Listbox(resultsFrame)
        suspectList.pack(side = tk.LEFT)
        for suspect in suspects:
            suspectList.insert(tk.END, suspect.getName())

        weaponList = tk.Listbox(resultsFrame)
        weaponList.pack(side = tk.LEFT)
        for weapon in weapons:
            weaponList.insert(tk.END, weapon.getName())

        roomList = tk.Listbox(resultsFrame)
        roomList.pack(side = tk.LEFT)
        for room in rooms:
            roomList.insert(tk.END, room.getName())

    def removeFunction(self):
            pass

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()





#suspects, weapons, rooms = card_handler.loadCards()