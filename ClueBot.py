import tkinter as tk
from cards import card_handler

suspects, weapons, rooms = card_handler.loadCards()

for s in suspects:
    print(s.getName())

for w in weapons:
    print(w.getName())

for r in rooms:
    print(r.getName())

#root = tk.Tk()

#root.mainloop()