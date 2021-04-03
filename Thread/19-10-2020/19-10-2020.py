#blocking queue

#buffer circolare:
#usato all'interno dei sistemi op. ha 2 proprieta' fondamentali:
#1) dimensione del buffer fissata
#2) operazioni di put/get devono essere straveloci. complex O(1)

# implementazione:
# 1)si dichiara array B di dimensione fissata [0---N-1]
# come la facciamo la put? tieniamoci una variabile che si ricorda 
# la prima cella disponibile => B[i]=c; i+=1;

# come la facciamo la get? possiamo usare una variabile che si 
# ricorda da quale cella ho estratto l'ultima volta => 
# outV=out; out+=1; return B[outV];
# out ""segue"" in e gli sta leggermente indietro

# se sono arrivato al bordo destro con in? si riciclano le cellette 
# vuote che sono rimaste a sx usando il modulo. quando incremento
# in faccio in=(in+1)%N; 
# cosa succede se out arriva al bordo dx? quando incremento
# out faccio out=(out+1)%N

# se buffer pieno? ci teniamo un contatore che conta quante palluzze 
# ci sono dentro il buffer. cont = 0; se faccio put faccio cont += 1.
# se faccio get faccio cont -= 1;
# se cont==0 coda vuota
# se cont==N coda piena

# from threading import Thread
# from random import random
# from time import sleep

# class BlockingQueue2020:
#     def __init__(self, dim):
#         self.ins = 0
#         self.out = 0
#         self.slotPieni = 0
#         self.dim=dim #dimensione del buffer
#         self.thebuffer=[None]*dim

#     def put(self,c):
#         if self.slotPieni==len(self.thebuffer):
#             raise ValueError #da errore e blocca programma
#         self.thebuffer[self.ins] = c
#         self.ins=(self.ins+1)% len(self.thebuffer)
#         self.slotPieni += 1

#     def get(self):
#         if self.slotPieni==0:
#             raise ValueError

#         returnValue = self.thebuffer[self.out]
#         self.out = (self.out+1)% len(self.thebuffer)
#         self.slotPieni -=1
#         return returnValue

# class Consumer(Thread):
#     def __init(self,buffer):
#         self.queue = buffer
#         Thread.__init__(self)
    
#     def run(self):
#         while True:
#             sleep(random()*2)
#             self.palluzza = self.queue.get()
#             print("sono il thread %s e ho prelevato il valore %s" % (self.getName(),self.palluzza))

# class Producer(Thread):
#     def __init(self,buffer):
#         self.queue = buffer
#         Thread.__init__(self)

#     def run(self):
#         while True:
#             sleep(random()*2)
#             self.palluzza="PALLUZZA: "+self.getName()
#             self.queue.put(self.palluzza)
#             print("sono il thread %s e ho prelevato il valore %s" % (self.getName(),self.palluzza))

# buffer=BlockingQueue2020(10)
# producers=[Producer(buffer) for x in range(5)]
# consumers=[Consumer(buffer) for x in range(2)]

# for p in producers:
#     p.start()

# for c in consumers:
#     c.start()
# con il codice fino a riga 89:
#abbiamo problemi di thread safety pesantissimi perchè
#può benissimo succedere che mentre un produttore sta
#innocentemente inserendo un elemento arriva un altro produttore che ti
# va a modificare ins con il risultato che l'inserimento viene
#fatto nel punto sbagliato. PUò SUCCEDERE LO STESSO CON LE GET
# capiamo che c'è la race condition dal fatto che non è disciplinato l'accesso
#alle variabili condivise. per stoppare la race condition possiamo usare LOCK

# La differenza tra RLock e Lock è che con Rlock è rientrante, 
# cioé se io thread che già possiedo il lock lo riprendo un'altra volta non
# andrò in attesa circolare su me stesso ma il lock rimane nelle mie mani
# invece con Lock se io chiedo un'altra volta il lock rischio di andare in attesa 
# circolare su me stesso

# from threading import Thread, Lock
# from random import random
# from time import sleep

# class BlockingQueue2020:
#     def __init__(self, dim):
#         self.ins = 0
#         self.out = 0
#         self.slotPieni = 0
#         self.dim=dim #dimensione del buffer
#         self.thebuffer=[None]*dim
#         self.lock=Lock()

#     def put(self,c):
#         with self.lock:
#             if self.slotPieni==len(self.thebuffer):
#                 raise ValueError #da errore e blocca programma
#             self.thebuffer[self.ins] = c
#             self.ins=(self.ins+1)% len(self.thebuffer)
#             self.slotPieni += 1

#     def get(self):
#         with self.lock:
#             if self.slotPieni==0:
#                 raise ValueError
#             returnValue = self.thebuffer[self.out]
#             self.out = (self.out+1)% len(self.thebuffer)
#             self.slotPieni -=1
#             return returnValue

# non conviene mettere 2 lock distinti perché vuol dire che
# sto consentendo di prelevare mentre si inserisce mantenendo la race condition

# class Consumer(Thread):
#     def __init(self,buffer):
#         self.queue = buffer
#         Thread.__init__(self)
    
#     def run(self):
#         while True:
#             sleep(random()*2)
#             self.palluzza = self.queue.get()
#             print("sono il thread %s e ho prelevato il valore %s" % (self.getName(),self.palluzza))

