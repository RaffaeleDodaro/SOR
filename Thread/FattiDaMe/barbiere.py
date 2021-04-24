from threading import Thread, RLock, Condition
from time import sleep
from random import randrange, random


class RunningSushiBuffer:
    def __init__(self, n):
        self.n = n
        self.lock = RLock()
        self.conditionCuoco = Condition(self.lock)
        self.conditionCliente = Condition(self.lock)
        self.thebuffer = [None for i in range(0, self.n)]
        self.zeroOccupata = False
        self.zeroPosition=0

    def put(self, t):
        with self.lock:
            while self.zeroOccupata:
                self.conditionCuoco.wait()  # SVEGLIALA
            self.thebuffer[0] = t

    def get(self, i: int):
        with self.lock:
            if i < 1 or i > self.n - 1:
                raise ValueError

            while self.thebuffer[i] is None:
                self.conditionCliente.wait()  # SVEGLIALA
            e=self.thebuffer[i]
            self.thebuffer.pop(e)
            return e

    def shift(self, j: int):
        with self.lock:
            self.conditionCliente.notify_all()
            self.conditionCuoco.notify_all()
            self.zeroPosition=(self.zeroPosition-j)%self.n


    def shift(self):
        self.shift(1)
