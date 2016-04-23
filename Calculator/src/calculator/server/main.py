'''
Created on 2016. 4. 16.

@author: Hwajung Lee
'''

if __name__ == '__main__':
### UDP ###
    from socket import *    # 소켓 생성을 위한 모듈
    serverPort = 12000      # 서버의 포트 번호
    
    serverSocket = socket(AF_INET, SOCK_DGRAM)  # 서버 측에 IPv4(AF_INET)와 UDP(SOCK_DGRAM)를 사용하는 소켓 생성
    serverSocket.bind(('', serverPort))         # 서버 소켓에 포트 번호 할당
    print ("The server is ready to receive")
     
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)    # 서버 소켓을 통해 클라이언트로부터 메시지를 받음
        modifiedMessage = message.upper()
        serverSocket.sendto(modifiedMessage, clientAddress)     # 결과를 소켓으로 보냄


### TCP ###
#     from socket import *
#     serverPort = 12000
#     
#     serverSocket = socket(AF_INET,SOCK_STREAM)    # 서버 측에 IPv4(AF_INET)와 TCP(SOCK_STREAM)를 사용하는 소켓 생성
#     serverSocket.bind(('',serverPort))            # 서버 소켓에 포트 번호 할당
#     serverSocket.listen(1)                        # 연결 요청 듣기 (최대 연결수는 1)
#     print ('The server is ready to receive')
#     
#     while True:
#         connectionSocket, addr = serverSocket.accept()    # 연결된 클라이언트에 특정된 서버 사이에, 새로운 소켓 생성을 생성하고 TCP 연결
#         sentence = connectionSocket.recv(1024)            # 소켓을 통해 클라이언트로부터 메시지를 받음
#         capitalizedSentence = sentence.upper()
#         connectionSocket.send(capitalizedSentence)        # 결과를 소켓으로 보냄
#         connectionSocket.close()                          # 소켓을 닫음