from socket import *

serverPort=6789 #creo listening socket
welcomeSocket=socket()
welcomeSocket.bind(('',serverPort)) #'' significa "mettiti in ascolto su tutte le interfacce che hai". bind significa attacca la spina al socket stesso
welcomeSocket.listen(5)#mettimi in listen. 5 rappresenta il numero di telefonate che posso bufferizzare. al massimo voglio 5 buffer

while True:

    connectionSocket,addr=welcomeSocket.accept() #accept dice: vai nel buffer delle telefonate ed estraine una. se il buffer e' vuoto accept e' bloccante.
                                                #appena arriva una palluzza(telefonata) io la estraggo. le telfonate le estraggo una alla volta
                                                # accept quando c'e' una palluzza restituisce i dati della palluzza, in particolare restituisce una coppia.
                                                # come primo valore c'e' connectionSocket che e' un socket che e' gia' collegato con un'estremita' all'altra parte
                                                # una volta fatto accetp la connessione e' gia' partita
                                                # addr mi dice chi sono i comunicanti
    print(addr)
    clientSentence=connectionSocket.makefile().readline() #readline legge tutti i byte che vede fino a quando non legge un fine riga
    capitalizedSentence=clientSentence.upper()

    connectionSocket.makefile("w").writelines(capitalizedSentence+'\n')
    connectionSocket.close()