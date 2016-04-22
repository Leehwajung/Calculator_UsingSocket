### UDPServer.py ###

# 소켓 생성을 위한 모듈
from socket import *
# 서버의 포트 번호
serverPort = 12000

# 서버 측에 IPv4(AF_INET)와 UDP(SOCK_DGRAM)를 사용하는 소켓 생성
serverSocket = socket(AF_INET, SOCK_DGRAM)
# 서버 소켓에 포트 번호 할당
serverSocket.bind(('', serverPort))
print ("The server is ready to receive")
 
while True:
    # 서버 소켓을 통해 클라이언트로부터 메시지를 받음
    message, clientAddress = serverSocket.recvfrom(2048)
    # 메시지에 대한 작업
    modifiedMessage = message.upper()
    # 결과를 소켓으로 보냄
    serverSocket.sendto(modifiedMessage, clientAddress)