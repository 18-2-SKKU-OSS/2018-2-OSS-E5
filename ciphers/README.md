# The Algorithms - Python <!-- [![Build Status](https://travis-ci.org/TheAlgorithms/Python.svg)](https://travis-ci.org/TheAlgorithms/Python) -->

### All algorithms implemented in Python (for education)

These implementations are for demonstration purposes. They are less efficient than the implementations in the Python standard library.

## Ciphers

### Caesar
![alt text][caesar]<br>
**Caesar cipher**, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.<br>
It is **a type of substitution cipher** in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. <br>
The method is named after **Julius Caesar**, who used it in his private correspondence.<br>
The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communication security.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)

### Vigenère
The **Vigenère cipher** is a method of encrypting alphabetic text by using a series of **interwoven Caesar ciphers** based on the letters of a keyword. It is **a form of polyalphabetic substitution**.<br>
The Vigenère cipher has been reinvented many times. The method was originally described by Giovan Battista Bellaso in his 1553 book La cifra del. Sig. Giovan Battista Bellaso; however, the scheme was later misattributed to Blaise de Vigenère in the 19th century, and is now widely known as the "Vigenère cipher".<br>
Though the cipher is easy to understand and implement, for three centuries it resisted all attempts to break it; this earned it the description **le chiffre indéchiffrable**(French for 'the indecipherable cipher').
Many people have tried to implement encryption schemes that are essentially Vigenère ciphers. Friedrich Kasiski was the first to publish a general method of deciphering a Vigenère cipher in 1863.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

### Transposition

In cryptography, a **transposition cipher** is a method of encryption by which the positions held by units of plaintext (which are commonly characters or groups of characters) are shifted according to a regular system, so that the ciphertext constitutes a permutation of the plaintext. That is, the order of the units is changed (the plaintext is reordered).<br>

Mathematically a bijective function is used on the characters' positions to encrypt and an inverse function to decrypt.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/Transposition_cipher)

### RSA (Rivest–Shamir–Adleman)
RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and it is different from the decryption key which is kept secret (private). In RSA, this asymmetry is based on the practical difficulty of the factorization of the product of two large prime numbers, the "factoring problem". The acronym RSA is made of the initial letters of the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who first publicly described the algorithm in 1978. Clifford Cocks, an English mathematician working for the British intelligence agency Government Communications Headquarters (GCHQ), had developed an equivalent system in 1973, but this was not declassified until 1997.

A user of RSA creates and then publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers must be kept secret. Anyone can use the public key to encrypt a message, but with currently published methods, and if the public key is large enough, only someone with knowledge of the prime numbers can decode the message feasibly. Breaking RSA encryption is known as the RSA problem. Whether it is as difficult as the factoring problem remains an open question.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

## ROT13
![alt text][ROT13-image]
ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet. ROT13 is a special case of the Caesar cipher which was developed in ancient Rome.

Because there are 26 letters (2×13) in the basic Latin alphabet, ROT13 is its own inverse; that is, to undo ROT13, the same algorithm is applied, so the same action can be used for encoding and decoding. The algorithm provides virtually no cryptographic security, and is often cited as a canonical example of weak encryption.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/ROT13)

## XOR
In cryptography, the simple XOR cipher is a type of additive cipher, an encryption algorithm that operates according to the principles:

A ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  0 = A,
A ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  A = 0,
(A ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  B) ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  C = A ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  (B ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  C),
(B ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  A) ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  A = B ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  0 = B,
where ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b16e2bdaefee9eed86d866e6eba3ac47c710f60)  denotes the exclusive disjunction (XOR) operation. This operation is sometimes called modulus 2 addition (or subtraction, which is identical). With this logic, a string of text can be encrypted by applying the bitwise XOR operator to every character using a given key. To decrypt the output, merely reapplying the XOR function with the key will remove the cipher.
###### Source: [Wikipedia](https://en.wikipedia.org/wiki/XOR_cipher)



[caesar]: https://upload.wikimedia.org/wikipedia/commons/4/4a/Caesar_cipher_left_shift_of_3.svg "Caesar"

[ROT13-image]: https://upload.wikimedia.org/wikipedia/commons/3/33/ROT13_table_with_example.svg "ROT13"

[JumpSearch-image]: https://i1.wp.com/theoryofprogramming.com/wp-content/uploads/2016/11/jump-search-1.jpg "Jump Search"

[QuickSelect-image]: https://upload.wikimedia.org/wikipedia/commons/0/04/Selecting_quickselect_frames.gif "Quick Select"
