import random, time, os
from threading import Lock, Thread,Condition,RLock
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

    def shift(self, m:int):
        with self.lock:
            self.appoggio=[None * self.n]

    def shift(self,i:int,v:int,d:int):
        if d==1:
            pass
        elif(d==0):
            pass

    def get(self,i:int,d=int):
        if d==1:
            pass
        elif(d==0):
            pass