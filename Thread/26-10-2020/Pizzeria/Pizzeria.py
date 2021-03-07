from queue import Queue
from BlockingSet import BlockingSet
from Ordine import Ordine

class Pizzeria:

    bufferOrdini = Queue(5) #uso la queue di python dato che  "la politica du gestione di BO e' FIFO".
                            # le queue in python sono bloccanti
    
    bufferPizze = BlockingSet(5) # non posso usare la queue di py perche' 
        # nel caso in cui svolgessi gli ordini nel formato queue succede che fintanto che un cliente 
        # non si sveglia per prendere le pizze, tutti gli altri non le possono prendere. 
        # questo implica che ci sarebbero attese inutili per i clienti che aspettano determinati ordini
        # alla fine la queue(OVVIAMENTE) rappresenta una FIFO/LIFO, quindi se l'ordine di G e' in [0]
        # e G e' al telefono, nel frattempo il pizzaiolo deposita la pizza di A in [1], G non puo
        # ritirare la pizza fino a quando non la ritira B
        # https://i.imgur.com/ALFS9aP.png
    def putOrdine(self, tipoPizza, quantita):
        ordine = Ordine(tipoPizza,quantita)
        self.bufferOrdini.put(ordine)
        return ordine

    def getOrdine(self):
        return self.bufferOrdini.get()

    def putPizze(self,ordine):
        self.bufferPizze.add(ordine)

    def getPizze(self,ordine):
        return self.bufferPizze.remove(ordine)
