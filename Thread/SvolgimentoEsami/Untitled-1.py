from threading import Thread, Lock, RLock, Condition
from time import sleep
from collections import deque
from random import random


class RoundRobinLock:
    def __init__(self, n: int) -> None:
        self.n = n
        self.thebuffer = [None for i in range(0, self.n)]
        self.lock = RLock()
        self.condition = [Condition(self.lock) for i in range(0, self.n)]
        self.possessori = 0
        self.idProprietario = -1
        self.richiesteId = [0 for i in range(0, self.n)]

    def acquire(self, id: int):
        with self.lock:
            self.richiesteId[id] += 1
            while self.possessori > 0 and self.idProprietario != id:
                self.condition[id].wait()

            self.possessori += 1
            self.richiesteId[id] -= 1

    def release(self, id: int):
        with self.lock:
            self.possessori-=1
            if self.possessori == 0:
                for i in range(0, self.n):
                    turno = (id+i) % self.n
                    if self.richiesteId[turno] > 0:
                        self.idProprietario = turno
                        self.condition[turno].notifyAll()
                        break
