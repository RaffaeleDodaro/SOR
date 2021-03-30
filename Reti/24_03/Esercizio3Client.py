from socket import *

serverName = '192.168.0.122'
serverPort = 6789

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

clientSocket.makefile("w").writelines(input("inserisci comando ")+"\n")
response = clientSocket.makefile().readline()
while response != "<EOF>\n":
    print(response)
    response = clientSocket.makefile().readline()

clientSocket.close()