from __future__ import print_function
import math

def rearrange(bitString32):
	"""[요약]
	주어진 2 진 문자열을 다시 그룹화합니다.

	인수 :
	bitString32 {[string]} - [32 비트 바이너리]

	제기 :
	ValueError - [주어진 문자열이 32 비트 이진 문자열이 아닌 경우]

	보고:
	[문자열] - [32 비트 바이너리 문자열]
	"""

	if len(bitString32) != 32:
		raise ValueError("Need length 32")
	newString = ""
	for i in [3,2,1,0]:
		newString += bitString32[8*i:8*i+8]
	return newString

def reformatHex(i):
	"""[summary]
	주어진 정수를 8 자리 16 진수로 변환합니다.

	인수 :
	i {[int]} - [정수]
	"""

	hexrep = format(i,'08x')
	thing = ""
	for i in [3,2,1,0]:
		thing += hexrep[2*i:2*i+2]
	return thing

def pad(bitString):
	"""[summary]
	이진 문자열을 512 비트 이진 문자열로 채 웁니다.

	인수 :
	bitString {[string]} - [바이너리 문자열]

	보고:
	[문자열] - [바이너리 문자열]
	"""

	startLength = len(bitString)
	bitString += '1'
	while len(bitString) % 512 != 448:
		bitString += '0'
	lastPart = format(startLength,'064b')
	bitString += rearrange(lastPart[32:]) + rearrange(lastPart[:32]) 
	return bitString

def getBlock(bitString):
	"""[summary]
	반복자 :
	각 호출에 의해 길이가 16 인 목록을 32 비트로 반환합니다.
	정수 블록.

	인수 :
	bitString {[string]} - [binary string> = 512]
	"""

	currPos = 0
	while currPos < len(bitString):
		currPart = bitString[currPos:currPos+512]
		mySplits = []
		for i in range(16):
			mySplits.append(int(rearrange(currPart[32*i:32*i+32]),2))
		yield mySplits
		currPos += 512

def not32(i):
	i_str = format(i,'032b')
	new_str = ''
	for c in i_str:
		new_str += '1' if c=='0' else '0'
	return int(new_str,2)

def sum32(a,b):
	return (a + b) % 2**32

def leftrot32(i,s):
	return (i << s) ^ (i >> (32-s))

def md5me(testString):
	"""[summary]
	'testString'문자열의 32 비트 해시 코드를 반환합니다.

	인수 :
	testString {[문자열]} - [메시지]
	"""

	bs =''
	for i in testString:
		bs += format(ord(i),'08b')
	bs = pad(bs)

	tvals = [int(2**32 * abs(math.sin(i+1))) for i in range(64)]

	a0 = 0x67452301
	b0 = 0xefcdab89
	c0 = 0x98badcfe
	d0 = 0x10325476

	s = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22, \
		5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20, \
		4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23, \
		6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21 ]

	for m in getBlock(bs):
		A = a0 
		B = b0
		C = c0
		D = d0
		for i in range(64):
			if i <= 15:
				#f = (B & C) | (not32(B) & D)
				f = D ^ (B & (C ^ D))
				g = i
			elif i<= 31:
				#f = (D & B) | (not32(D) & C)
				f = C ^ (D & (B ^ C))
				g = (5*i+1) % 16
			elif i <= 47:
				f = B ^ C ^ D
				g = (3*i+5) % 16
			else:
				f = C ^ (B | not32(D))
				g = (7*i) % 16
			dtemp = D
			D = C
			C = B
			B = sum32(B,leftrot32((A + f + tvals[i] + m[g]) % 2**32, s[i]))
			A = dtemp
		a0 = sum32(a0, A)
		b0 = sum32(b0, B)
		c0 = sum32(c0, C)
		d0 = sum32(d0, D)

	digest = reformatHex(a0) + reformatHex(b0) + reformatHex(c0) + reformatHex(d0)
	return digest

def test():
	assert md5me("") == "d41d8cd98f00b204e9800998ecf8427e"	
	assert md5me("빠른 갈색 여우는 게으른 개를 뛰어 넘습니다.") == "9e107d9d372bb6826bd81d3542a419d6"
	print("Success.")


if __name__ == "__main__":
	test()
