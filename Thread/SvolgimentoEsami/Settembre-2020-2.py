from threading import Thread,RLock,Condition
from random import random
from time import sleep

#
# Funzione di stampa sincronizzata
#
plock = RLock()
def prints(s):
    plock.acquire()
    print(s)
    plock.release()

class DatoCondiviso:
    SOGLIAGIRI = 5

    def __init__(self,v):
        super().__init__(v)
        self.numScrittoriInAttesa = 0
        self.numGiriSenzaScrittori = 0
        self.lockNuovo=RLock()
        self.condition=Condition()
        self.numLettori=0
        self.entrambiScrittori=False
    def acquireTLock(self):
        while(self.numLettori>3 and self.entrambiScrittori):
            self.condition.wait()
        self.lockNuovo.acquire()
        
            

    def releaseTLock(self):
        self.condition.notifyAll()

    def acquireReadLock(self):

        self.lock.acquire()
        while self.ceUnoScrittore or (self.numScrittoriInAttesa > 0 and self.numGiriSenzaScrittori > self.SOGLIAGIRI):
            self.condition.wait()
        self.numLettori += 1
        #
        # * Il contatore viene incrementato solo se effettivamente ci sono
        # * scrittori in attesa.
        #
        
        if self.numScrittoriInAttesa > 0:
            self.numGiriSenzaScrittori += 1
        self.lock.release()

    def releaseReadLock(self):
        self.lock.acquire()
        self.numLettori -= 1
#
# Nella versione senza starvation, possono esserci anche dei lettori in attesa.
# E' necessario
# dunque svegliare tutti.
#
        if self.numLettori == 0:
            self.condition.notify_all()
        self.lock.release()

    def acquireWriteLock(self):
        self.lock.acquire()
        self.numScrittoriInAttesa += 1
        while self.numLettori > 0 or self.ceUnoScrittore:
            self.condition.wait()
        self.ceUnoScrittore = True
        self.numScrittoriInAttesa -= 1
        self.numGiriSenzaScrittori = 0
        self.lock.release()

    def releaseWriteLock(self):
        self.lock.acquire()
        self.ceUnoScrittore = False
        self.condition.notify_all()
        self.lock.release()

class Scrittore(Thread):
    maxIterations = 1000
    def __init__(self, i, dc):
        super().__init__()
        self.id = i
        self.dc = dc
        self.iterations = 0
    
    def run(self):
        while self.iterations < self.maxIterations:
            prints("Lo scrittore %d chiede di scrivere." % self.id)
            self.dc.acquireWriteLock()
            prints("Lo scrittore %d comincia a scrivere." % self.id )
            sleep(random())
            self.dc.setDato(self.id)
            prints("Lo scrittore %d ha scritto." % self.id)
            self.dc.releaseWriteLock()
            prints("Lo scrittore %d termina di scrivere." % self.id)
            sleep(random() * 5)
            self.iterations += 1

class Lettore(Thread):
    maxIterations = 100
    
    def __init__(self, i, dc):
        super().__init__()
        self.id = i
        self.dc = dc
        self.iterations = 0
    
    def run(self):
        while self.iterations < self.maxIterations:
            prints("Il lettore %d Chiede di leggere." % self.id)
            self.dc.acquireReadLock()
            prints("Il lettore %d Comincia a leggere." % self.id)
            sleep(random())
            prints("Il lettore %d legge." % self.dc.getDato())
            self.dc.releaseReadLock()
            prints("Il lettore %d termina di leggere." % self.id)
            sleep(random() * 5)
            self.iterations += 1

if __name__ == '__main__':
    dc = DatoCondiviso(999)
    NUMS = 5
    NUML = 5
    scrittori = [Scrittore(i,dc) for i in range(NUMS)]
    lettori = [Lettore(i,dc) for i in range(NUML)]
    for s in scrittori:
        s.start()
    for l in lettori:
        l.start()