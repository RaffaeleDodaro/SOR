from threading import Thread, Lock
import random
from time import sleep
from typing import MappingView

class Striscia():
    def __init__(self):
        self.s = list()
        self.mangiato = False
        self.dirGatto = 1
        self.lung = 20
        self.posTopo = random.randint(0, self.lung-1)
        self.posGatto = random.randint(0, self.lung-1)
        self.lock = Lock()
        for i in range(0, self.lung):
            self.s.append(' ')
        self.s[self.posTopo] = '.'
        self.s[self.posGatto] = '*'

    def stampaStriscia(self):
        with self.lock:
            print("|%s|" % ''.join(self.s))
            return self.mangiato

    def muoviGatto(self):
        with self.lock:
            if self.mangiato:
                return True
            self.s[self.posGatto] = ' '
            self.posGatto += self.dirGatto
            if (self.posGatto > self.lung-1 or self.posGatto < 0):
                self.dirGatto = -self.dirGatto
                self.posGatto += 2 * self.dirGatto

            if (self.posGatto == self.posTopo):
                self.mangiato = True
                self.s[self.posGatto] = '@'
                return True

            self.s[self.posGatto] = '*'
            return False

    def muoviTopo(self):
        with self.lock:
            if self.mangiato == True:
                return True
            self.s[self.posTopo] = ' '

            self.salto = random.randint(-1, 1)
            if (self.posTopo + self.salto >= 0 and self.posTopo + self.salto < self.lung):
                self.posTopo = self.posTopo + self.salto

            if (self.posGatto == self.posTopo):
                self.mangiato = True
                self.s[self.posTopo] = '@'
                return True

            self.s[self.posTopo] = '.'
            return False


class Display(Thread):
    def __init__(self, s: Striscia):
        Thread.__init__(self)
        self.s = s

    def run(self):
        while not self.s.stampaStriscia():
            sleep(0.020)


class Gatto(Thread):
    # Gatto: muove periodicamente di una posizione il gatto. Il gatto si muove da sinistra a destra
    # fino al bordo destro della striscia, per poi alternativamente cominciare a muoversi da destra
    # fino al bordo sinistro, finchè non si sovrappone al topo.
    def __init__(self, s: Striscia):
        Thread.__init__(self)
        self.s = s

    def run(self):
        while not self.s.muoviGatto():
            sleep(0.100)


class Topo(Thread):
    # Topo: muove periodicamente di una posizione il topo. Il topo decide casualmente di stare
    # fermo, o di muoversi di una casella a destra, a sinistra, finchè non viene raggiunto dal gatto
    # (Il topo potrebbe anche finire addosso al gatto).
    def __init__(self, s: Striscia):
        Thread.__init__(self)
        self.s = s

    def run(self):
        while not self.s.muoviTopo():
            sleep(0.050)


def main():
    striscia = Striscia()
    jerry = Topo(striscia)
    tom = Gatto(striscia)
    display = Display(striscia)
    print("Created")
    display.start()
    jerry.start()
    tom.start()
    print("Started")
    sleep(10)


if __name__ == "__main__":
    main()
