from threading import Thread, Lock, Condition
from random import randrange
from time import sleep
class Torre:
    def __init__(self):
        self.lock=Lock()
        self.conditionMattone=Condition(self.lock)
        self.conditionCemento=Condition(self.lock)
        self.torre=[]
        self.torre[0]="---"
        self.dimTorreMattone=1
        self.dimTorreCemento=2
        self.indiceMattone=1
        self.indiceCemento=1
        self.stringaMattone=""
        self.stringaCemento=""
        self.h=0

    def makeTorre(self, h:int, m:int,c:int):
        self.h=h


    def mettiMattone(self):
        with self.lock:
            if(self.h>(self.dimTorreMattone+self.dimTorreCemento)):
                if self.indiceMattone<4:
                    for i in range(0,self.indiceMattone):
                        self.stringaMattone+"*"
                    self.torre[self.dimTorreMattone]=self.stringaMattone
                else:
                    self.indiceMattone=1
                    self.stringaMattone=""
                    self.dimTorreMattone+=2
            

    def mettiCemento(self):
        with self.lock:
            if(self.h>(self.dimTorreMattone+self.dimTorreCemento)):
                if self.indiceCemento<4:
                    for i in range(0,self.indiceMattone):
                        self.stringaCemento+"-"
                    self.torre[self.dimTorreCemento]=self.stringaCemento
                else:
                    self.indiceCemento=1
                    self.stringaCemento=""
                    self.dimTorreCemento+=2

class Mattone(Thread):
    def __init__(self,t:Torre):
        super().__init__(self)
        self.t=t
    
    def run(self):
        while(True):
            sleep(0.50)
            self.t.mettiMattone()

class Cemento(Thread):
    def __init__(self,t:Torre):
        super().__init__(self)
        self.t=t
    
    def run(self):
        while(True):
            sleep(0.25)
            self.t.mettiCemento()