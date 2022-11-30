import time
import json
from socket import *

#Opening json file
f = open('wheel_rotation_sensor_data.json')

#Return json file as a dictionary
data = json.load(f)

#UDP Client
serverName = gethostname()
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)      #Create a UDP socket

userping= input('Send a message to the server :')
clientSocket.sendto(userping.encode(), (serverName,serverPort)) #sending message to the server

for i in data['wheel']:
    #UDP Client
    serverName = gethostname()
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)      #Create a UDP socket

    #Timeout value of 1 second
    clientSocket.settimeout(1)

    #Ping to server with the data from the json file
    message = json.dumps(i, sort_keys=True, indent=4)     #convert dict into a string to encode
    #Send the ping to the server
    start = time.time()
    clientSocket.sendto(message.encode(), (serverName, serverPort))     #sending message to the server

    #Pong from the server
    try:
        pong, serverAddress= clientSocket.recvfrom(2048) 
        end = time.time()
        rtt = end - start                   #calculating the RTT by substracting to the time of server response the time of sending the message
        print (pong.decode())               #print now modified message
        print (f'Delay of {rtt} seconds')   #print the RTT 

    except timeout:                         #in case of no response from the server after one second we print an error message
        print ('Packet from server lost')


clientSocket.close()