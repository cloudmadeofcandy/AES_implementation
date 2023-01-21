# AES_implementation

~~If you wish to encrypt or decrypt strings, I did push the app onto heroku :3~~

~~link: http://floating-ridge-18343.herokuapp.com/~~

Since December 2022, Heroku now no longer allow free dynos, subsequently every app on Heroku free plan are defuncted.

I have deployed the app on Vercel. link: https://quansaesimplementation.vercel.app/

AES Encryption and Decryption implementation for CT303 - Basis of Information Integrity and Security - Academy of Cryptography Techniques.

To use the program, please pay attention to the 2 functions/APIs in file AES.py.

The function aesEncrypt(state, cypherkey), takes 2 arguments: 
  - state: a plaintext of unknown length.
  - cypherkey: another string, serves as the input for the keyExpansion stage.

The function should return a cyphertext.

The function aesDecrypt(state, cypherkey), takes 2 arguments: 
  - state: a plaintext of unknown length.
  - cypherkey: another string, serves as the input for the keyExpansion stage.

The function should return the plaintext.


"Quân muốn đi chơi, ai đưa Quân đi chơi thì Quân sẽ rất hạnh phúc :3"