# class Producer(Thread):
#     def __init(self,buffer):
#         self.queue = buffer
#         Thread.__init__(self)

#     def run(self):
#         while True:
#             sleep(random()*2)
#             self.palluzza="PALLUZZA: "+self.getName()
#             self.queue.put(self.palluzza)
#             print("sono il thread %s e ho prelevato il valore %s" % (self.getName(),self.palluzza))

# buffer=BlockingQueue2020(10)
# producers=[Producer(buffer) for x in range(5)]
# consumers=[Consumer(buffer) for x in range(2)]

# for p in producers:
#     p.start()

# for c in consumers:
#     c.start()

#la versione da 102 a 169 occupa cpu inutilmente



#per risolvere il problema possiamo usare una 
#condition che consente di metterti in attesa passiva
#senza occupare cpu e aspetti che un evento ti sveglia

#come funzionano le condition? vanno create e per ogni
#condition c'è un insieme di thread in attesa su questa
#condition. ogni condition ha un solo lock padre. per mettere
# in attesa usiamo il metodo wait e non è possibile chiamare 
# wait se non si possiede il lock corrispondente
#per svegliare un thread(non sappiamo quale thread si sveglia) usiamo 
# il metodo notify. notifyAll sveglia tutti i thread presenti in wait-c
# e li mette in wait-l

from threading import Condition, Thread, Lock
from random import random
from time import sleep




# se buffer pieno? ci teniamo un contatore che conta quante palluzze 
# ci sono dentro il buffer. se faccio put faccio slotPieni += 1.
# se faccio get faccio slotPieni -= 1;
# se slotPieni==0 coda vuota
# se slotPieni==N coda piena



class BlockingQueue2020:
    def __init__(self, dim):
        self.ins = 0
        self.out = 0
        self.slotPieni = 0 # contatore che conta quante palluzze ci sono
        self.dim=dim #dimensione del buffer
        self.thebuffer=[None]*dim #si dichiara array B di dimensione fissata [0---N-1]
        self.lock=Lock()
        self.full_condition=Condition(self.lock)
        self.empty_condition=Condition(self.lock)

    # come la facciamo la put? tieniamoci una variabile che si ricorda 
    # la prima cella disponibile => B[i]=c; i+=1;
    def put(self,c):
        with self.lock:
            while (self.slotPieni == len(self.thebuffer)):
                self.full_condition.wait()

            self.empty_condition.notifyAll()    # mi serve per dire che la queue non è più vuota
            self.thebuffer[self.ins] = c
            self.ins=(self.ins+1)% len(self.thebuffer)# se sono arrivato al bordo destro con in? si riciclano le cellette 
                                                        # vuote che sono rimaste a sx usando il modulo. quando incremento
                                                        # in faccio in=(in+1)%N; 
            self.slotPieni += 1

    # come la facciamo la get? possiamo usare una variabile che si 
    # ricorda da quale cella ho estratto l'ultima volta => 
    # outV=out; out+=1; return B[outV];
    # out ""segue"" in e gli sta leggermente indietro
    def get(self):
        with self.lock:
            while self.slotPieni==0:# le wait vanno sempre circondate da while perché
                                    # quando ti svegli devi sempre vedere se davvero la situazione
                                    # che ti aveva posto in attesa adesso non vale più
                self.empty_condition.wait()
            returnValue = self.thebuffer[self.out]
            self.out = (self.out+1)% len(self.thebuffer)    # cosa succede se out arriva al bordo dx? quando incremento
                                                            # out faccio out=(out+1)%N.
                                                            # mi serve solo quando ho un buffer circolare, altrimenti no
            self.slotPieni -=1
            self.full_condition.notifyAll() #mi serve per dire che la queue non è più piena
            return returnValue

        # RICORDA L'ordine delle operazioni all'interno di un lock non è importante 
        # perché posso fare tutto quello che voglio sula struttura dati senza farmi 
        # problemi tanto il lock ce l'ho io e quello che sto facendo non lo vedrà nessuno

    def show(self):
        self.lock.acquire()
        val = [None] * self.dim
        
        for i in range(0,self.slotPieni):
            val[(self.out + i) % len(self.thebuffer)] = '*'
        
        for i in range(0,len(self.thebuffer) - self.slotPieni):
            val[(self.ins + i) % len(self.thebuffer)] = '-'
        
        print("In: %d Out: %d C: %d" % (self.ins,self.out,self.slotPieni))
        print("".join(val))
        self.lock.release()

#non conviene mettere 2 lock distinti perché vuol dire che
# sto consentendo di prelevare mentre si inserisce mantenendo la race condition

class Consumer(Thread):
    def __init(self,buffer):
        self.queue = buffer
        Thread.__init__(self)
    
    def run(self):
        while True:
            sleep(random()*2)
            self.palluzza = self.queue.get()
            self.queue.show()

class Producer(Thread):
    def __init(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self):
        while True:
            sleep(random()*2)
            self.palluzza="PALLUZZA: "+self.getName()
            self.queue.put(self.palluzza)
            self.queue.show()



buffer=BlockingQueue2020(10)
producers=[Producer(buffer) for x in range(5)]
consumers=[Consumer(buffer) for x in range(2)]

for p in producers:
    p.start()

for c in consumers:
    c.start()
#come funziona il programma per com'è fatto adesso? registrazione4 min 19