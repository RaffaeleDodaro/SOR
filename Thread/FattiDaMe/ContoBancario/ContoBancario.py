from threading import Thread, Lock, Condition
from random import randint
from queue import Queue

class Transazione:
    def __init__(self, a, b, n):
        self.t = (a, b, n)

class ContoBancario:
    numeroConto = 0

    def __init__(self):
        self.numeroConto = ContoBancario.numeroConto
        self.saldo = randint(0,50)
        self.transazioni = Queue()
        self.lock = Lock()
        ContoBancario.numeroConto += 1
        self.occupato = False
        
    def addTransazione(self, t: Transazione):
        self.transazioni.put(t)

    def getOccupato(self):
        return self.occupato

    def prendi(self):
        self.occupato = True

    def lascia(self):
        self.occupato = False

    def __str__(self):
        with self.lock:
            return "Il conto " + str(self.numeroConto)

class Conti(set):
    def __init__(self):
        self.lock = Lock()

    def add(self, conto: ContoBancario):
        with self.lock:
            super().add(conto)

class Banca:
    def __init__(self):
        self.conti = Conti()
        self.lock = Lock()
        self.condition = Condition(self.lock)

    def getSaldo(self, c: ContoBancario):
        return c.getSaldo()

    def addConto(self, c: ContoBancario):
        self.conti.add(c)

    def prendiLock(self, a: ContoBancario, b: ContoBancario):
        with self.lock:
            # if one of the two elem are busy, the thread go to wait.
            while (a.getOccupato() or b.getOccupato()):
                self.condition.wait()

            a.prendi()
            b.prendi()

    def lasciaLock(self, a: ContoBancario, b: ContoBancario):
        with self.lock:
            self.condition.notifyAll()  # notifyAll because the thread take all of two elem
            a.lascia()
            b.lascia()

    def trasferisci(self, a: ContoBancario, b: ContoBancario, n):
        if (a.saldo < n):
            return False

        a.saldo -= n
        b.saldo += n
        t = Transazione(a, b, n)
        a.addTransazione(t)
        b.addTransazione(t)
        return True


class Client(Thread):
    def __init__(self, b, c):
        Thread.__init__(self)
        self.b = b
        self.c = c

    def getRand(self):
        return self.c[randint(0,len(self.c))]

    def run(self):
        a = self.getRand()
        b = self.getRand()
        n = randint(0,20)

        self.b.prendiLock(a, b)
        if self.b.trasferisci(a, b, n):
            print(f"{a} ha trasferito {n} euro a {b}")
        else:
            print(f"Transazione da {a} a {b} non riuscita :(")
        self.b.lasciaLock(a, b)

class Generator(Thread):
    def __init__(self, b, c):
        Thread.__init__(self)
        self.b = b
        self.c = c

    def run(self):
        while True:
            c = Client(self.b, self.c)
            c.start()



b = Banca()
c = [ContoBancario() for i in range(20)]
for elem in c:
    b.addConto(elem)

g = Generator(b, c)
g.start()
