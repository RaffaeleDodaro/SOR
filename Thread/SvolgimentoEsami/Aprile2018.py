from threading import Thread,RLock,Condition

class BlockingQueuePool:
    def __init__(self,n,m,t):
        self.n=n
        self.thebuffers=[[]for i in range(0,self.n)]
        self.lock=RLock()
        self.condition=[Condition(self.lock) for i in range(0,self.n)]
        self.codaPut=-1


    def put(self,t):
        with self.lock:
            while self.thebuffers[self.codaPut]==self.m:
                self.condition.wait()

    def take(self):
        pass

    def nextPut(self):
        pass

    def nextTake(self):
        pass