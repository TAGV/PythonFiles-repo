#Creating a basic GUI button
#Everything is widget in tkinter

from tkinter import *

root = Tk()

def onClick():
    label = Label(root,text="Happy Birthday!!!Enjoy!!!")
    label.pack()

#Creating a Label widget
my_button = Button(root,text="Click Me!!!",state="active",fg="red",bg="yellow",padx=20,pady=20,command=onClick)

#Putting it on to a screen
my_button.pack()

#Loop that keeps on running to show the screen output
root.mainloop()