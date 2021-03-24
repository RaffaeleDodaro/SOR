from socket import *

serverName = '192.168.0.113'
serverPort = 6789

modifiedSentence = ""

# Sapreste modificare le regole del protocollo applicazione in modo che la connessione
# con ciascun client sia permanente, il server maiuscolizzi ogni frase inviata da ciascun
# client e non solo la prima, e il server si sconnette solo quando riceve la stringa "BASTA"?
clientSocket = socket(AF_INET,
                      SOCK_STREAM)  # AF_INET vuol dire che mi appoggio al protocollo ip. SOCK_STREAM specifica che voglio un socket tcp
clientSocket.connect((serverName, serverPort))  # faccio la telefonata
while modifiedSentence != "BASTA\n":
    sentence = input("Frase in minuscolo: ")
    clientSocket.makefile("w").writelines(
        sentence + "\n")  # se tolgo il \n rimane sempre in attesa e accetta infiniti input
    modifiedSentence = clientSocket.makefile().readline()  # leggo quello che mi ha mandato il server
    print("FROM SERVER: ", modifiedSentence)

clientSocket.close()