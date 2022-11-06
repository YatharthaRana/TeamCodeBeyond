# Import module
from tkinter import *
from qiskit import IBMQ
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor
import numpy as np
from qiskit import QuantumCircuit, Aer , execute
from qiskit.visualization import plot_histogram
import math

def main():
   # Create object
   root = Tk()

   # Adjust size
   root.geometry("1280x1024")




   label = Label( root, text = "DECRYPTION",font=("Arial Black",30),fg="green")
   label.pack(pady = 10)

   # Create Frame
   frame1 = Frame(root)
   frame1.pack(pady = 20 )


   def display_text():
      global entry
      string= entry.get()
      label.configure(text=string)

   #Initialize a Label to display the User Input
   label1=Label(root, text="Cypher text", font=("Courier 22 bold"))
   label1.pack()

   #Create an Entry widget to accept User Input
   entry1= Entry(root, width= 40)
   entry1.focus_set()
   entry1.pack()


   #Initialize a Label to display the User Input
   label2=Label(root, text="Public key", font=("Courier 22 bold"))
   label2.pack()

   #Create an Entry widget to accept User Input
   entry2= Entry(root, width= 40)
   entry2.focus_set()
   entry2.pack()


  
   #Initialize a Label to display the User Input
   label3=Label(root, text="Deciphered text", font=("Courier 22 bold"))
   label3.pack()

   #Create an Entry widget to accept User Input
   entry3= Entry(root, width= 40)
   entry3.focus_set()
   entry3.pack()
   # Execute tkinter
   cypher=str(entry1.get())
   print("Enter Public key")
   N=15
   e=7
   backend = Aer.get_backend('qasm_simulator')
   quantum_instance = QuantumInstance(backend, shots=1000) 
   my_shor=Shor(quantum_instance=quantum_instance)
   result = my_shor.factor(N)
   p=result.factors[0][0]
   q=result.factors[0][1]

   n=1
   x=(p-1)*(q-1)

   while((x*n+1)% p!=0 ) :
        n+=1
   d=(x*n+1)/p
   decipher=""
   for c in cypher:
      cy=int(c)
      m=int((pow(cy,d))%N)
      decipher+=str(m)
   entry3.insert(END,decipher)
   root.mainloop()
