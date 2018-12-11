"""
치환 암호(Substitution Cipher)는 특정 글자를 다른 글자로 치환함으로서 암호를 생성하는 방법이다. 
예를 들어 알파벳 A를 임의로 H로 지정하듯이 특정 문자를 다른 문자로 치환하면 된다. 
치환 암호에는 크게 두 가지 방법이 있는데, 단일 문자 치환(Monoalphabetic Cipher)과
다중 문자 치환(Polyalphabetic Cipher)가 있다. Monoalphabetic은 항상 한 문자에 대해서는 
같은 문자로 치환 되는 것이다. 예를 들어, 앞서 A를 H로 치환했다면, 하나의 key를 통해 암호화 된 
문서에서 나타나는 모든 H는 Plaintext의 A가 된다. 반면에 Polyalphabetic에서는 
하나의 문자가 여러 다른 문자로 바뀔 수 있다. 즉 Plaintext의 A가 H가 될 수도, Y가 될 수도 있다는 말이다.
이 말은 일반적으로 Polyalphabetic이 Monoalphabetic 방법보다 더욱 알아내기 어렵다고 생각할 수 있다.

출처: http://ieatt.tistory.com/21?category=623923 [IeatT]
"""
from __future__ import print_function
import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = input('Enter message: ')
    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    resp = input('Encrypt/Decrypt [e/d]: ')

    checkValidKey(key)

    if resp.lower().startswith('e'):
        mode = 'encrypt'
        translated = encryptMessage(key, message)
    elif resp.lower().startswith('d'):
        mode = 'decrypt'
        translated = decryptMessage(key, message)

    print('\n%sion: \n%s' % (mode.title(), translated))
    
def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    if keyList != lettersList:
        sys.exit('Error in the key or symbol set.')

def encryptMessage(key, message):
    """
    >>> encryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
    'Ilcrism Olcvs'
    """
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    """
    >>> decryptMessage('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs')
    'Harshil Darji'
    """
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key

    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
        
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol

    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()
