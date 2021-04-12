from math import e
from threading import Lock, Thread, RLock, Condition
from time import sleep
from random import randrange


class ContoBancario:
    idx=0
    def __init__(self) -> None:
        self.saldo = randrange(100, 1000)
        self.elencoTransazioni = []
        self.idx=ContoBancario.idx
        ContoBancario.idx+=1

    def setSaldo(self, v):
        self.saldo += v

    def getSaldo(self):
        return self.saldo
    
    def addTransazioni(self,t):
        self.elencoTransazioni.append(t)


class Transazione:
    def __init__(self, cA: ContoBancario, cB: ContoBancario, v:int) -> None:
        self.sorgente = cA
        self.destinazione = cB
        self.valore = v

class Banca:
    def __init__(self) -> None:
        self.lock = RLock()
        self.elencoConti=[]

    def getSaldo(self, c: ContoBancario):
        with self.lock:
            return c.getSaldo()

    def trasferisci(self, a: ContoBancario, b: ContoBancario, n: int):
        with self.lock:
            if a.getSaldo() < n:
                return False

            a.setSaldo(-n)
            b.setSaldo(n)
            tA=Transazione(a,b,-n)
            tB=Transazione(a,b,n)
            a.addTransazioni(tA)
            b.addTransazioni(tB)
            return True

    def aggiungiConto(self):
        with self.lock:
            c=ContoBancario()
            self.elencoConti.append(c)

class Cliente(Thread):
    def __init__(self) -> None:
        super().__init__()
    
    def run(self) -> None:
        