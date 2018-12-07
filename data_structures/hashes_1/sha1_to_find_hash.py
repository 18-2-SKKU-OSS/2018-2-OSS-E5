"""
Python 클래스에서 SHA1 해시 함수를 구현하고 파일에서 
문자열의 해시 또는 텍스트의 해시를 찾는 유틸리티를 제공합니다.
사용법 : python sha1.py --string "Hello World !!"
       pyhton sha1.py - 파일 "hello_world.txt"
       인수없이 실행하면 "Hello World !! Welcome to Cryptography"문자열의 해시를 인쇄합니다.
또한 생성 된 해시가 hashlib 라이브러리에 의해 반환 된 해시와 
동일한 지 확인하는 Test 클래스가 포함되어 있습니다.

문자열의 SHA1 해시 또는 SHA1 합은 crytpographic 함수이므로 
전달을 계산하는 것이 쉽지만 역으로 계산하는 것은 어렵습니다. 
이것이 의미하는 바는 문자열의 해시를 쉽게 계산할 수 있지만 
해시가 있으면 원래 문자열을 아는 것은 매우 어렵습니다. 
이 속성은 안전하게 통신하고, 암호화 된 메시지를 보내며, 지불 시스템, 블록 체인 및 암호 해독 등에 매우 유용합니다.
참조로 설명 된 알고리즘 :
먼저 메시지로 시작합니다. 메시지가 채워지고 메시지의 길이가 끝에 추가됩니다. 
그런 다음 512 비트 또는 64 바이트 블록으로 분할됩니다. 
그런 다음 블록은 한 번에 하나씩 처리됩니다. 각 블록은 확장 및 압축되어야합니다.
각 압축 후 값은 현재 해시 상태라고하는 160 비트 버퍼에 추가됩니다. 
마지막 블록이 처리 된 후 현재 해시 상태가 최종 해시로 반환됩니다.
참조: https://deadhacker.com/2006/02/21/sha-1-illustrated/
"""

import argparse
import struct
import hashlib #hashlib is only used inside the Test class
import unittest


class SHA1Hash:
    """
    SHA1 해싱 알고리즘의 전체 파이프 라인을 포함하는 클래스
    """
    def __init__(self, data):
        """
        변수 data와 h를 시작합니다. h는 5 자리 8 자리 16 진수의 목록입니다.
        (1732584193, 4023233417, 2562383102, 271733878, 3285377520)에 각각 대응하는 번호를 갖습니다. 
        우리는 이것을 메시지 다이제스트로 시작할 것입니다. 0x는 파이썬에서 16 진수를 쓰는 방법입니다.
        """
        self.data = data
        self.h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

    @staticmethod
    def rotate(n, b):
        """
        다른 메서드 내에서 사용되는 정적 메서드입니다. 왼쪽은 n을 b만큼 회전합니다.
        """
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    def padding(self):
        """
        padded_data가 64 바이트 또는 512 비트가되도록 입력 메시지에 0을 덧붙입니다.
        """
        padding = b'\x80' + b'\x00'*(63 - (len(self.data) + 8) % 64)
        padded_data = self.data + padding + struct.pack('>Q', 8 * len(self.data))
        return padded_data

    def split_blocks(self):
        """
        각 길이가 64 인 바이트의 목록을 반환합니다.
        """
        return [self.padded_data[i:i+64] for i in range(0, len(self.padded_data), 64)]

    # @staticmethod
    def expand_block(self, block):
        """
        길이 64의 바이트 블록을 가져 와서 정수 목록에 압축을 푼 다음 비트 연산 후 80 개의 정수 목록을 반환합니다.
        """
        w = list(struct.unpack('>16L', block)) + [0] * 64
        for i in range(16, 80):
            w[i] = self.rotate((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)
        return w

    def final_hash(self):
        """
        다른 모든 메소드를 호출하여 입력을 처리합니다. 데이터를 패딩 한 다음 블록으로 분할 한 다음 
        각 블록 (확장 포함)에 대해 일련의 작업을 수행합니다.
        각 블록에 대해 초기화 된 변수 h가 a, b, c, d, e에 복사되고 
        이러한 5 개의 변수 a, b, c, d, e는 여러 변경 사항을 거칩니다. 
        모든 블록이 처리 된 후,이 5 개의 변수는 h ie a에서 h [0], b에서 h [1] 등과 같이 쌍으로 추가됩니다.
        이 h는 반환되는 최종 해시가됩니다.
        """
        self.padded_data = self.padding()
        self.blocks = self.split_blocks()
        for block in self.blocks:
            expanded_block = self.expand_block(block)
            a, b, c, d, e = self.h
            for i in range(0, 80):
                if 0 <= i < 20:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i < 40:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i < 80:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6
                a, b, c, d, e = self.rotate(a, 5) + f + e + k + expanded_block[i] & 0xffffffff,\
                                a, self.rotate(b, 30), c, d
        self.h = self.h[0] + a & 0xffffffff,\
                 self.h[1] + b & 0xffffffff,\
                 self.h[2] + c & 0xffffffff,\
                 self.h[3] + d & 0xffffffff,\
                 self.h[4] + e & 0xffffffff
        return '%08x%08x%08x%08x%08x' %tuple(self.h)


class SHA1HashTest(unittest.TestCase):
    """
    SHA1Hash 클래스의 테스트 클래스. unittest에서 TestCase 클래스를 상속받습니다.
    """
    def testMatchHashes(self):
        msg = bytes('Test String', 'utf-8')
        self.assertEqual(SHA1Hash(msg).final_hash(), hashlib.sha1(msg).hexdigest())


def main():
    """
    'string'또는 'file'옵션을 제공하여 입력을 가져오고 계산 된 SHA1 해시를 인쇄합니다.
     unittest.main ()이 주석 처리되었습니다. 우리가 실행하고 싶지 않기 때문입니다.
     매번 시험.
    """
    # unittest.main()
    parser = argparse.ArgumentParser(description='Process some strings or files')
    parser.add_argument('--string', dest='input_string',
                        default='Hello World!! Welcome to Cryptography',
                        help='Hash the string')
    parser.add_argument('--file', dest='input_file', help='Hash contents of a file')
    args = parser.parse_args()
    input_string = args.input_string
    #In any case hash input should be a bytestring
    if args.input_file:
        hash_input = open(args.input_file, 'rb').read()
    else:
        hash_input = bytes(input_string, 'utf-8')
    print(SHA1Hash(hash_input).final_hash())


if __name__ == '__main__':
    main()
