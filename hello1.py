#creating inpuit feild

from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
def myClick():
	myLabel = Label(root, text="Hello " + e.get())
	myLabel.pack()
myButton = Button(root, text="enter your name", command=myClick, fg="blue", bg="black")
myButton.pack()
root.mainloop()
