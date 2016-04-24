'''
Created on 2016. 4. 16.

@author: Hwajung Lee
'''

def proceed(message, address):
    modifiedMessage = message.upper()
    print (address, ": ", modifiedMessage)
    return modifiedMessage

if __name__ == '__main__':
    from socket import *        # 소켓 생성을 위한 모듈
    serverPort = 12000          # 서버의 포트 번호
    socketType = SOCK_STREAM    # 소켓 타입 (SOCK_DGRAM: UDP, SOCK_STREAM: TCP)
    bufferSize = 1024           # 메시지 버퍼 크기
    
    serverSocket = socket(AF_INET, socketType)  # 서버 측에 IPv4(AF_INET)와 UDP(SOCK_DGRAM)를 사용하는 소켓 생성
    serverSocket.bind(('', serverPort))         # 서버 소켓에 포트 번호 할당
    if socketType == SOCK_STREAM:               # TCP(SOCK_STREAM)
        serverSocket.listen(1)                  # 연결 요청 듣기 (최대 연결수는 1)
    print ("The server is ready to receive")
    
    if socketType == SOCK_DGRAM:                                                # UDP(SOCK_DGRAM)
        while True:
            message, clientAddress = serverSocket.recvfrom(bufferSize)          # 서버 소켓을 통해 클라이언트로부터 메시지를 받음
            serverSocket.sendto(proceed(message, clientAddress), clientAddress) # 결과를 소켓으로 보냄
        
    elif socketType == SOCK_STREAM:                                 # TCP(SOCK_STREAM)
        while True:
            connectionSocket, clientAddress = serverSocket.accept() # 연결된 클라이언트에 특정된 서버 사이에, 새로운 소켓 생성을 생성하고 TCP 연결
            message = connectionSocket.recv(bufferSize)             # 소켓을 통해 클라이언트로부터 메시지를 받음
            connectionSocket.send(proceed(message, clientAddress))  # 결과를 소켓으로 보냄
            connectionSocket.close()                                # 소켓을 닫음