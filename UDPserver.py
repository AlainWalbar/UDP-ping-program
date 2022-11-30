from socket import *

#UDP Server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)              #Creating a UDP socket
serverSocket.bind(('', serverPort))


print("The server is running")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)    #Receive client package
    print (message.decode())
    pong = 'Message received!'
    serverSocket.sendto(pong.encode(), clientAddress)    #send it back to client

print("Done")
