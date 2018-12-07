# client.py

import socket

HOST, PORT = '127.0.0.1', 1400

s = socket.socket(

            socket.AF_INET,      # address family
                                 #Name 목적
                                 #AF_UNIX, AF_LOCAL 지역 통신
                                 #AF_INET IPv4 인터넷 프로토콜
                                 # AF_INET6 IPv6 인터넷 프로토콜
                                 #AF_APPLETALK Appletalk
                                 #AF_BLUETOOTH 블루투스

            socket.SOCK_STREAM  #           소켓 유형
                                #Name           통신 수단
                                #SOCK_STREAM    TCP
                                #SOCK_DGRAM     UDP
)
s.connect((HOST, PORT))

s.send('Hello World'.encode('ascii')) #in UDP use sendto()
data = s.recv(1024)                   #in UDP use recvfrom()

s.close()# 연결 종료
print(repr(data.decode('ascii')))
