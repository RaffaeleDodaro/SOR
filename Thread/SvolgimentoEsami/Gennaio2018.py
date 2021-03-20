from threading import Thread, Lock, RLock, Condition
from random import random, randint
from time import sleep

class RunningSushiBuffer:
    def __init__(self,n) -> None:
        self.n=n
        self.zeroPosition=0
        self.lock=RLock()
        self.condition=Condition()
        self.thebuffer=[]
        for i in range(0,n):
            self.thebuffer[i]=None
        self.zeroOccupato=False

    def _om(self,i):
        with self.lock:
            pass

    def put(self,t):
        with self.lock:
            while self.thebuffer[self._om(0)]!=None:
                self.condition.wait()
            
            self.thebuffer[self._om(0)]=t

    def get(self,i):
        with self.lock:
            if i<1 or i>self.n-1:
                ValueError

            while self.thebuffer[i]==None:
                self.condition.wait()
            v=self.thebuffer[self._om(i)]
            self.thebuffer[self._om(i)]=None
            return v


    def shift(self,j):
        with self.lock:
            self.zeroPosition = (self.zeroPosition - j) % self.n
            self.condition.notifyAll()

    def shift(self):
        self.shift(1)