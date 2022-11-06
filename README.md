## TeamCodeBeyond
<img width="504" alt="Screenshot 2022-11-04 at 22 31 14" src="https://user-images.githubusercontent.com/95047694/200163871-bced6626-00d6-4806-845f-d5e01fd6a0bb.png">

# What is QDECC ?
Quantum Decryption Encrpytion and Classification of Ciphers (QDECC) is an application for decryption of RSA algorithm, encrption of data and classification of Ciphers using Quantum Computing. It acts as a common platform for performing all these tasks.

This project provides:
-Way to classify Cipher
-Method to decrypt RSA 
-Methond to Encrypt data and detect possible interception

DECRIPTION OF RSA: QDECC uses Shor's algorithm to decript RSA encrypted data , Shor's algorithm can be used to factorize the public key which is a multiple
of two large prime numbers , classical compuetrs can take years to calulate these factors while shor's algorithm uses quantum ciruits to calculate them in 
much less time thus rendering RSA defenseless to it.

DESCRIPTION OF CLASSIFIER: QDECC uses neural network for classifying the ciphers, It utilizes LSTM(Long Short Term Memory) to form a relationship between the inputted sequence, the quantum circuits are used to further process the data and used rotation operator and hadmard gate for processing, softmax algorithm is used to find the probability of data being a particular cipher. Using quantum computing in machine learning decreases the computing time and makes the algorithm run more faster

DESCRIPTION OF ENCRYPTOR: QDECC uses BB84 Protocol to encrypt the data. It start with accepting the message and then converting into bits and then chooses random basis for each bit. It is then encoded into qubits using the basis. This means the qubits are chosen randomly. This is send over a network and is recieved by the reciever. If someone trys to intercept the data in between the qubits will get changed and the reciever will get to know that the qubits got changed. 
