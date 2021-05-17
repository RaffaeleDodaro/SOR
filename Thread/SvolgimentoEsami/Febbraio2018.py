from threading import Thread,RLock,Condition

class SharedInteger:
    def __init__(self,n):
        self.n=n
        self.lock=RLock()
        self.condition=Condition(self.lock)

    def get(self):
        with self.lock:
            return self.n

    def set(self,i):
        with self.lock:
            self.n=i
            self.condition.notify_all()

    def inc(self,i):
        with self.lock:
            self.n+=i
            self.condition.notify_all()

    def inc(self,i:int):
        with self.lock:
            self.n+=i
            self.condition.notify_all()

    def waitForAtLeast(self,soglia):
        with self.lock:
            while self.n<soglia:
                self.condition.wait()
            return self.n

    def setInTheFuture(self,i,soglia,valore):
        with self.lock:
            while i<soglia:
                self.condition.wait()
            self.condition.notify_all()
            self.n=valore