from threading import Thread,Lock,Condition
from time import sleep
from random import random,randint


class PivotBlockingQueue:

    
    def __init__(self, n:int) -> None:
        self.queue=[]
        self.n=n
        self.lock=Lock()
        self.condition=Condition(self.lock)
        self.prendo=False #se false prendo minimo
                    #se true prendo max

    def take(self) -> int:
        with self.lock:
            while len(self.queue)<2:
                self.condition.wait()
            
            self.rimuoviPivot()
            return self.queue.pop()

    def rimuoviPivot(self):
        pos=0
        min=10000000
        max=0
        if(self.prendo==True):
            for i in self.queue:
                if(max<self.queue[i]):
                    max=self.queue[i]
                    pos=i

        if(self.prendo==False):
            for i in self.queue:
                if(min>self.queue[i]):
                    min=self.queue[i]
                    pos=i

        self.queue.remove(pos)

    def put(self,t:int):
        with self.lock:
            while(len(self.queue) == self.n):
                self.rimuoviPivot()
            
            self.queue.append(t)
            if len(self.queue)==2:
                self.condition.notify()


    def setCriterioPivot(self,minMax:bool):
        with self.lock:
            if minMax == True:
                prendo=False
            else:
                prendo=True

class Operator(Thread):
    def __init__(self,c) -> None:
        super().__init__()
        self.coda=c
    
    def run(self):
        for i in range(1000):
            sleep(random())
            self.coda.put(randint(-100,100))
            sleep(random())

if __name__ == '__main__':
    coda=PivotBlockingQueue(10)
    operatori = [Operator(coda) for i in range(50)] 
    for o in operatori:
        o.start()