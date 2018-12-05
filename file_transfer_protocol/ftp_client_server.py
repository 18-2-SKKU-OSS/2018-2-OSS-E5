# server

import socket                   # Import socket module 

port = 60000                    # 사용할 포트 설정
s = socket.socket()             # 소켓 오브젝트 생성
host = socket.gethostname()     # 로컬 머신 이름 지정
s.bind((host, port))            # 포트에 바인드
s.listen(5)                     # 클라이언트 연결을 대기.

print('Server listening....')

while True:
    conn, addr = s.accept()     # 클라이언트와 연결 수립
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data)) # 연결 되었을시 서버에 알림

    filename = 'mytext.txt'
    f = open(filename, 'rb')
    in_data = f.read(1024)  # 연결된 1024 위치로부터 데이터를 읽음
    while (in_data):
       conn.send(in_data)       #서버에 읽은 데이터 전송
       print('Sent ', repr(in_data))
       in_data = f.read(1024)
    f.close()               # 모든 데이터를 읽고 서버에 전송한 뒤 파일 닫기

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()            # 연결 종료


# client side server

import socket                   # Import socket module

s = socket.socket()             # 소켓 오브젝트 생성
host = socket.gethostname()     # 로컬 머신 이름 받아오기
port = 60000                    # 사용할 포트 지정

s.connect((host, port))
s.send("Hello server!")         # 연결에 성공하였을시 메세지 전송

with open('received_file', 'wb') as f:
    print('file opened')
    while True:                 # 서버에 저장된 값들을 열어서
        print('receiving data...')
        data = s.recv(1024)     # 클라이언트에 받은 파일로서 값을 옮긴다.
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()                       # 파일에 모든 내용들을 다 옮긴 뒤 닫기
print('Successfully get the file')
s.close()
print('connection closed')      # 연결 종료
