
"""
파일 전송 프로토콜 : FTP 서버를 이용한 발송 및 수신
FTP client에 접근 하기 위해 권한을 이용해야한다.

공지 : 보안상의 문제가 있을 수 있으므로 root의 유저 이름과 비밀번호를 입력하지 마세요.
개별 유저를 만든 후 그 곳에서 home directory를 만들어 접근을 하세요.
현재 작업중인 디렉토리에 접근 중인 유저의 아이디와 비밀번호를 이용하여 접속하세요.
"""
from ftplib import FTP
ftp = FTP('xxx.xxx.x.x')  # Enter the ip address or the domain name here
ftp.login(user='username', passwd='password')
ftp.cwd('/Enter the directory here/')

"""
FTP 서버를 통해 전달받을 파일에 대한 함수이다.
파일을 받을 곳의 위치를 접속한다.
"""

def ReceiveFile():
	FileName = 'example.txt'   """ 파일의 위치에 접속 """
	LocalFile = open(FileName, 'wb')
	ftp.retrbinary('RETR ' + FileName, LocalFile.write, 1024)
	ftp.quit()
	LocalFile.close()


"""
FTP 서버를 통해 전달할 파일에 대한 함수이다.
현재 작업중인 디렉토리를 통해 이 파일이 전송된다.
"""

def SendFile():
	FileName = 'example.txt'   """ 파일의 이름 입력  """
	ftp.storbinary('STOR ' + FileName, open(FileName, 'rb'))
	ftp.quit()
