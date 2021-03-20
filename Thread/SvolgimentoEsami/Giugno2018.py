import random, time, os
from threading import Thread,Condition,RLock
from queue import Queue

class DischiConcentrici:
    def __init__(self,n:int) -> None:
        self.in=[]
        self.out=[]
        self.n=n
        for i in range(0,n):
            self.in[i]=None
            self.out[i]=None
        self.lock=RLock()
        self.condition=Condition(self.lock)
        self.shiftAttuale=0

    def _om(self,i):
        with self.lock:
            return (i + self.shiftAttuale) % self.size

    def shift(self, m:int):
        with self.lock:
            self.shiftAttuale+=m

    def set(self,i:int,v:int,d:int):
        with self.lock:
            if d==1:
                self.out[self._om(i)]=v
            elif(d==0):
                self.out[i]=v
            if self.in[i]==self.out[self._om(i)]:
                self.in[i]=0
                self.out[self._om(i)]=0
            elif v!=0:
                self.condition.notifyAll()


    def get(self,i:int,d=int):
        with self.lock:
            while (d==1 and self.in[i]==0) or (d==0 and self.out[self._om(i)==0]):
                    self.condition.wait()
            
            if d==1:
                return self.in[i]
                
            elif(d==0):
                return self.out[self._om(i)]