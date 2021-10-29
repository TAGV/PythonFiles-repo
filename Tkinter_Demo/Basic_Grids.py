#Creating a basic GUI grids

from tkinter import *

root = Tk()

#Creating a Label widget
my_label_1 = Label(root,text="Hello World!!!!")
my_label_2 = Label(root,text="Welcome to Python!!!")
my_label_3 = Label(root,text="                       ")

#Putting it on to a screen
my_label_1.grid(row=0,column=0)
my_label_2.grid(row=1,column=10)
my_label_3.grid(row=10,column=5)

#Loop that keeps on running to show the screen output
root.mainloop()