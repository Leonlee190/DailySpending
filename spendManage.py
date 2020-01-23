import tkinter as tk

win = tk.Tk()

myLabel = tk.Label(win, text="Hey this is my first tkinter!")
myLabel.grid(row=0, column=2)

win.mainloop()