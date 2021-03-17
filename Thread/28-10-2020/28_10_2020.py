# PROBLEMA DEI 5 FILOSOFI
# ogni filosofo ha una bacchetta alla sua sx e una alla sua dx.
# quando un filosofo vuole mangiare deve prendere entrambe le bacchette
# un filosofo solitamente pensa, fa uno spuntino prende le bacchette e mangia. quando
# Hegel mangia sta usando le bacchette di Schopenhauer e Marx. questo
# implica che finquando hegel mangia Schopenhauer e Marx digiunano. un filosofo
# puo' usare solo le bacchette che ha affianco. La bacchetta e' una risorsa condivisa mentre i 
# filosofi sono i thread.

from threading import Thread,Lock,Condition
from time import sleep
from random import randrange

# class Bacchetta:
#     def __init__(self):
#         self.lock=Lock()

#     def prendiBacchetta(self):
#         self.lock.acquire()

#     def lasciaBacchetta(self):
#         self.lock.release()

# class Tavolo:
#     def __init__(self):
#         self.bacchetta=[Bacchetta() for _ in range(5)] #sto attribuendo un numero ad ogni bacchetta 


# class Filosofo(Thread):
#     def __init__(self,tavolo,pos):
#         super().__init__()
#         self.posizione=pos
#         self.t=tavolo
#         self.name="Philip %s"%pos
    
#     def attesaCasuale(self,msec):
#         sleep(randrange(msec)/1000.0)
    
#     def pensa(self):
#         print(f"il filosofo {self.getName()} pensa")
#         self.attesaCasuale(1000)
#         print(f"il filosofo {self.getName()} smette di pensare")
    
#     def mangia(self):#per mangiare ho bisogno di prendere la bacchetta sx e dx
        
#         print f"il filosofo {self.getName()} vuole mangiare."
        
#         self.t.bacchetta[self.posizione].prendiBacchetta()
#         print f"il filosofo {self.getName()} ha preso prima bacchetta."
        
#         self.t.bacchetta[(self.posizione+1)%5].prendiBacchetta() # il modulo mi serve per capire la bacchetta successiva che posso prendere
#         print f"il filosofo {self.getName()} ha preso seconda bacchetta e mangia."
        
#         self.attesaCasuale(500)
        
        
#         self.t.bacchetta[self.posizione].lasciaBacchetta()
#         print f"il filosofo {self.getName()} ha lasciato prima bacchetta"
        
#         self.t.bacchetta[(self.posizione+1)%5].lasciaBacchetta() # il modulo mi serve per capire la bacchetta successiva che posso prendere
#         print f"il filosofo {self.getName()} ha lasciato seconda bacchetta"
    
#     def run(self):
#         while True:
#             self.pensa()
#             self.mangia()


# tavolo = Tavolo()

# filosofi =[Filosofo(tavolo,i) for i in range(5)] #creo un array di filosofi, i e' il numero che attribuiro' ad ogni filosofo
# for f in filosofi:
#     f.start() #faccio partire i 5 filosofi
# ho la situazione di foto1.jpg
    
    
#con il programma fino a riga 71 abbiamo una brutta cosa:
# di botto le stampe smetteranno di andare avanti. perche'? abbiamo un deadlock.
# deadlock --> attesa circolare
# ogni thread occupa un pezzetto di risorsa che gli serve e aspetta se stessa.
# si potrebbe risolvere solo se si liberasse la risorsa che ha davanti e cosi via. FOTO 2

# MINUTO 48 REGISTRAZIONE



# attualmente ho 5 lock e come detto la politica di acquisizione di questi lock e' tale per cui si puo' 
# formare un ciclo. perche' non cambiamo la disciplina di accesso a queste bacchette facendo
# in maniera che o prendo entrambe le bacchette insieme o aspetto a prescindere? qui dov'e' il problema?
# io prendo una risorsa che non mi serve a niente in questo momento e poi vado a mettermi in attesa dell'altro.
# la soluzione e': cambiero' la disciplina di accesso alle bacchette rimuovendo il problema alla radice. qui dov'e'
# il problema? ogni filosofo prende una risorsa che non gli serve ancora finquando non prende anche l'altra risorsa in mano
# e creando appunto il ciclo. cambieremo proprio la disciplina di acquisizione delle bacchette in maniera che posso prendere
# solamente entrambe le bacchette ma se una e' occupata metteremo il filosofo in attesa a prescindere

#voglio fare un sistema di prenotazione delle bacchette.

class Bacchetta:
    def __init__(self):
        self.lock=Lock()
        self.occupata=False

    def checkOccupata(self):
        return self.occupata

    def prendiBacchetta(self):
        self.occupata=True

    def lasciaBacchetta(self):
        self.occupata=False

class Tavolo:
    def __init__(self):
        self.bacchetta=[Bacchetta() for _ in range(5)] #sto attribuendo un numero ad ogni bacchetta 
        self.lock=Lock()
        self.condition=Condition(self.lock)
        
    def prendiLockSimultaneo(self,posizione):
        with self.lock:
            while(self.bacchetta[posizione].checkOccupata() or self.bacchetta[(posizione+1)%5].checkOccupata()):
                self.cond.wait()
            self.bacchetta[posizione].prendiBacchetta()
            self.bacchetta[(posizione+1)%5].prendiBacchetta()
    
    def mollaLockSimultaneo(self,posizione):#minu
        with self.lock:
            self.bacchetta[posizione].lasciaBacchetta()
            self.bacchetta[(posizione+1)%5].lasciaBacchetta()
            self.condition.notifyAll() #ho fatto notifyall perche voglio poter svegliare chiunque possa sfruttare le bacchette che sto lasciando

class Filosofo(Thread):
    def __init__(self,tavolo,pos):
        super().__init__()
        self.posizione=pos
        self.t=tavolo
        self.name="Philip %s"%pos
    
    def attesaCasuale(self,msec):
        sleep(randrange(msec)/1000.0)
    
    def pensa(self):
        print(f"il filosofo {self.getName()} pensa")
        self.attesaCasuale(1000)
        print(f"il filosofo {self.getName()} smette di pensare")
    
    def mangia(self):#per mangiare ho bisogno di prendere la bacchetta sx e dx
        
        print(f"il filosofo {self.getName()} vuole mangiare.")
        
        #acquire di entrambe le bacchette
        self.t.prendiLockSimultaneo(self.posizione)
        print(f"il filosofo {self.getName()} ha le sue bacchette e mangia")
        
        self.attesaCasuale(500)
        
        #release di entrambe le bacchette
        print(f"il filosofo {self.getName()} sta per lasciare le sue bacchette")
        self.t.mollaLockSimultaneo(self.posizione)
        
        print(f"il filosofo {self.getName()} termina di mangiare")
        
    def run(self):
        while True:
            self.pensa()
            self.mangia()


tavolo = Tavolo()

filosofi =[Filosofo(tavolo,i) for i in range(5)] #creo un array di filosofi, i e' il numero che attribuiro' ad ogni filosofo
for f in filosofi:
    f.start()