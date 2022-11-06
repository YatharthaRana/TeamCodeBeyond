# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("1280x1024")




label2 = Label( root, text = "ENCRYPTION",font=("Arial Black",30),fg="RED")
label2.pack(pady = 10)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )




def display_text():
   global entry
   string= entry.get()
   label2.configure(text=string)
#Initialize a Label to display the User Input
label2=Label(root, text="ENTER TEXT", font=("Courier 22 bold"))
label2.pack()

#Create an Entry widget to accept User Input
entry2= Entry(root, width= 40)
entry2.focus_set()
entry2.pack()


def display_text():
   global entry
   string= entry.get()
   label3.configure(text=string)
#Initialize a Label to display the User Input
label3=Label(root, text="SAMPLE SIZE", font=("Courier 22 bold"))
label3.pack()

#Create an Entry widget to accept User Input
entry3= Entry(root, width= 40)
entry3.focus_set()
entry3.pack()
# Execute tkinter
root.mainloop()