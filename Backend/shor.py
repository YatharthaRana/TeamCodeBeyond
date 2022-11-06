from qiskit import IBMQ
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor
import numpy as np
from qiskit import QuantumCircuit, Aer , execute
from qiskit.visualization import plot_histogram
import math

publickey=[]
cypher=str(input("Enter Cypher Text. \n "))
print("Enter Public key")
for i in range(0, 2):
    ele = int(input())
    publickey.append(ele)

N=publickey[0]
e=publickey[1]
backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1000) 
my_shor=Shor(quantum_instance=quantum_instance)
result = my_shor.factor(N)
p=result.factors[0][0]
q=result.factors[0][1]

n=1
x=(p-1)*(q-1)
while((x*n+1)% p !=0 ) :
    n+=1
d=(x*n+1)/p
decipher=""
for c in cypher:
  cy=int(c)
  m=int((pow(cy,d))%N)
  decipher+=str(m)
print(decipher)
