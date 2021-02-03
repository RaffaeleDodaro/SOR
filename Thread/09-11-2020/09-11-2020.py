# cyclic barrier

from multiprocessing import cpu_count
from threading import Thread, Condition, Lock
import math
import time


def eprimo(n: int) -> bool:
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True


# conta primi sequenziale
def contaPrimiSeq(min: int, max: int) -> int:
    totale = 0
    for i in range(min, max+1):
        if(eprimo(i)):
            totale += 1

    return totale


# programma multithread, partizionamento a blocchi


# class Macinatore(Thread):
#     def __init__(self, min, max):
#         Thread().__init__(self)
#         self.min = min
#         self.max = max
#         self.totale = 0

#     def getTotale(self):
#         return self.totale

#     def run(self):
#         self.totale = contaPrimiSeq(self.min, self.max)


# def contaPrimiMultiThread(min, max):

#     if max < min:
#         return 0

#     threadReali = 4  # vedere che scegliere
#     # fettina = (max - min) / tr --> foto 1

#     fettina = (max - min) // threadReali  # // è la divisione intera

#     ciucci = []

#     for i in range(threadReali-1):  # l'ultimo thread lo vado ad inizializzare a riga 67
#         minI = min+i*fettina
#         # -1 perché non voglio sovrapporre il calcolo con il thread successivo
#         maxI = minI+fettina-1
#         ciucci.append(Macinatore(minI, maxI))
#         ciucci[i].start()
#         # creare un macinatore e passargli minI e maxI
#         # foto 2

#     # facendo cosi do' all'ultimo thread più numeri da analizzare
#     minI = min+(threadReali - 1) * fettina
#     maxI = max
#     ciucci.append(Macinatore(minI, maxI))
#     ciucci[threadReali - 1].start()
#     # queste righe mi servono per dare da mangiare all'ultimo thread

#     # accumulo i risultati parziali di tutti i macinatori.
#     totale = 0
#     for i in range(threadReali):
#         totale += ciucci[i].getTotale()
#     return totale
# con il codice fino a riga 79 molto probabilmente i totale parziali non sono stati ancora calcolati.
# i 4 ciucci stanno ancora lavorando quando io gli invoco il getTotale sopra


# Come funziona una barriera? la si crea e la si passa a tutti i thread che vogliamo sincronizzare
# class Barrier:

#     def __init__(self, n):  # n è il tetto massimo di thread che va raggiunto
#         self.soglia = n
#         self.threadArrivati = 0
#         self.lock = Lock()
#         self.condition = Condition(self.lock)

#     def wait(self):
#         with self.lock:
#             self.threadArrivati += 1
#             if self.threadArrivati == self.soglia:  # se sei l'ultimo thread
#                 self.condition.notifyAll()
#             while self.threadArrivati < self.soglia:  # se non sei l'ultimo thread, ti metti in wait
#                 self.condition.wait()


# class Macinatore(Thread):
#     def __init__(self, min, max, b):
#         Thread().__init__(self)
#         self.min = min
#         self.max = max
#         self.totale = 0
#         self.barrier = b  # ogni thread vedrà la stessa barrier degli altri

#     def getTotale(self):
#         return self.totale

#     def run(self):
#         self.totale = contaPrimiSeq(self.min, self.max)
#         self.barrier.wait() # ciascun ciuccio invocherà la wait
#                             # --> prenderà il lock
#                             # --> incrementerà threadArrivati di 1 
#                             # --> se sei l'ultimo fai la notify a tutti gli altri, se non sei l'ultimo aspetti gli altri


# def contaPrimiMultiThread(min, max):

#     if max < min:
#         return 0

#     threadReali = 4  # vedere che scegliere
#     # fettina = (max - min) / tr --> foto 1

#     fettina = (max - min) // threadReali  # // è la divisione intera

#     ciucci = []
#     b = Barrier(threadReali+1) #Perché 5 e non 4? perché quando si usa una barriera bisogna individuare l'insieme dei thread che si devono sincronizzare tra loro
#                                 #qui non ho in gioco solo i 4 ciucci ma ho anche il main thread, il quale è fondamentale he aspetta tutti gli altri. minuto 43 parte2

