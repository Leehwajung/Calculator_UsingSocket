### UDPClient.py ###

# 소켓 생성을 위한 모듈
from socket import *
# 서버의 IP 주소
serverName = '192.168.0.10'
# 서버의 포트 번호
serverPort = 12000

# 클라이언트 측에 IPv4(AF_INET)와 UDP(SOCK_DGRAM)를 사용하는 소켓 생성
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 사용자 입력
message = input('Input lowercase sentence:')
# 클라이언트 소켓을 통해 서버로 메시지를 보내고 수신을 기다림
clientSocket.sendto(message.encode(),(serverName, serverPort))

# 받은 데이터 할당
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# 받은 메시지 출력
print('From Server:', modifiedMessage.decode())
# 소켓을 닫음
clientSocket.close()