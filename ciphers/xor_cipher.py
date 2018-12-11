"""
	author: Christian Bender
	date: 21.12.2017
	class: XORCipher

	이 클래스는 XOR-cipher 알고리즘을 구현해,
	문자열을 암호화하고 해독하는 유용한 방법
	파일.

	메소드 개요

	- 암호화 : char의 목록
	- decrypt : char의 목록
	- encrypt_string : str
	- decrypt_string : str
	- 암호화 파일 : 부울
	- decrypt_file : 부울
"""
class XORCipher(object):

	def __init__(self, key = 0):
		"""
			simple constructor that receives a key or uses
			default key = 0
		"""

		#private field
		self.__key = key

	def encrypt(self, content, key):
		"""
			입력 : 문자열 유형의 'content'및 유형 유형의 'key'
			출력 : 암호화 된 문자열 'content'를 문자 목록으로 사용
			키가 건네받지 않은 경우, 메서드는 생성자에 의해 키를 사용합니다.
			그렇지 않으면 key = 1
		"""

		# precondition
		assert (isinstance(key,int) and isinstance(content,str))

		key = key or self.__key or 1

		# make sure key can be any size
		while (key > 255):
			key -= 255

		# This will be returned
		ans = []

		for ch in content:
			ans.append(chr(ord(ch) ^ key))

		return ans

	def decrypt(self,content,key):
		"""
			입력 : 유형 목록의 'content'및 유형 'int'의 'key'
			출력 : 문자의 목록으로 해독 된 문자열 'content'
			키가 건네받지 않은 경우, 메서드는 생성자에 의해 키를 사용합니다.
			그렇지 않으면 key = 1
		"""

		# precondition
		assert (isinstance(key,int) and isinstance(content,list))

		key = key or self.__key or 1

		# make sure key can be any size
		while (key > 255):
			key -= 255

		# This will be returned
		ans = []

		for ch in content:
			ans.append(chr(ord(ch) ^ key))

		return ans


	def encrypt_string(self,content, key = 0):
		"""
			입력 : 문자열 유형의 'content'및 유형 유형의 'key'
			출력 : 암호화 된 문자열 'content'
			키가 건네받지 않은 경우, 메서드는 생성자에 의해 키를 사용합니다.
			그렇지 않으면 key = 1
		"""

		# precondition
		assert (isinstance(key,int) and isinstance(content,str))

		key = key or self.__key or 1

		# make sure key can be any size
		while (key > 255):
			key -= 255

		# This will be returned
		ans = ""

		for ch in content:
			ans += chr(ord(ch) ^ key)

		return ans

	def decrypt_string(self,content,key = 0):
		"""
			입력 : 문자열 유형의 'content'및 유형 유형의 'key'
			출력 : 해독 된 문자열 'content'
			키가 건네받지 않은 경우, 메서드는 생성자에 의해 키를 사용합니다.
			그렇지 않으면 key = 1
		"""

		# precondition
		assert (isinstance(key,int) and isinstance(content,str))

		key = key or self.__key or 1

		# make sure key can be any size
		while (key > 255):
			key -= 255

		# This will be returned
		ans = ""
		
		for ch in content:
			ans += chr(ord(ch) ^ key)

		return ans


	def encrypt_file(self, file, key = 0):
		"""
			입력 : 파일 이름 (str)과 키 (int)
			output : 암호화 프로세스가 true이면 true를 반환합니다.
			성공 그렇지 않으면 거짓
			키가 건네받지 않은 경우, 메서드는 생성자에 의해 키를 사용합니다.
			그렇지 않으면 key = 1
		"""

		#precondition
		assert (isinstance(file,str) and isinstance(key,int))

		try:
			with open(file,"r") as fin:
				with open("encrypt.out","w+") as fout:

					# actual encrypt-process
					for line in fin:
						fout.write(self.encrypt_string(line,key))

		except:
			return False

		return True


	def decrypt_file(self,file, key):
		"""
			입력 : 파일 이름 (str)과 키 (int)
			output : 프로세스의 암호를 해독 한 경우 true를 반환합니다.
			성공 그렇지 않으면 거짓
			키가 건네받지 않은 경우, 메서드는 생성자에 의해 키를 사용합니다.
			그렇지 않으면 key = 1
		"""

		#precondition
		assert (isinstance(file,str) and isinstance(key,int))

		try:
			with open(file,"r") as fin:
				with open("decrypt.out","w+") as fout:

					# actual encrypt-process
					for line in fin:
						fout.write(self.decrypt_string(line,key))

		except:
			return False

		return True




# Tests
# crypt = XORCipher()
# key = 67

# # test enrcypt
# print crypt.encrypt("hallo welt",key)
# # test decrypt
# print crypt.decrypt(crypt.encrypt("hallo welt",key), key)

# # test encrypt_string
# print crypt.encrypt_string("hallo welt",key)

# # test decrypt_string
# print crypt.decrypt_string(crypt.encrypt_string("hallo welt",key),key)

# if (crypt.encrypt_file("test.txt",key)):
# 	print "encrypt successful"
# else:
# 	print "encrypt unsuccessful"

# if (crypt.decrypt_file("encrypt.out",key)):
# 	print "decrypt successful"
# else:
# 	print "decrypt unsuccessful"
