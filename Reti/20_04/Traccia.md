Provate a scrivere un TCPserver che produce molti più dati di quanti il TCPclient ne elabori 
(è sufficiente che il server faccia abbondanti writelines continuative, mentre il client fa 
una readline alternata a una sleep(10)). Osservate ora il dialogo tra i due interlocutori con 
wireshark e annotate l'andamento del campo Win=? nel flusso Server->Client e nel flusso 
Client->Server. Cosa succede quando il client risponde con un segmento che valorizza win=0?