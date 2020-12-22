from queue import Queue
from BlockingSet import BlockingSet
from Ordine import Ordine

class Pizzeria:

    bufferOrdini = Queue(5)
    bufferPizze = BlockingSet(5)

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
