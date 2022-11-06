# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("1280x1024")




label2 = Label( root, text = "ClASSIFIER",font=("Arial Black",30),fg="blue")
label2.pack(pady = 10)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )


def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(root, text="Enter the string", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(root, width= 40)
entry.focus_set()
entry.pack()


# Execute tkinter
root.mainloop()