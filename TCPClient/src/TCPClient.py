### TCPClient.py ###

# 소켓 생성을 위한 모듈
from socket import *
# 서버의 IP 주소
serverName = '192.168.0.10'
# 서버의 포트 번호
serverPort = 12000

# 클라이언트 측에 IPv4(AF_INET)와 TCP(SOCK_STREAM)를 사용하는 소켓 생성
clientSocket = socket(AF_INET, SOCK_STREAM)
# 핸드 셰이크 및 TCP 연결 설정
clientSocket.connect((serverName,serverPort))
# 사용자 입력
sentence = input('Input lowercase sentence:')
# 클라이언트 소켓을 통해 메시지를 서버로 보내고 수신을 기다림
clientSocket.send(sentence.encode())

# 받은 데이터 할당
modifiedSentence = clientSocket.recv(1024)
# 받은 메시지 출력
print('From Server:', modifiedSentence.decode())
# 소켓을 닫음
clientSocket.close()