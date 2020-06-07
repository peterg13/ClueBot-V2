import tkinter as tk
from cards import card_handler

root = tk.Tk()

swrFrameBG = "black"
swrFrame = tk.Frame(root, bg=swrFrameBG, borderwidth = 5, relief = "solid")
swrFrame.pack()


#suspect section
suspectVar = tk.StringVar()
suspectBG = "#8bf7ec"
suspectFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
suspectFrame.pack(side = tk.LEFT, fill="y")
tk.Radiobutton(suspectFrame, text = "mrs. white", variable = suspectVar, value = "mrs. white", bg=suspectBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(suspectFrame, text = "mrs. peacock", variable = suspectVar, value = "mrs. peacock", bg=suspectBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(suspectFrame, text = "miss scarlet", variable = suspectVar, value = "miss scarlet", bg=suspectBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(suspectFrame, text = "colonel mustard", variable = suspectVar, value = "colonel mustard", bg=suspectBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(suspectFrame, text = "mr. green", variable = suspectVar, value = "mr. green", bg=suspectBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(suspectFrame, text = "professor plum", variable = suspectVar, value = "professor plum", bg=suspectBG, indicatoron = 0).pack(fill="x")

#weapon section
weaponVar = tk.StringVar()
weaponsBG = "#e18bf7"
weaponFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
weaponFrame.pack(side = tk.LEFT, fill="y")
tk.Radiobutton(weaponFrame, text = "candlestick", variable = weaponVar, value = "candlestick", bg=weaponsBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(weaponFrame, text = "revolver", variable = weaponVar, value = "revolver", bg=weaponsBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(weaponFrame, text = "rope", variable = weaponVar, value = "rope", bg=weaponsBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(weaponFrame, text = "wrench", variable = weaponVar, value = "wrench", bg=weaponsBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(weaponFrame, text = "leadpipe", variable = weaponVar, value = "leadpipe", bg=weaponsBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(weaponFrame, text = "knife", variable = weaponVar, value = "knife", bg=weaponsBG, indicatoron = 0).pack(fill="x")

#room section
roomVar = tk.StringVar()
roomBG = "#bcf78b"
roomFrame = tk.Frame(swrFrame, bg=swrFrameBG, borderwidth = 1, relief = "groove")
roomFrame.pack(side = tk.LEFT, fill="y")
tk.Radiobutton(roomFrame, text = "study", variable = roomVar, value = "study", bg=roomBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(roomFrame, text = "library", variable = roomVar, value = "library", bg=roomBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(roomFrame, text = "conservatory", variable = roomVar, value = "conservatory", bg=roomBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(roomFrame, text = "hall", variable = roomVar, value = "hall", bg=roomBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(roomFrame, text = "kitchen", variable = roomVar, value = "kitchen", bg=roomBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(roomFrame, text = "ballroom", variable = roomVar, value = "ballroom", bg=roomBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(roomFrame, text = "dining room", variable = roomVar, value = "dining room", bg=roomBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(roomFrame, text = "lounge", variable = roomVar, value = "lounge", bg=roomBG, indicatoron = 0).pack(fill="x")
tk.Radiobutton(roomFrame, text = "billiard room", variable = roomVar, value = "billiard room", bg=roomBG, indicatoron = 0).pack(fill="x")



root.mainloop()





#suspects, weapons, rooms = card_handler.loadCards()