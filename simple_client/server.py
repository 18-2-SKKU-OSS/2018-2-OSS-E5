# server.py

import socket

HOST, PORT = '127.0.0.1', 1400

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #client.py를 참조하십시오.
s.bind((HOST, PORT))
s.listen(1)                                             # 1개의 연결에 대해 listen.

conn, addr = s.accept()                                 # 실제 데이터 흐름 시작

print('connected to:', addr)

while 1:
    data = conn.recv(1024).decode('ascii')# 1024 바이트를 받고 ascii를 사용하여 디코딩
    if not data:
        break
    conn.send((data + ' [ addition by server ]').encode('ascii'))

conn.close()
