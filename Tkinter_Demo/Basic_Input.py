#Creating a basic GUI input
#Everything is widget in tkinter

from tkinter import *

root = Tk()

#Taking the input from the user
user_input = Entry(root,width = 50,bg="pink",fg="blue")

#Insert default text in the input box
user_input.insert(0,"Enter your name---")
user_input.pack()

def onClick():
    mesg = "Welcome " + user_input.get()        #Gets the input and displays on screen
    label = Label(root,text=mesg,bg="orange")
    label.pack()

#Creating a Label widget
my_button = Button(root,text="Click Me!!!",state="active",fg="red",bg="yellow",padx=20,pady=20,command=onClick)

#Putting it on to a screen
my_button.pack()

#Loop that keeps on running to show the screen output
root.mainloop()