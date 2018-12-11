"""
Playfair Cipher는 Substitution cipher(대처법)중 하나로
대처법이란 '해당 글자를 다른 글자로 대체하여 암호화하는 방법'이다.
​1854년 찰스 휘트스톤(Charles Wheatstone)이라는 사람이 맨처음 만들었는데 
맨처음 나왔을 당시 사용이 너무 어렵다는 이유로 사용이 되지 않다가
라이언 플레이페어(Lyon Playfair)라는 사람을 통해 널리 알려졌다고 한다.
[출처] Playfair Cipher|작성자 훔친거
암호화 하는 방법
먼저 5 X 5 대형으로 

A-Z까지 쓰고

I와 J는 같은 곳에 놓이며

제시어를 맨 앞에 적는다

복호화 하는 방법
Keyword가 = 'playfair example'로 주어졌다
그러면 위에 설명과 같이 일단 playfair example을 적는다
연속되는 절자가 없으므로 그냥 일단 적는다 5 X 5 대형으로
P L A Y F

I R E X M
이때 여기서 중복되는 철자는 적지 않는다.
그리고 A-Z중 쓰지 않은 철자를 적으면 된다.

P L A Y F

I R E X M

B C D G H

K N O Q S

T U V W Z
가 되는 것 이다.
"""import string
import itertools

def chunker(seq, size):
    it = iter(seq)
    while True:
       chunk = tuple(itertools.islice(it, size))
       if not chunk:
           return
       yield chunk



def prepare_input(dirty):
    """
    Prepare the plaintext by up-casing it
    and separating repeated letters with X's
    """
    
    dirty = ''.join([c.upper() for c in dirty if c in string.ascii_letters])
    clean = ""
    
    if len(dirty) < 2:
        return dirty

    for i in range(len(dirty)-1):
        clean += dirty[i]
        
        if dirty[i] == dirty[i+1]:
            clean += 'X'
    
    clean += dirty[-1]

    if len(clean) & 1:
        clean += 'X'

    return clean

def generate_table(key):

    # I and J are used interchangeably to allow
    # us to use a 5x5 table (25 letters)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # we're using a list instead of a '2d' array because it makes the math 
    # for setting up the table and doing the actual encoding/decoding simpler
    table = []

    # copy key chars into the table if they are in `alphabet` ignoring duplicates
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    # fill the rest of the table in with the remaining alphabet chars
    for char in alphabet:
        if char not in table:
            table.append(char)

    return table

def encode(plaintext, key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""

    # https://en.wikipedia.org/wiki/Playfair_cipher#Description
    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            ciphertext += table[row1*5+(col1+1)%5]
            ciphertext += table[row2*5+(col2+1)%5]
        elif col1 == col2:
            ciphertext += table[((row1+1)%5)*5+col1]
            ciphertext += table[((row2+1)%5)*5+col2]
        else: # rectangle
            ciphertext += table[row1*5+col2]
            ciphertext += table[row2*5+col1]

    return ciphertext


def decode(ciphertext, key):
    table = generate_table(key)
    plaintext = ""

    # https://en.wikipedia.org/wiki/Playfair_cipher#Description
    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            plaintext += table[row1*5+(col1-1)%5]
            plaintext += table[row2*5+(col2-1)%5]
        elif col1 == col2:
            plaintext += table[((row1-1)%5)*5+col1]
            plaintext += table[((row2-1)%5)*5+col2]
        else: # rectangle
            plaintext += table[row1*5+col2]
            plaintext += table[row2*5+col1]

    return plaintext
