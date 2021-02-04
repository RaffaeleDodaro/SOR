from threading import Thread, Lock, Condition
from random import randrange

class CLock:
    def __init__(self, n: int):
        self.permessi = n
        self.lock = Lock()
        self.conditionAcquire = Condition(self.lock)
        self.esisteLimite = False
        self.limite = 0

    def acquire(self):
        with self.lock:
            while(self.permessi == 0):
                self.conditionAcquire.wait()
            self.permessi -= 1

    def release(self):
        with self.lock:
            if not self.esisteLimite:
                self.permessi+=1
            else:
                if((self.permessi) == self.limite):
                    return
            self.permessi+=1
            self.conditionAcquire.notifyAll()

    def limita(self, n: int):
        with self.lock:
            self.esisteLimite = True
            self.limite = n

    def getPermessi(self) -> int:
        return self.permessi

    def getPermessiMax(self) -> int:
        with self.lock:
            return self.limite



def main():
    c = CLock(3)
    print(c.getPermessi())
    
    c.limita(5)
    print(c.getPermessi())
    
    c.release()
    print(c.getPermessi())
    
    c.release()
    print(c.getPermessi())
    
    c.release()
    print(c.getPermessi())
    
    c.acquire()
    print(c.getPermessi())


if __name__ == '__main__':
    main()