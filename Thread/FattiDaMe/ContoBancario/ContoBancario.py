from threading import Thread, Lock, Condition
import random

class Transazione():
    def __init__(self, m, d, importo):
        self.t = (m, d, importo)

class ContoBancario(Thread):
    idConto=0
    def __init__(self):
        self.idConto=ContoBancario.idConto
        super().__init__()
        self.saldo = random.randint(0,50)
        self.elencoTransazioni = list()
        self.lock = Lock()
        ContoBancario.idConto+=1

    def addTransazione(self, t:Transazione):
            self.elencoTransazioni.append(t)
        
class Conti(set):
    def __init__(self):
        self.lock= Lock()
    
    def add(self,c:ContoBancario):
        with self.lock:
            super().add(c)

class Banca(Thread):
    def __init__(self):
        super().__init__()
        self.contiBancari = Conti()
        self.lock = Lock()
        self.condition=Condition(self.lock)

    def getSaldo(self, c: ContoBancario):
            return c.saldo

    def setSaldo(self, c: ContoBancario, n):
        with self.lock:
            c.saldo += n

    def addConto(self, c:ContoBancario):
        self.contiBancari.add(c)

    def trasferisci(self, a: ContoBancario, b: ContoBancario, n: int):
        with self.lock:
            if(self.getSaldo(self.a) < n):
                return ValueError("saldo insufficiente")

            self.setSaldo(a, -n)
            self.setSaldo(b, n)
            t = Transazione(a, b, n)
            a.addTransazione(self.t)
            b.addTransazione(self.t)
            return True


class Cliente(Thread):
    def __init__(self, b, c):
        super().__init__()
        self.b = b
        self.c = c

    def getRand(self):
        return self.c[random.randint(0,len(self.c))]

    def run(self):
        a = self.getRand()
        b = self.getRand()
        n = random.randint(0,1000)

        self.b.prendiLock(a, b)
        if self.b.trasferisci(a, b, n):
            print(f"{a} ha trasferito {n} euro a {b}")
        else:
            print(f"Transazione da {a} a {b} non riuscita :(")
        self.b.lasciaLock(a, b)

class CreaThread(Thread):
    def __init__(self,b:Banca,c:ContoBancario):
        super().__init__()
        self.b=b
        self.c=c

    def run(self):
        while True:
            c=Cliente(self.b,self.c)
            c.start()



b = Banca()
c = [ContoBancario() for i in range(5)]
for e in c:
    b.addConto(e)

ct = CreaThread(b, c)
ct.start()
