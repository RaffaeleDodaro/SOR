from threading import Thread, Lock, Condition
from random import random
from queue import Queue

class Ordine:
    idx=0
    def __init__(self, cp: int, quantita: int):
        self.codicePizza = cp
        self.quantita = quantita
        self.idx=Ordine.idx
        self.idx+=1
        self.pizze = ""  # mi serve per l'output

    def prepara(self):
        for i in range(0, self.quantita):
            if(self.codicePizza == 1):
                tipo = "-"
            elif self.codicePizza == 2:
                tipo = "+"
            elif self.codicePizza == 3:
                tipo = "/"
            else:
                tipo = "*"
            self.pizze += "("+tipo+")"


class Pizzeria:
    def __init__(self, dimO: int, dimP: int):
        self.lock = Lock()
        self.condition = Condition(self.lock)
        self.bo = Queue()
        self.dimO = dimO
        self.bo = [None * self.dimO]
        self.dimP = dimP
        self.bp = Queue()
        self.bp = [None * self.dimP]
        self.ordine = dict()

    def putPizze(self, o: Ordine):
        with self.lock:
            while(len(self.bp)>=self.dimP):
                self.condition.wait()
            self.bp.put(o)
            self.condition.notifyAll()

    def getPizze(self, idx: int):
        with self.lock:
            while(not idx in self.bp):
                self.condition.wait()
            p = self.bp.get(idx)
            self.condition.notifyAll()
            return p

    def putOrdine(self, o: Ordine):
        while self.dimO == len(self.bo):
            self.condition.wait()
        idxVecchio = self.idx
        self.ordine[idxVecchio] = o
        self.idx += 1
        self.condition.notifyAll()
        return idxVecchio

    def getOrdine(self):
        while len(self.bo) == 0:
            self.condition.wait()
        self.condition.notifyAll()
        return self.bo.get()

class Cliente(Thread):
    def __init__(self, p: Pizzeria):
        self.pizzeria = p
        Thread.__init__(self)

    def run(self):
        while True:
            tipoPizza = random(1, 4)
            quantita = random(1, 4)
            o = Ordine(tipoPizza, quantita)
            self.idx = self.pizzeria.putOrdine(o)
            Thread.sleep(random(1, 4)*quantita)
            self.pizzeria.getPizze(self.idx)

class Pizzaiolo(Thread):
    def __init__(self, p: Pizzeria):
        self.pizzeria = p
        Thread.__init__(self)

    def run(self):
        while True:
            o = self.pizzeria.getOrdine()
            Thread.sleep(random(1, 4)*o.quantita)
            o.prepara()
            self.pizzeria.putPizze(o)


p = Pizzeria(10, 100)
c = Cliente(p)
pizzaiolo = Pizzaiolo(p)
