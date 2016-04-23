'''
Created on 2016. 4. 16.

@author: Hwajung Lee
'''

if __name__ == '__main__':
### UDP ###
    from socket import *        # 소켓 생성을 위한 모듈
    serverName = '192.168.0.10' # 서버의 IP 주소
    serverPort = 12000          # 서버의 포트 번호
    
    clientSocket = socket(AF_INET, SOCK_DGRAM)                      # 클라이언트 측에 IPv4(AF_INET)와 UDP(SOCK_DGRAM)를 사용하는 소켓 생성
    message = input('Input lowercase sentence:')                    # 사용자 입력
    clientSocket.sendto(message.encode(),(serverName, serverPort))  # 클라이언트 소켓을 통해 서버로 메시지를 보내고 수신을 기다림
    
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)    # 받은 데이터 할당
    print('From Server:', modifiedMessage)                          # 받은 메시지 출력
    clientSocket.close()                                            # 소켓을 닫음


### TCP ###
#     from socket import *        # 소켓 생성을 위한 모듈
#     serverName = '192.168.0.10' # 서버의 IP 주소
#     serverPort = 12000          # 서버의 포트 번호
#       
#     clientSocket = socket(AF_INET, SOCK_STREAM)     # 클라이언트 측에 IPv4(AF_INET)와 TCP(SOCK_STREAM)를 사용하는 소켓 생성
#     clientSocket.connect((serverName,serverPort))   # 핸드 셰이크 및 TCP 연결 설정
#     sentence = input('Input lowercase sentence:')   # 사용자 입력
#     clientSocket.send(sentence.encode())            # 클라이언트 소켓을 통해 메시지를 서버로 보내고 수신을 기다림
#       
#     modifiedSentence = clientSocket.recv(1024)      # 받은 데이터 할당
#     print('From Server:', modifiedSentence)         # 받은 메시지 출력
#     clientSocket.close()                            # 소켓을 닫음