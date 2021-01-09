# La libreria deve consentire di eseguire la somma e la sottrazione tra due vettori (di pari
# lunghezza), facendo uso dei processori a disposizione. A tal proposito si può usare la funzione predefinita
# Runtime.getRuntime().availableProcessors() che restituisce il numero di processori a disposizione sul PC in
# cui gira il programma da progettare.

# Si progetti quindi la classe Operazioni preposta allo scopo.
# La classe deve essere dotata del metodo int[] somma(int[] V1, int[] V2) che ritorna un nuovo
# vettore dato dalla somma elemento per elemento dei vettori puntati V1 e V2, e dell’analogo metodo int[]
# sottrai(int[] V1, int[] V2).
# Ad esempio se A = [1,4,7,8,12] e B = [1,2,1,2,1], allora somma(A,B) = [2,6,8,10,13], mentre sottrai(A,B) =
# [0,2,6,6,11].
# La classe deve essere progettata in maniera tale da far uso del numero di thread ideale: ad esempio se
# getProcessori() = 4, può convenire effettuare la somma in parallelo usando 4 thread.
# È parte integrante dell’esercizio completare le specifiche date nei punti non esplicitamente definiti, e
# risolvere eventuali ambiguità.
import multiprocessing
from threading import Thread, Lock, Condition, Barrier
from random import random
from multiprocessing import cpu_count
from time import time

def faiSommaSeq(min: int, max: int, v1, v2):
    sommaTotale = 0
    for i in range(min, max):
        sommaTotale += v1[i]+v2[i]
        print("somma totale:"+"  passo  \n", sommaTotale, i)
    return sommaTotale


class Macinatore(Thread):
    def __init__(self, min: int, max: int, b: Barrier, v1, v2):
        Thread.__init__(self)
        self.min = min
        self.max = max
        self.totale = [None for i in range(self.max)]
        self.barrier = b
        self.v1 = v1
        self.v2 = v2

    def getTotale(self):
        self.totale

    def run(self):
        for i in range(self.min, self.max):
            self.totale[i] = self.v1[i+self.min]+self.v2[i+self.max]
        self.barrier.wait()

class Operazioni:
    def __init__(self):
        pass

    def somma(self, v1: int, v2: int):
        if len(v1) != len(v2):
            return 0

        threadReali = multiprocessing.cpu_count()
        fettina = len(v1)//threadReali
        while fettina == 0:
            threadReali -= 1
            fettina = len(v1)//threadReali
            print("Userò {} core". format(threadReali))

        print(f"numberForThread {fettina}  ---- --   thread: {threadReali}")
        ciucci = [None for i in range(0, threadReali)]
        b = Barrier(threadReali+1)
        min = 0
        for i in range(threadReali-1):
            ciucci[i]=Macinatore(min, threadReali, b, v1, v2)
            min += threadReali
            ciucci[i].start()

        ciucci[threadReali-1]=Macinatore(min, len(v1)-min, b, v1, v2)
        ciucci[threadReali-1].start()
        b.wait()

        totale = []
        for i in range(0, len(v1)-1):
            totale.append(ciucci[i].getTotale())
        return totale

    def sottrazione(self, v1: int, v2: int):
        pass


v1 = [1, 4, 7, 8, 12]
v2 = [1, 2, 1, 2, 1]
print("v1: ", v1)
print("v2: ", v2)
o=Operazioni()
print(f"Somma: {o.somma(v1,v2)}")
