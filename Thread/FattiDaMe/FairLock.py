from threading import Thread, Lock, RLock, Condition
from time import sleep
from collections import deque
from random import random

debug = True


class FairLock():

    def __init__(self):
        #
        # Lock interno per la gestione della struttura dati
        #
        self.lock = RLock()
        #
        # Tiene traccia dello stato del lock
        #
        self.occupato = False
        #
        # Tiene traccia della prossima condition da notificare
        #
        self.nextThreadCondition = None
        #
        # Pila LIFO di condition di attesa in urgentAcquire
        #
        self.pilaUrgenti = deque()
        #
        # Coda FIFO di condition di attesa in acquire
        #
        self.codaNormali = deque()
        #
        # Gestione starvation
        #
        self.starvationControl = 0
        self.contaConsecutivi = 0

    def acquire(self):
        with self.lock:
            myCondition = Condition(self.lock)
            while self.occupato:
                self.codaNormali.append(myCondition)
                myCondition.wait()
            self.occupato = True

    def urgentAcquire(self):
        with self.lock:
            myCondition = Condition(self.lock)
            while self.occupato:
                self.pilaUrgenti.append(myCondition)
                myCondition.wait()
            self.occupato = True
            self.contaConsecutivi += 1

    def release(self):
        with self.lock:
            self.occupato = False

            starvationControlActive = (
                    self.starvationControl > 0 and
                    len(self.codaNormali) > 0 and
                    self.contaConsecutivi >= self.starvationControl
            )
            #
            # La starvation e l'ordine di risveglio vengono gestiti
            # decidendo quale condition notificare
            #
            if len(self.pilaUrgenti) > 0 and not starvationControlActive:
                self.nextThreadCondition = self.pilaUrgenti.pop()
                self.nextThreadCondition.notify()
            elif len(self.codaNormali) > 0:
                self.nextThreadCondition = self.codaNormali.popleft()
                self.nextThreadCondition.notify()
                self.contaConsecutivi = 0

    def setStarvationControl(self, n: int):
        with self.lock:
            self.starvationControl = n
