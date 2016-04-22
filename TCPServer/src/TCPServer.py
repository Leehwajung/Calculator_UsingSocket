### TCPServer.py ###

# 소켓 생성을 위한 모듈
from socket import *
# 서버의 포트 번호
serverPort = 12000

# 서버 측에 IPv4(AF_INET)와 TCP(SOCK_STREAM)를 사용하는 소켓 생성
serverSocket = socket(AF_INET,SOCK_STREAM)
# 서버 소켓에 포트 번호 할당
serverSocket.bind(('',serverPort))
# 연결 요청 듣기 (최대 연결수는 1)
serverSocket.listen(1)
print ('The server is ready to receive')

while True:
    # 연결된 클라이언트에 특정된 서버 사이에, 새로운 소켓 생성을 생성하고 TCP 연결
    connectionSocket, addr = serverSocket.accept()
    # 소켓을 통해 클라이언트로부터 메시지를 받음
    sentence = connectionSocket.recv(1024)
    # 메시지에 대한 작업
    capitalizedSentence = sentence.upper()
    # 결과를 소켓으로 보냄
    connectionSocket.send(capitalizedSentence)
    # 소켓을 닫음
    connectionSocket.close()