"""
로마에서 장군으로 활약한 카이사르가 썼던 암호로, 평행이동이라는 방법을 사용하여 암호화한다.
기원전 100년경에 로마의 장군 카이사르가 썼던 암호로, 시저 암호라고도 불린다. 
그 당시 '암살자를 조심하라 Be careful for assassinator'라는 암호문을 전달하기 위해 사용되었다고 한다.

이 암호는 평문에서 사용되고 있는 알파벳을 암호키 k개만큼 평행이동시켜 암호화하는 '치환 암호'이다. 
간단한 방법으로 암호화하기 때문에 암호키만 알게 되면 쉽게 암호를 복호화(암호를 해독하는 것) 할 수 있다는 단점이 있다.
알파벳을 평행이동시키는 작업 자체가 암호화 알고리즘이라고 할 수 있다.

예를 들어, 평문 Kabsoonyee가 있으며, 카이사르 암호에 사용되는 암호키는 3이라고 가정하자. 
암호키는 3이므로 알파벳을 3문자 평행이동시킨다. 평행이동시킨 문자에 의해서 평문을 암호화 하면 NDEVRRQBHH이다.
[네이버 지식백과] 카이사르 암호 [Caesar cipher] (두산백과)
"""
import sys
def encrypt(strng, key):
    encrypted = ''
    for x in strng:
        indx = (ord(x) + key) % 256
        if indx > 126:
            indx = indx - 95
        encrypted = encrypted + chr(indx)
    return encrypted


def decrypt(strng, key):
    decrypted = ''
    for x in strng:
        indx = (ord(x) - key) % 256
        if indx < 32:
            indx = indx + 95
        decrypted = decrypted + chr(indx)
    return decrypted

def brute_force(strng):
    key = 1
    decrypted = ''
    while key <= 94:
        for x in strng:
            indx = (ord(x) - key) % 256
            if indx < 32:
                indx = indx + 95
            decrypted = decrypted + chr(indx)
        print("Key: {}\t| Message: {}".format(key, decrypted))
        decrypted = ''
        key += 1
    return None


def main():
    while True:
        print('-' * 10 + "\n**Menu**\n" + '-' * 10)
        print("1.Encrpyt")
        print("2.Decrypt")
        print("3.BruteForce")
        print("4.Quit")
        choice = input("What would you like to do?: ")
        if choice not in ['1', '2', '3', '4']:
            print ("Invalid choice")
        elif choice == '1':
            strng = input("Please enter the string to be ecrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            if key in range(1, 95):
                print (encrypt(strng.lower(), key))
        elif choice == '2':
            strng = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            if key > 0 and key <= 94:
                print(decrypt(strng, key))
        elif choice == '3':
            strng = input("Please enter the string to be decrypted: ")
            brute_force(strng)
            main()
        elif choice == '4':
            print ("Goodbye.")
            break
main()
