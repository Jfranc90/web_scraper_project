from tkinter import *

def clicked():
    userJob = textBox.get()
    

window = Tk()
window.title("FACK")
window.geometry("350x200")

label = Label(window,text  = "Please enter the desired profession: ")
label.grid(column = 0, row = 0)

textBox = Entry(master = window)
textBox.grid(column = 1, row = 0)

button = Button(master = window, text = "PARENT", command = clicked)
button.grid(column = 0, row = 1)
window.mainloop()

