'''
Created on 2016. 4. 16.

@author: Hwajung Lee
'''

if __name__ == '__main__':
    import socket                   # 소켓 생성을 위한 모듈
    serverName = '192.168.0.10'     # 서버의 IP 주소
    serverPort = 12004              # 서버의 포트 번호
    socketType = socket.SOCK_STREAM # 소켓 타입 (SOCK_DGRAM: UDP, SOCK_STREAM: TCP)
    bufferSize = 1024               # 메시지 버퍼 크기
    
    while True:
        message = input("Input arithmetic sentence: ")              # 사용자 입력
        if message.lower() == "exit" or message.lower() == "e":     # 종료 명령
            break;
        clientSocket = socket.socket(socket.AF_INET, socketType)    # 클라이언트 측에 IPv4(AF_INET) 소켓 생성
        
        if socketType == socket.SOCK_DGRAM:                                     # UDP(SOCK_DGRAM)
            clientSocket.sendto(message.encode(),(serverName, serverPort))      # 클라이언트 소켓을 통해 서버로 메시지를 보내고 수신을 기다림
            modifiedMessage, serverAddress = clientSocket.recvfrom(bufferSize)  # 받은 데이터 할당
            
        elif socketType == socket.SOCK_STREAM:              # TCP(SOCK_STREAM)
            clientSocket.connect((serverName,serverPort))   # 핸드 셰이크 및 TCP 연결 설정
            clientSocket.send(message.encode())             # 클라이언트 소켓을 통해 메시지를 서버로 보내고 수신을 기다림
            modifiedMessage = clientSocket.recv(bufferSize) # 받은 데이터 할당
        
        print("Output result:", modifiedMessage.decode())   # 받은 메시지 출력
        clientSocket.close()                                # 소켓을 닫음
    
    print("Program is terminated.")