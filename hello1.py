#making buttons functional and adding colours


from tkinter import *
root = Tk()
def myClick():
	myLabel = Label(root, text="hey! go fuck yourself!")
	myLabel.pack()
myButton = Button(root, text="click me", command=myClick, fg="blue", bg="black")
myButton.pack()
root.mainloop()
