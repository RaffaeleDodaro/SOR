from socket import *
import sys

serverAddress = sys.argv[1]
senderEmail = sys.argv[2]
destEmail = sys.argv[3]
file = open(r"/mnt/c/Users/Danilo/PycharmProjects/EsercitazioneReti24/03/2021/wewe.txt")
text = file.read()

server = serverAddress.split(":",1)
portNum = int(server[1])

socket = socket(AF_INET, SOCK_STREAM)
socket.connect((server[0],portNum))

answer = socket.makefile().readline()
print(answer)
socket.makefile("w").writelines("HELO gibbi" + "\r\n")
answer = socket.makefile().readline()
print(answer)
socket.makefile("w").writelines("MAIL FROM: " + senderEmail + "\r\n")
answer = socket.makefile().readline()
print(answer)
socket.makefile("w").writelines("RCPT TO: " + destEmail + "\r\n")
answer = socket.makefile().readline()
print(answer)
socket.makefile("w").writelines("DATA" + "\r\n")
socket.makefile("w").writelines(text+"\r\n")
print(text)
socket.makefile("w").writelines(".\r\n")
answer = socket.makefile().readline()
print(answer)
answer = socket.makefile().readline()
print(answer)
socket.makefile("w").writelines("QUIT\r\n")
answer = socket.makefile().readline()
print(answer)