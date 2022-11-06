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

![WhatsApp Image 2022-11-06 at 16 01 17](https://user-images.githubusercontent.com/95047694/200167012-332fd727-7b99-4ea6-81ef-82d4a4556d18.jpeg)

DESCRIPTION OF ENCRYPTOR: QDECC uses BB84 Protocol to encrypt the data. It start with accepting the message and then converting into bits and then chooses random basis for each bit. It is then encoded into qubits using the basis. This means the qubits are chosen randomly. This is send over a network and is recieved by the reciever. If someone trys to intercept the data in between the qubits will get changed and the reciever will get to know that the qubits got changed. 

<img width="574" alt="Screenshot 2022-11-06 at 16 24 36" src="https://user-images.githubusercontent.com/95047694/200166713-475ef949-9427-4cb0-acb3-5ca64b041890.png">
<img width="437" alt="Screenshot 2022-11-06 at 16 24 52" src="https://user-images.githubusercontent.com/95047694/200166714-cde39432-b285-4335-8f84-4a1f4d89121c.png">
<img width="1440" alt="Screenshot 2022-11-06 at 16 25 06" src="https://user-images.githubusercontent.com/95047694/200166717-fe9e413e-963d-48c1-a8f3-2e8d99b0f433.png"><img width="414" alt="Screenshot 2022-11-06 at 16 25 18" src="https://user-images.githubusercontent.com/95047694/200166718-bbdb053e-ba6c-425b-829f-85d5a83b7f76.png">

#FRONTEND
![Screenshot (30)](https://user-images.githubusercontent.com/95047694/200166995-659ef915-6ca5-4a60-bdf3-90b0e154db75.png)
![Screenshot (31)](https://user-images.githubusercontent.com/95047694/200166996-7c231a7b-f5f4-41db-bca6-dbbd29a34dde.png)
![Screenshot (32)](https://user-images.githubusercontent.com/95047694/200167003-65dd6962-2ac4-4476-9802-db3582e3e505.png)
![Screenshot (33)](https://user-images.githubusercontent.com/95047694/200167004-51953026-c6fc-4a1b-a224-c7e45a37dc09.png)
