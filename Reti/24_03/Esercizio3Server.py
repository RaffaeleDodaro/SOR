from socket import *
import os

serverPort = 6789

serverSocket = socket()
serverSocket.bind(('', serverPort))
serverSocket.listen(20)
print("Server avviato")

while True:
    clientSocket, addr = serverSocket.accept()
    print(addr)
    clientSentence = clientSocket.makefile().readline()
    comando = clientSentence.split()
    print("Il comando che ho ricevuto è: "+clientSentence)
    if((clientSentence == "ls\n" or clientSentence == "LS\n") and (len(comando)==1)):
        result = os.listdir(".")
        for file in result:
            clientSocket.makefile("w").writelines(file + "\n")
        clientSocket.makefile("w").writelines("<EOF>\n")
    
    elif(len(comando)>1):
        print("lunghezza comando: \n",len(comando))
        if(comando[0] == "cat" or comando[0] == "CAT"):
            try:
                result=open(comando[1], "r")
                clientSocket.makefile("w").writelines("OK\n")

                for file in result:
                    clientSocket.makefile("w").writelines(file + "\n")
                clientSocket.makefile("w").writelines("<EOF>\n")
            except OSError:
                clientSocket.makefile("w").writelines("ERROR\n")
                clientSocket.makefile("w").writelines("<EOF>\n")
        elif(comando[0] == "cd" or comando[0] == "CD"):
            os.chdir(comando[1]) 
            clientSocket.makefile("w").writelines("New working directory is: \n",comando[1])
            clientSocket.makefile("w").writelines("<EOF>\n")
    else:
        clientSocket.makefile("w").writelines("Comando non riconosciuto\n")
        clientSocket.makefile("w").writelines("<EOF>\n")

    clientSocket.makefile("w").writelines("<EOF>\n")
    clientSocket.close()




