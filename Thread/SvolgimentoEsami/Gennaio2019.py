from threading import Condition,RLock,Thread

class Cittadino:
    def __init__(self):
        self.soldiPercepiti = 0
        self.offerteRicevute = list()
        self.disoccupato = True
        self.lock=RLock()
        self.conditionDisoccupato=Condition(self.lock)
        self.conditionAccetta=Condition(self.lock)
        self.conditionMinore3=Condition(self.lock)
    
    def offriLavoro(self, nomeLavoro : str):
        #
        # Offre un lavoro a Self. Registra l'offerta nomeLavoro 
        # in self.offerteRicevute, ma solo se disoccupato = True
        #
        with self.lock:
            # if self.disoccupato:
            #     self.offerteRicevute.append(nomeLavoro)
            while not self.disoccupato:
                self.conditionDisoccupato.wait()
            self.conditionAccetta.notify_all()
            self.offerteRicevute.append(nomeLavoro)
            if len(self.offerteRicevute)<4:
                self.conditionMinore3.notify_all()
        
    def accettaLavoro(self,nomeLavoro : str):
        #
        # se nomeLavoro appartiene a self.offerteRicevute, pone self.disoccupato = False
        #
        with self.lock:
            # if nomeLavoro in self.offerteRicevute:
            #     self.disoccupato=False
            while not nomeLavoro in self.offerteRicevute:
                self.conditionAccetta.wait()
            self.offerteRicevute.remove(nomeLavoro)
            self.conditionMinore3.notify_all()
            self.conditionDisoccupato.notify_all()
            self.disoccupato=False
        
    def paga(self):
        #
        # Eroga 780 EUR a self, ma solo 
        # se quest'ultimo è disoccupato e il numero di offerte ricevute non supera 3
        # incrementa soldiPercepiti in accordo
        #
        with self.lock:
            # if self.disoccupato and len(self.offerteRicevute)<4:
            #     self.soldiPercepiti+=780
            while not self.disoccupato or len(self.offerteRicevute)>3:
                self.conditionMinore3.wait()
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
        self.lock=RLock()
        
    def distribuisciReddito(self):
        #
        # Attribuisce a tutti i componenti di self.cittadini il reddito del mese corrente (780 EUR a testa), 
        # decrementando soldiDisponibili e incrementando soldiErogati. Genera una eccezione e interrompe 
        # l'operazione se durante l'operazione i soldiDisponibili dovessero finire
        #
        with self.lock:
            for i in range(0,len(self.cittadini)):
                if self.soldiDisponibili-780<0:
                    raise ValueError
                self.cittadini[i].paga()
                self.soldiDisponibili-=780
                self.soldiErogati+=780
                

    def aggiungiSoldi(self, valore : int):
        #
        # incrementa self.soldiDisponibili dell'ammontare di 'valore'
        #
        with self.lock:
            self.soldiDisponibili+=valore

    def iContiTornano(self):
        #
        # Verifica che la somma di quanto percepito dai singoli elementi di self.cittadini corrisponda a self.soldiErogati
        # restituisce un valore booleano in accordo
        #
        with self.lock:
            somma=0
            for i in range(0,len(self.cittadini)):
                somma+=780
            return somma==self.soldiErogati