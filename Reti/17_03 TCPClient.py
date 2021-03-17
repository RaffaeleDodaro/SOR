from socket import *

serverName='192.168.0.3'
serverPort=6789

clientSocket=socket(AF_INET,SOCK_STREAM) #AF_INET vuol dire che mi appoggio al protocollo ip. SOCK_STREAM specifica che voglio un socket tcp
clientSocket.connect(serverName,serverPort) #faccio la telefonata
sentence=input("Frase in minuscolo: ")
clientSocket.makefile("w").writelines(sentence+"\n")
modifiedSentence=clientSocket.makefile().readline() #leggo quello che mi ha mandato il server
print("FROM SERVER: ",modifiedSentence)
clientSocket.close()