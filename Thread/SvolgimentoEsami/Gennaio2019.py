from threading import Thread,Lock,Condition
from random import randrange
from time import sleep
from typing import List

class Cittadino:
    def __init__(self):
        self.soldiPercepiti = 0
        self.offerteRicevute = list()
        self.disoccupato = True
        self.lock=Lock()
        self.condition=Condition(self.lock)
    
    def offriLavoro(self, nomeLavoro : str):
        #
        # Offre un lavoro a Self. Registra l'offerta nomeLavoro 
        # in self.offerteRicevute, ma solo se disoccupato = True
        # 
        with self.lock:
            if self.disoccupato:
                self.offerteRicevute.append(nomeLavoro)
        
    def accettaLavoro(self,nomeLavoro : str):
        #
        # se nomeLavoro appartiene a self.offerteRicevute, pone self.disoccupato = False
        #
        with self.lock:
            if nomeLavoro in self.offerteRicevute:
                self.disoccupato=False
        
    def paga(self):
        #
        # Eroga 780 EUR a self, ma solo 
        # se quest'ultimo è disoccupato e il numero di offerte ricevute non supera 3
        # incrementa soldiPercepiti in accordo
        #
        with self.lock:
            if self.disoccupato and len(self.offerteRicevute)<4:
                self.soldiPercepiti+=780

    def getPercepito(self):
        #
        # Restituisce quanto percepito finora
        #
        with self.lock:
            return self.soldiPercepiti
        
class Popolo:        
    
    def __init__ (self):
        self.soldiErogati = 0
        self.soldiDisponibili = 1000000000
        self.cittadini = list()
        self.lock=Lock()
        self.condition=Condition(self.lock)

    def put(self,c):
        with self.lock:
            self.cittadini.append(c)

    def distribuisciReddito(self):
        #
        # Attribuisce a tutti i componenti di self.cittadini il
        # reddito del mese corrente (780 EUR a testa), 
        # decrementando soldiDisponibili e incrementando
        # soldiErogati. Genera una eccezione e interrompe
        # l'operazione se durante l'operazione i soldiDisponibili
        # dovessero finire
        with self.lock:
            for i in range(0,len(self.cittadini)):
                self.cittadini[i].paga()
                self.soldiDisponibili-=780
                self.soldiErogati+=780
                if self.soldiDisponibili<=0:
                    raise ValueError

    def aggiungiSoldi(self, valore : int):
        #
        # incrementa self.soldiDisponibili dell'ammontare di 'valore'
        #
        with self.lock:
            self.soldiDisponibili+=valore

    def iContiTornano(self):
        #
        # Verifica che la somma di quanto percepito dai singoli elementi
        # di self.cittadini corrisponda a self.soldiErogati
        # restituisce un valore booleano in accordo
        #
        with self.lock:
            somma=0
            for i in range(0,len(self.cittadini)):
                somma+=self.cittadini[i]
            return somma==self.soldiErogati

p=Popolo()

for i in range (0,10):
    c=Cittadino()
    p.put(c)

p.distribuisciReddito()

for i in range (0,10):
    print(p.cittadini[i].getPercepito())

print ("soldi disponibili: ", p.soldiDisponibili)
print ("soldi erogati: ", p.soldiErogati)