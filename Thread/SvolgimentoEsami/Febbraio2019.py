import random, time, os
from threading import Thread,Condition,RLock
from queue import Queue

class Ufficio:
    def __init__(self,l):
        Thread.__init__(self)
        self.lock = RLock()
        self.condition = Condition(self.lock)
        self.lettera = l
        self.ticketDaRilasciare = 0
        self.ticketDaServire = 0

    def formatTicket(self,lettera,numero):
        return "%s%03d" % (lettera, numero)
    
    def getTicketInAttesa(self):
        with self.lock:
            return self.ticketDaRilasciare - self.ticketDaServire

    def prendiProssimoTicket(self):
        with self.lock:
            #
            # self.ticketDaRilasciare e self.ticketDaServire stanno per diventare diversi
            #
            if (self.ticketDaRilasciare <= self.ticketDaServire):
                self.condition.notify_all()
            self.ticketDaRilasciare+=1
            
            return self.formatTicket(self.lettera, self.ticketDaRilasciare)

    def chiamaProssimoTicket(self):
        with self.lock:
            #
            # Non ci sono ticket in attesa da elaborare. Attendo
            #
            while(self.ticketDaRilasciare <= self.ticketDaServire):
                self.condition.wait()

            self.ticketDaServire+=1
            
            return self.formatTicket(self.lettera, self.ticketDaServire)
                
 
class Sede:

    def __init__(self,n):
        self.n = n
        self.uffici = {} 
        for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[0:n]:
            self.uffici[l] = Ufficio(l) 
        self.lock = RLock()
        self.condition = Condition(self.lock)
        self.ultimiTicket = []
        self.update = False
        self.setPrintAttese = False

    def prendiTicket(self,uff):
        return self.uffici[uff].prendiProssimoTicket()

    def chiamaTicket(self,uff):
        ticket = self.uffici[uff].chiamaProssimoTicket()
        with self.lock:
            self.condition.notifyAll()
            self.update = True
            if(len(self.ultimiTicket) >= 5):
                self.ultimiTicket.pop()
            self.ultimiTicket.insert(0,ticket)
            

    def waitForTicket(self,ticket):
        with self.lock:
            while(ticket not in self.ultimiTicket):
                self.condition.wait()

    def printAttese(self):
        with self.lock:
            self.setPrintAttese = True
        

    def printUltimi(self):
        with self.lock:
            while not self.update:
                self.condition.wait()
            self.update = False
            #os.system('clear')
            if (self.setPrintAttese):
                for u in self.uffici:
                    print("%s : %d" % (self.uffici[u].lettera, self.uffici[u].getTicketInAttesa()))
                self.setPrintAttese = False
            else:
                for t in self.ultimiTicket:
                    print(t)
            print ("="*10)
            



class Persona(Thread):
    def __init__(self, sede):
        Thread.__init__(self)
        self.sede = sede
        self.n = len(sede.uffici)

    def run(self):
        while True:
            ticket = self.sede.prendiTicket(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[0:self.n]))
            self.sede.waitForTicket(str(ticket))



class Impiegato(Thread):
    def __init__(self, sede, lettera):
        Thread.__init__(self)
        self.sede = sede
        self.ufficio = lettera
 
    def run(self):
        while True:
            self.sede.chiamaTicket(self.ufficio)
            time.sleep(random.randint(0,4))
            #
            # Notifica di voler stampare il riepilogo attese 
            #
            if random.randint(0,5) >= 4:
                self.sede.printAttese()





class Display(Thread):
    def __init__(self, sede):
        Thread.__init__(self)
        self.sede = sede
        

    def run(self):
        while True:
            self.sede.printUltimi()
            





sede = Sede(6)

display = Display(sede)
display.start()


persona = [Persona(sede) for p in range(10)]
impiegato = [Impiegato(sede, i) for i in "ABCDEF"]


for p in persona:
    p.start()

for i in impiegato:
    i.start()