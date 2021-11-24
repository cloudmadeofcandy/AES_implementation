#I would like to thank the former mathematicians, the programmers that worked tirelessly to come up with these
#methods to obfuscate data under such strenuous ways, in order to protect information from being stolen.

# Book: The Design of Rijndael - https://cs.ru.nl/~joan/papers/JDA_VRI_Rijndael_2002.pdf

# https://crypto.stackexchange.com/questions/2569/how-does-one-implement-the-inverse-of-aes-mixcolumns
# https://en.wikipedia.org/wiki/Rijndael_S-box
# https://en.wikipedia.org/wiki/Rijndael_MixColumns
# https://en.wikipedia.org/wiki/AES_key_schedule

# On the theory of Galois Field GF(2^8) and how it applies in said situation:
# https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture5.pdf
# https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture6.pdf
# https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture7.pdf
# https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture8.pdf

# On the overall mechanism of AES Encryption:
# https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.197.pdf
# https://formaestudio.com/rijndaelinspector/archivos/Rijndael_Animation_v4_eng-html5.html
# https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
# https://crypto.stackexchange.com/questions/2569/how-does-one-implement-the-inverse-of-aes-mixcolumns
# https://crypto.stackexchange.com/questions/51951/aes-key-expansion-for-192-bit

# FOR CHECKING THE CORRECTNESS OF AES:
# https://formaestudio.com/rijndaelinspector/archivos/Rijndael_Animation_v4_eng-html5.html
# https://github.com/chrisveness/crypto/blob/master/test/aes-tests.js