from tkinter import *
import webscrap
def clicked():
    userJob = textBox.get()
    webscrap.scrapeTheWeb(userJob)

window = Tk()
window.title("FACK")
window.geometry("350x200")
window.configure(background = "orange")

label = Label(window,text  = "Please enter the desired profession: ")
label.configure(background = "pink")
label.grid(column = 0, row = 0)

textBox = Entry(master = window)
textBox.grid(column = 1, row = 0)

button = Button(master = window, text = "SEARCH", command = clicked)
button.configure(background = "pink")
button.grid(column = 0, row = 1)
window.mainloop()

