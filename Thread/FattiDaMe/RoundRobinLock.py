from threading import Thread, RLock, Condition
from random import randrange
from time import sleep


class RoundRobinLock:
    def __init__(self, n: int):
        self.n = n
        self.theBuffer = []
        self.slotPieni = 0
        self.lock = RLock()
        self.condition = [Condition(self.lock)] * self.n
        self.idTurnoCorrente = -1

    def acquire(self, idx: int):
        with self.lock:
            # se lock e' occupato
            while self.idTurnoCorrente != -1 or self.idTurnoCorrente != id:
                self.condition[idx].wait()
            self.idTurnoCorrente = idx

    def release(self, idx: int):
        with self.lock:
            self.condition[idx].notifyAll()