#     for i in range(threadReali-1):  # l'ultimo thread lo vado ad inizializzare a riga 67
#         minI = min+i*fettina
#         # -1 perché non voglio sovrapporre il calcolo con il thread successivo
#         maxI = minI+fettina-1
#         ciucci.append(Macinatore(minI, maxI, b))
#         ciucci[i].start()

#         # creare un macinatore e passargli minI e maxI
#         # foto 2

#     # facendo cosi do' all'ultimo thread più numeri da analizzare
#     minI = min+(threadReali - 1) * fettina
#     maxI = max
#     ciucci.append(Macinatore(minI, maxI, b))
#     ciucci[threadReali - 1].start()
#     # queste righe mi servono per dare da mangiare all'ultimo thread
    
    
#     b.wait()


#     # aspetta i risultati definitivi

#     # accumulo i risultati parziali di tutti i macinatori.
#     totale = 0
#     for i in range(threadReali):
#         totale += ciucci[i].getTotale()
#     return totale

#######################
#       Miglioramo il codice
#anziché dire un numero fisso di cpu da utilizzare , possiamo
#usare un metodo che mi dice quante cpu ci sono a disposizione
import multiprocessing

# Come funziona una barriera? la si crea e la si passa a tutti i thread che vogliamo sincronizzare
class Barrier:

    def __init__(self, n):  # n è il tetto massimo di thread che va raggiunto
        self.soglia = n
        self.threadArrivati = 0
        self.lock = Lock()
        self.condition = Condition(self.lock)

    def wait(self):
        with self.lock:
            self.threadArrivati += 1
            if self.threadArrivati == self.soglia:  # se sei l'ultimo thread
                self.condition.notifyAll()
            while self.threadArrivati < self.soglia:  # se non sei l'ultimo thread, ti metti in wait
                self.condition.wait()


class Macinatore(Thread):
    def __init__(self, min, max, b):
        Thread().__init__(self)
        self.min = min
        self.max = max
        self.totale = 0
        self.barrier = b  # ogni thread vedrà la stessa barrier degli altri

    def getTotale(self):
        return self.totale

    def run(self):
        self.totale = contaPrimiSeq(self.min, self.max)
        self.barrier.wait() # ciascun ciuccio invocherà la wait
                            # --> prenderà il lock
                            # --> incrementerà threadArrivati di 1 
                            # --> se sei l'ultimo fai la notify a tutti gli altri, se non sei l'ultimo aspetti gli altri


def contaPrimiMultiThread(min, max):

    if max < min:
        return 0

    threadReali = cpu_count()
    # fettina = (max - min) / tr --> foto 1



    fettina = (max - min) // threadReali  # // è la divisione intera

    while fettina ==0:
        threadReali -= 1
        fettina =(max-min+1)//threadReali
        print("Usero' {} core" . format(threadReali))

    ciucci = []
    b = Barrier(threadReali+1) #Perché 5 e non 4? perché quando si usa una barriera bisogna individuare l'insieme dei thread che si devono sincronizzare tra loro
                                #qui non ho in gioco solo i 4 ciucci ma ho anche il main thread, il quale è fondamentale he aspetta tutti gli altri. minuto 43 parte2

    for i in range(threadReali-1):  # l'ultimo thread lo vado ad inizializzare a riga 67
        minI = min+i*fettina
        # -1 perché non voglio sovrapporre il calcolo con il thread successivo
        maxI = minI+fettina-1
        ciucci.append(Macinatore(minI, maxI, b))
        ciucci[i].start()

        # creare un macinatore e passargli minI e maxI
        # foto 2

    # facendo cosi do' all'ultimo thread più numeri da analizzare
    minI = min+(threadReali - 1) * fettina
    maxI = max
    ciucci.append(Macinatore(minI, maxI, b))
    ciucci[threadReali - 1].start()
    # queste righe mi servono per dare da mangiare all'ultimo thread
    
    
    b.wait()


    # aspetta i risultati definitivi

    # accumulo i risultati parziali di tutti i macinatori.
    totale = 0
    for i in range(threadReali):
        totale += ciucci[i].getTotale()
    return totale



start = time.time()
minimo = 100000
massimo = 1000000
print(f"Primi tra {minimo} e {massimo}: {contaPrimiSeq(minimo,massimo)}")
print(
    f"Primi tra {minimo} e {massimo}: {contaPrimiMultiThread(minimo,massimo)}")
elapsed = time.time()-start
print(f"tempo trascorso: {elapsed}")
