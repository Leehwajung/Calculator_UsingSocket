'''
Created on 2016. 4. 16.

@author: Hwajung Lee
'''

if __name__ == '__main__':
    import socket                   # 소켓 생성을 위한 모듈
    serverName = '192.168.0.10'     # 서버의 IP 주소
    serverPort = 12000              # 서버의 포트 번호
    socketType = socket.SOCK_STREAM # 소켓 타입 (SOCK_DGRAM: UDP, SOCK_STREAM: TCP)
    bufferSize = 1024               # 메시지 버퍼 크기
    
    print("### Simple Arithmetic Calculator ###")
    print(" - If you want to quit, input \"quit\" or \"q\".\n")
    while True:
        # 사용자 입력
        message = input("Input arithmetic sentence: ")
        # 종료 명령
        if message.lower() == "quit" or message.lower() == "q": 
            break;
        # 클라이언트 측에 IPv4(AF_INET) 소켓 생성
        clientSocket = socket.socket(socket.AF_INET, socketType)
        
        # UDP(SOCK_DGRAM)
        if socketType == socket.SOCK_DGRAM:
            # 클라이언트 소켓을 통해 서버로 메시지를 보내고 수신을 기다림
            clientSocket.sendto(message.encode(),(serverName, serverPort))
            # 받은 데이터 할당
            modifiedMessage, serverAddress = clientSocket.recvfrom(bufferSize)
            
        # TCP(SOCK_STREAM)
        elif socketType == socket.SOCK_STREAM:
            # 핸드 셰이크 및 TCP 연결 설정
            clientSocket.connect((serverName,serverPort))
            # 클라이언트 소켓을 통해 메시지를 서버로 보내고 수신을 기다림
            clientSocket.send(message.encode())
            # 받은 데이터 할당
            modifiedMessage = clientSocket.recv(bufferSize)
        
        # 받은 메시지 출력
        print("Output result:", modifiedMessage.decode())
        # 소켓을 닫음
        clientSocket.close()
    
    print("Program is terminated.")