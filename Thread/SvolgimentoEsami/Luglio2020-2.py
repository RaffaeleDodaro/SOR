from threading import Thread, RLock, Condition, current_thread
from random import randint

class Player(Thread):

    def __init__(self,nb):
        super().__init__()
        self.nb = nb

    def run(self):
        self.nb.puntaNumero(randint(1,10))

class NumeroBasso:
    def __init__(self):
        self.giocate = []
        self.lock = RLock()
        self.threadGioca = Condition(self.lock)
        self.partitaInCorso = False
        self.nGiocate = 0
        self.barrier = None
        self.stoGiocando=Condition(self.lock)

    def gioca(self,N : int) -> int:
        with self.lock:
            self.giocate = {}
            self.nGiocate = 0
            self.partitaInCorso = True
            for _ in range(0,N):
                Player(self).start()
            while(self.nGiocate < N):
                self.threadGioca.wait()
            self.partitaInCorso = False
            self.stoGiocando.notifyAll()
            for k in sorted(self.giocate):
                if len(self.giocate[k]) == 1:
                    print(f"Il vincitore è il thread {self.giocate[k][0]} che ha puntato il numero {k}")
                    return self.giocate[k][0]
            print("Non ci sono vincitori")
            return 0

    def puntaNumero(self,n : int):
        with self.lock:
            self.giocate.setdefault(n,[]).append(current_thread().ident)
            self.nGiocate += 1
            self.threadGioca.notify()

    
    def puntaNumeroNuovo(self,n : int):
        # si deve attendere l’esito della partita; infine va restituito un valore booleano che
        # indichi se il thread che ha appena invocato puntaNumero risulta essere quello vincente
        with self.lock:
            while(self.partitaInCorso):
                self.stoGiocando.wait()
            self.giocate.setdefault(n,[]).append(current_thread().ident)
            self.nGiocate += 1
            self.threadGioca.notify()

if __name__ == '__main__':
    gameManager = NumeroBasso()
    v = 1
    while v != 0:
        v = gameManager.gioca(10)