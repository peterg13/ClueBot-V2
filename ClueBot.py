import tkinter as tk
from cards import card_handler

suspects, weapons, rooms = card_handler.loadCards()

root = tk.Tk()

def removeFunction():
    pass
#Frame that holds the suspects, weapons and rooms ----------------
swrFrameBG = "black"
swrFrame = tk.Frame(root, bg=swrFrameBG, borderwidth = 5, relief = "solid")
swrFrame.pack()

#button to remove the selected options
tk.Button(swrFrame, text="remove", command=removeFunction).pack(side=tk.BOTTOM, fill="x")

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




root.mainloop()





#suspects, weapons, rooms = card_handler.loadCards()