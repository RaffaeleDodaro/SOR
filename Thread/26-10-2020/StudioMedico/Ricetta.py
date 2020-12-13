from threading import RLock, Condition
class Ricetta:
    lock=RLock()
    condition=Condition(lock)
    medicina=None
    def attendiEsito(self):
        self.lock.acquire()
        while self.medicina==None:
            self.condition.wait()
        
        self.lock.release()

    def ricettaPronta(self):
        self.lock.acquire()
        self.condition.notifyAll()
        self.lock.release()
    
    

