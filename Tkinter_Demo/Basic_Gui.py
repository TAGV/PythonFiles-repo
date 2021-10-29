#Creating a basic GUI window
#Everything is widget in tkinter

from tkinter import *

root = Tk()

#Creating a Label widget
my_label = Label(root,text="Welcome to Python!!!")

#Putting it on to a screen
my_label.pack()

#Loop that keeps on running to show the screen output
root.mainloop()