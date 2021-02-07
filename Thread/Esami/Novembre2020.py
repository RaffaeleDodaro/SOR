from threading import Thread, RLock, Condition
from random import randint
debug = True


class RoundRobinLock:
    def __init__(self, N: int):
        self.nturni = N
        self.lock = RLock()
        self.conditions = [Condition(self.lock) for _ in range(0, N)]
        self.inAttesa = [0 for _ in range(0, N)]
        self.turnoCorrente = 0
        self.possessori = 0
        self.presidente = -1
        self.presidentWaiting = 0

    def setPresident(self, id: int):
        with self.lock:
            self.presidente = id

    def urgentAcquire(self):
        with self.lock:
            self.presidentWaiting += 1

            #mentre il lock è occupato da un non presidente
            while ((self.presidente != self.turnoCorrente ) 
                    and (self.possessori > 0)):
                self.conditions[self.presidente].wait()#facciamo attendere il presidente
            self.possessori += 1
            self.presidentWaiting -= 1

#
# Non c'è bisogno di particolare attenzione alla gestione del primo accesso
#
    def acquire(self, id: int):
        with self.lock:
            self.inAttesa[id] += 1
            while(self.possessori > 0 and self.turnoCorrente != id
                    or id != self.presidente and self.presidentWaiting > 0):
                self.conditions[id].wait()
            self.inAttesa[id] -= 1
            self.possessori += 1
            if debug:
                self.__print__()

    def release(self, id: int):
        with self.lock:
            self.possessori -= 1
            # and self.inAttesa[self.turnoCorrente] ==0:
            if self.possessori == 0:
                if self.turnoCorrente == self.presidentGroupID: # se è il turno del presidente
                    # ricomincio la turnazione da dove avevo sospeso
                    self.turnoCorrente = self.turnoSospeso
                if self.presidentsWaiting == 0: # se non ho presidenti in attesa
                    for i in range(1, self.nturni):
                        turno = (id + i) % self.nturni
                        if self.inAttesa[turno] > 0:
                            self.turnoCorrente = turno
                            self.conditions[turno].notifyAll()
                            break
                else: # se ho presidenti in attesa hanno la precedenza
                    # faccio un backup del livello in cui mi trovo
                    self.turnoSospeso = self.turnoCorrente
                    self.turnoCorrente = self.presidente
                    #risveglio i presidenti in attesa
                    self.conditions[self.presidentGroupID].notifyAll()
            if debug:
                self.__print__()

    def __print__(self):
        with self.lock:
            print("=" * self.turnoCorrente + "|@@|" + "=" *
                  (self.nturni - self.turnoCorrente - 1))
            for l in range(0, max(max(self.inAttesa), self.possessori)):
                o = ''
                for t in range(0, self.nturni):
                    if self.turnoCorrente == t:
                        if self.possessori > l:
                            o = o + "|o"
                        else:
                            o = o + "|-"
                    if self.inAttesa[t] > l:
                        o = o + "*"
                    else:
                        o = o + "-"
                    if self.turnoCorrente == t:
                        o = o + "|"
                print(o)
            print("")


class RoundRobinLockStarvationMitigation(RoundRobinLock):
    SOGLIASTARVATION = 5

    def __init__(self, N: int):
        super().__init__(N)
        self.consecutiveOwners = 0

    def acquire(self, id: int):
        with self.lock:
            self.inAttesa[id] += 1
            while(self.possessori > 0 and
                    self.turnoCorrente != id or
                    self.turnoCorrente == id and
                    self.consecutiveOwners > self.SOGLIASTARVATION and
                    max(self.inAttesa) > 0
                  ):
                self.conditions[id].wait()

            self.inAttesa[id] -= 1
            self.possessori += 1
            self.consecutiveOwners += 1
            if debug:
                self.__print__()


    def release(self, id: int):
        with self.lock:
            self.possessori -= 1
            if self.possessori == 0:
                for i in range(1, self.nturni):
                    turno = (id + i) % self.nturni
                    if self.inAttesa[turno] > 0:
                        self.turnoCorrente = turno
                        self.consecutiveOwners = 0
                        self.conditions[turno].notifyAll()
                        break


class RoundRobinLockConCoda(RoundRobinLock):
    def __init__(self, N: int):
        pass

    def acquire(self, id: int):
        pass

    def release(self, id: int):
        pass


class Animale(Thread):
    def __init__(self, id: int, idTurno: int, R: RoundRobinLock):
        super().__init__()
        self.idTurno = idTurno
        self.iterazioni = 1000
        self.lock = R

    def run(self):
        while(self.iterazioni > 0):
            self.iterazioni -= 1
            self.lock.acquire(self.idTurno)
            # self.lock.__print__()
            self.lock.release(self.idTurno)


NGruppi = 5
R = RoundRobinLockStarvationMitigation(NGruppi)
#R = RoundRobinLock(NGruppi)
for i in range(0, 60):
    Animale(i, randint(0, NGruppi-1), R).start()
