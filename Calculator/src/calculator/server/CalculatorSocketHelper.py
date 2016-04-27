'''
Created on 2016. 4. 25.

@author: Hwajung Lee
'''

import socket
from calculator.server.Calculator import Calculator

class CalculatorSocketHelper(object):
    '''
    Socket Helper for Calculator of server
    '''
    __defaultType = socket.SOCK_DGRAM
    __defaultPort = 12000
    __defaultBufferSize = 1024
    __defalutListenings = 1
    
    def __init__(self, socketType = __defaultType, serverPort = __defaultPort, bufferSize = __defaultBufferSize):
        '''
        Constructor
        '''
        self.socketType = socketType    # 소켓 타입 (SOCK_DGRAM: UDP, SOCK_STREAM: TCP)
        self.serverPort = serverPort    # 서버의 포트 번호
        self.bufferSize = bufferSize    # 메시지 버퍼 크기
        
        # 서버 측에 IPv4(AF_INET)와 UDP(SOCK_DGRAM)를 사용하는 소켓 생성
        self.serverSocket = socket.socket(socket.AF_INET, self.socketType)
        # 서버 소켓에 포트 번호 할당
        self.serverSocket.bind(('', self.serverPort))
        # TCP(SOCK_STREAM)일 경우 연결 요청 듣기 (최대 연결수는 1)
        if self.socketType == socket.SOCK_STREAM:
            self.serverSocket.listen(self.__defalutListenings)
        print ("The server is ready to receive")
    
    def runSocket(self):
        print("The server is running ...")
        # UDP(SOCK_DGRAM)
        if self.socketType == socket.SOCK_DGRAM:
            while True:
                # 서버 소켓을 통해 클라이언트로부터 메시지를 받음
                message, clientAddress = self.serverSocket.recvfrom(self.bufferSize)
                # 결과를 소켓으로 보냄
                self.serverSocket.sendto(self.__proceed(message, clientAddress), clientAddress)
            
        # TCP(SOCK_STREAM)
        elif self.socketType == socket.SOCK_STREAM:
            while True:
                # 연결된 클라이언트에 특정된 서버 사이에, 새로운 소켓 생성을 생성하고 TCP 연결
                connectionSocket, clientAddress = self.serverSocket.accept()
                # 소켓을 통해 클라이언트로부터 메시지를 받음
                message = connectionSocket.recv(self.bufferSize)
                # 결과를 소켓으로 보냄
                connectionSocket.send(self.__proceed(message, clientAddress))
                # 연결 소켓을 닫음
                connectionSocket.close()
    
    def __proceed(self, message, address):
        decodedMsg = message.decode()
        form = decodedMsg.split('=')
        print ("Received from", self.socketType, address, ":\t", decodedMsg)
        cal = Calculator()
        try:
            result = form[0] + "= "
            result += str(cal.calculate(form[0]))
        except Exception as e:
            result = "Syntax Error"
            print ("Error:", e)
        print ("Send to", self.socketType, address, ":\t", result)
        return result.encode()
    
    def closeSocket(self):
        # 서버 소켓을 닫음
        self.serverSocket.close()
        print ("The server is closed")