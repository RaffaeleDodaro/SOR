import random, time, os
from threading import Lock, Thread,Condition,RLock
from queue import Queue

class BlockingStack:
    def __init__(self,n:int) -> None:
        self.n=n
        self.theBuffer=[]
        self.slotInseriti=0
        self.ins=0
        self.out=0
        self.lock=Lock()
        self.condition=Condition(self.lock)

    def put(self,t):
        with self.lock:
            while self.slotInseriti==self.n:
                self.condition.wait()
            

            self.slotInseriti+=1
            self.condition.notify()
            self.theBuffer.append(t)
            

    def take(self):
        with self.lock:
            while self.slotInseriti==0:
                self.condition.wait()
            
            if self.slotInseriti==self.n:
                self.condition.notify()

            self.slotInseriti+=1
            return self.theBuffer.pop(0)

    def take(self,t):
        with self.lock:
            while not t in self.theBuffer:
                self.condition.wait()
            
            if self.slotInseriti==self.n:
                self.condition.notify()

            self.theBuffer.remove(t)
            return t