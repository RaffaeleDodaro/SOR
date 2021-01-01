from threading import Condition, Thread, Lock
from random import random
import time


class BlockingQueue():
    def __init__(self, dim):
        self.slotPieni = 0
        self.dim = dim
        self.thebuffer = [None] * dim
        self.out = 0
        self.lock = Lock()
        self.attesa_condition = Condition(self.lock)
        self.lavora_condition = Condition(self.lock)

    def aggiungiCliente(self):
        with self.lock:
            if self.slotPieni == self.dim:
                raise ValueError("Array pieno")
            self.slotPieni += 1
            while self.slotPieni > 1:
                self.attesa_condition.wait()
            self.thebuffer[self.slotPieni] = '*'
            self.lavora_condition.notifyAll()

    def rimuoviCliente(self):
        with self.lock:
            if self.out >= (self.dim-1):
                self.out = 0
            self.out += 1
            self.thebuffer[self.out] = '-'
            self.thebuffer[0] = ' '
            while self.slotPieni == 0:
                self.lavora_condition.wait()
            self.attesa_condition.notifyAll()
            self.slotPieni -= 1

    def stampa(self):
        with self.lock:
            print(f"Stanno aspettando {self.slotPieni} clienti")
            #print(self.thebuffer)



class Barbiere(Thread):
    def __init__(self, b: BlockingQueue):
        Thread.__init__(self)
        self.b = b

    def run(self):
        while True:
            time.sleep(random()*2)
            self.b.rimuoviCliente()
            self.b.stampa()


class Cliente(Thread):
    def __init__(self, b: BlockingQueue):
        Thread.__init__(self)
        self.b = b

    def run(self):
        while True:
            time.sleep(random()*5)
            self.b.aggiungiCliente()
            self.b.stampa()


queue = BlockingQueue(11)
clienti = [Cliente(queue) for i in range(0, 7)]
b = Barbiere(queue)
b.start()
for e in clienti:
    e.start()
