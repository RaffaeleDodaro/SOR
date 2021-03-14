from threading import Thread,RLock,Condition
from random import randrange,random
from time import sleep
from queue import Queue

class PivotBlockingQueue:
    def __init__(self,n) -> None:
        self.n=n
        self.theBuffer=[]
        self.lock=RLock()
        self.condition=Condition(self.lock)
        self.criterio=0 # 0 = prendo il minimo

    def individuaPivot(self):
        elemento=self.theBuffer[0]
        if self.criterio==0:
            for i in self.theBuffer:
                if self.theBuffer[i]<=elemento:
                    elemento=i
        elif self.criterio==1:
            for i in self.theBuffer:
                if self.theBuffer[i]>=elemento:
                    elemento=i
        return elemento

    def take(self):
        with self.lock:
            while len(self.theBuffer)<2:
                self.condition.wait()
            self.theBuffer.pop(self.individuaPivot())
            return self.theBuffer.pop()

    def put(self,t:int):
        with self.lock:
            if len(self.theBuffer) == self.n:
                # individua ed elimina l’elemento PIVOT,
                # quindi inserisce subito l’elemento T
                indice=self.individuaPivot()
                self.theBuffer.pop(indice)
            else:
                self.theBuffer.append(t)
            
            if(len(self.theBuffer)>1):
                self.condition.notifyAll()

    def setCriterioPivot(self, minMax:bool):
        with self.lock:
            if minMax:
                self.criterio=0
            else:
                self.criterio=1


class Operator(Thread):
    def __init__(self,p) -> None:
        super().__init__() 
        self.p=p
    def run(self):
        for i in range(1000):
            sleep(random())
            self.p.put(randrange(0,50))
            sleep(random())
            self.p.take()


p=PivotBlockingQueue(10)
o=[Operator(p) for i in range(50)]
for op in o:
    op.start()
