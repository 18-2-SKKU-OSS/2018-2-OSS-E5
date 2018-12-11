"""
전치 암호(Transposition Cipher)는 치환 암호(Substitution Cipher)와 다르게 
특정 글자를 다른 글자로 치환하지 않는다. 그 대신 글자들의 순서를 변경하여 암호화한다. 
예를 들어 Plaintext의 첫 글자와 열 번째 글자를 바꾸고, 두 번째 글자를 다섯 번째와 바꿔서 암호화할 수 있다. 
이렇게 단순히 순서를 변경하는 것만으로도, Ciphertext로부터 Plaintext를 한눈에 알기는 어려워진다. 
Transposition Cipher는 이러한 점을 이용해서 위치 변경의 규칙을 정하고, 그 규칙에 맞추어 Plaintext를 암호화한다. 
복호화는 어렵지 않다. 암호화한 규칙을 역으로 Ciphertext로부터 Plaintext를 찾을 수 있을 것이다. 
간단히, Transpositon Chipher는 문자들을 재순서한다고 생각하면 된다.

출처: http://ieatt.tistory.com/27 [IeatT]
"""
from __future__ import print_function
import math

def main():
    message = input('Enter message: ')
    key = int(input('Enter key [2-%s]: ' % (len(message) - 1)))
    mode = input('Encryption/Decryption [e/d]: ')

    if mode.lower().startswith('e'):
        text = encryptMessage(key, message)
    elif mode.lower().startswith('d'):
        text = decryptMessage(key, message)

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print('Output:\n%s' %(text + '|'))

def encryptMessage(key, message):
    """
    >>> encryptMessage(6, 'Harshil Darji')
    'Hlia rDsahrij'
    """
    cipherText = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return ''.join(cipherText)

def decryptMessage(key, message):
    """
    >>> decryptMessage(6, 'Hlia rDsahrij')
    'Harshil Darji'
    """
    numCols = math.ceil(len(message) / key)
    numRows = key
    numShadedBoxes = (numCols * numRows) - len(message)
    plainText = [""] * numCols
    col = 0; row = 0;

    for symbol in message:
        plainText[col] += symbol
        col += 1

        if (col == numCols) or (col == numCols - 1) and (row >= numRows - numShadedBoxes):
            col = 0
            row += 1

    return "".join(plainText)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
