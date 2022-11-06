# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("1280x1024")




label2 = Label( root, text = "HACKET",font=("Arial Black",30),fg="orange")
label2.pack(pady = 10)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )

# Add buttons
btn1 = Button( frame1, text = "DECRYPTER",font=("Arial Black",10),height=5,width=20,bg="black",fg="yellow")
# btn1.pack(padx= 10,pady = 250)
# btn1.pack( ,side=LEFT, padx=15, pady=30)
# btn1.place(x=25, y=10)
btn1.grid(row=0, column=0,  padx=(800,6), pady=(350))


btn2 = Button( frame1, text = "ENCRYPTER",font=("Arial Black",10),height=5,width=20,bg="black",fg="blue")
# btn2.pack(pady = 20)
# btn2.pack(side=RIGHT, padx=15, pady=20)
btn2.grid(row=0, column=0, padx=(6,800), pady=(350))


btn3 = Button( frame1, text = "CLASSIFIER",font=("Arial Black",10),height=5,width=20,bg="black",fg="GREEN")
# btn2.pack(pady = 20)
# btn2.pack(side=RIGHT, padx=15, pady=20)
btn3.grid(row=0, column=0, pady=(350))

# Execute tkinter
root.mainloop()