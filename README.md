# AES_implementation
AES Encryption and Decryption implementation for CT303 - Basis of Information Integrity and Security - Academy of Cryptography Techniques
To use the program, please pay attention to 2 functions/APIs in file AES.py
The function aesEncrypt(state, cypherkey), takes 2 arguments: 
  - state: a 4 x 4 matrix created from the plaintext.
  - cypherkey: another 4 x 4 matrix, serves as the input for the keyExpansion stage.
The function should return a 4 x 4 matrix interpretation of the cyphertext, which then can be composed into a string.

The function aesDecrypt(state, cypherkey), takes 2 arguments: 
  - state: a 4 x 4 matrix created from the cyphertext.
  - cypherkey: another 4 x 4 matrix, serves as the input for the keyExpansion stage.
The function should return a 4 x 4 matrix interpretation of the plaintext, which then can be composed into a string.

"Quân muốn đi chơi, ai đưa Quân đi chơi thì Quân sẽ rất hạnh phúc :3"
