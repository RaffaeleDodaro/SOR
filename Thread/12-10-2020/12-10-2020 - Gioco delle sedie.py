# ogni partecipante e' un thread
# Regola n1: capire qual e' la struttura dati condivisa
# in questo caso si tratta di un array

# from threading import Thread


# class Posto:
#     def __init__(self):
#         self.occupato = False

#     def libero(self):
#         return not self.occupato

#     def set(self, v):
#         self.occupato = v


# class Partecipante(Thread):
#     def __init__(self, posti):
#         # per i thread e' fondamentale chiamare il costruttore della classe madre
#         super().__init__()
#         # perche' il thread padre nel suo costruttore ha tutto cio' che serve
#         # per far diventare quest'oggetto un thread di sistema
#         self.posti = posti

#     def run(self):
#         for i in range(0, len(self.posti)):
#             if self.posti[i].libero():
#                 print("sono il thread %s. occupo il posto %d" % (self.getName(), i))  # getName appartiene ai Thread
#                 self.posti[i].set(True)
#                 return
#         print("sono il thread %s. ho perso" % (self.getName()))


# NSEDIE = 10
# posti = [Posto() for i in range(0, NSEDIE)]

# lg = Display(posti)
# lg.start()

# for t in range(0, NSEDIE+1):
#     t=Partecipante(posti)
#     t.start()

# FINO A RIGA 42 => strategia di gioco scema. tutti i thread provano ad occupare il posto 0
# ci sono problemi di race condition

# from threading import Thread


# class Display(Thread):
#     def __init__(self, posti):
#         super().__init__()
#         self.posti = posti

#     def run(self):
#         sleep(1)
#         while(True):
#             for i in range(0, len(self.posti)):
#                 if self.posti[i].libero():
#                     print("-", end='', flush=True)
#                 else:
#                     print("o", end='', flush=True)
#         print('')


# class Posto:
#     def __init__(self):
#         self.occupato = False

#     def libero(self):
#         return not self.occupato

#     def set(self, v):
#         self.occupato = v

# from time import sleep
# from random import random,randrange

# class Partecipante(Thread):
#     def __init__(self, posti):
#         # per i thread e' fondamentale chiamare il costruttore della classe madre
#         super().__init__()
#         # perche' il thread padre nel suo costruttore ha tutto cio' che serve
#         # per far diventare quest'oggetto un thread di sistema
#         self.posti = posti

#     def run(self):
#         sleep(random.randrange(5))#ogni thread si addormenta
#         for i in range(0, len(self.posti)):
#             if self.posti[i].libero():
#                 print("sono il thread %s. occupo il posto %d" %
#                       (self.getName(), i))  # getName appartiene ai Thread
#                 self.posti[i].set(True)
#                 return
#         print("sono il thread %s. ho perso" % (self.getName()))


# NSEDIE = 10
# posti = [Posto() for i in range(0, NSEDIE)]

# lg = Display(posti)
# lg.start()

# for t in range(0, NSEDIE+1):
#     t = Partecipante(posti)
#     t.start()

# ancora soffre di race condition


from threading import Thread, Lock
from time import sleep
from random import random, randrange


class Display(Thread):

    def __init__(self,posti):
        super().__init__()
        self.posti = posti

    def run(self):
        while(True):
            sleep(1)
            for i in range(0,len(self.posti)):
                if self.posti[i].libero():
                    print("-", end='', flush=True)
                else:
                    print("o", end='', flush=True)
            print('')


class Posto:
    def __init__(self):
        self.lock = Lock()
        self.occupato = False

    def libero(self):  # se non metto il semaforo qui potrebbe succedere che io vado a testare libero
                        # mentre qualcun altro fa la set e ottengo lo stesso una race condition

        # self.lock.acquire()
        # return not self.occupato
        # self.lock.release()# se lo metto qui, non viene mai eseguito per via del return +> thread mai rilasciato
        # risolvo questo problema con
        with self.lock:
            # con il with dopo la return e' come se ci fosse la release ma stavolta viene eseguita
            return not self.occupato

    def set(self, v):
        self.lock.acquire()
        self.occupato = v
        self.lock.release()
    
    #per risolvere il problema di riga 174
    def testaEOccupa(self):
        with self.lock():
            if self.occupato:
                return False
            else:
                self.occupato=True
                return True


class Partecipante(Thread):
    def __init__(self, posti):
        # per i thread e' fondamentale chiamare il costruttore della classe madre
        super().__init__()
        # perche' il thread padre nel suo costruttore ha tutto cio' che serve
        # per far diventare quest'oggetto un thread di sistema
        self.posti = posti

    def run(self):
        for i in range(0, len(self.posti)):
            # PROBLEMA: con if self.posti[i].libero(): POSSIBILE RACE CONDITION per il momento tra il release di libero e l'acquire di set potrebbe esserci un context switch
            if self.posti[i].testaEOccupa:#risolto problema 174
                print("sono il thread %s. occupo il posto %d" % (self.getName(), i))  # getName appartiene ai Thread
                return
        print("sono il thread %s. ho perso" % (self.getName()))


NSEDIE = 10
posti = [Posto() for i in range(0, NSEDIE)]

lg = Display(posti)
lg.start()

for t in range(0, NSEDIE+1):
    t = Partecipante(posti)
    t.start()
