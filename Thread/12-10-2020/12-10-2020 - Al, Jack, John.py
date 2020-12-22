# #Il mio primo thread
# from threading import Thread


# class Stampa:
#     def stampaStriscia(self,c,l):#self è l'oggetto stesso su cui si applica il metodo
#         for i in range(0,l+1):#stampa l copie del carattere c
#             print(c, end='',flush=True)#termina la stampa con la stringa vuota,flush dice a print di stampare subito
#         print('')


# #creo 2 thread che stampano uno asterisco e l'altro trattini
# #nel costruttore troviamo s. questa s è un'istanza della classe Stampa
# class StampaAsterischi(Thread):
#     def __init__(self,s:Stampa): #per verificare che s è veramente un oggetto di stampa possiamo fare def __inti__(self,s:Stampa)
#         super().__init__()
#         self.st=s

#     def run(self):
#         while True:
#             self.st.stampaStriscia("*")

# class StampaTrattini(Thread):
#     def __init__(self,s:Stampa):
#         super().__init__()
#         self.st=s

#     def run(self):
#         while True:
#             self.st.stampaStriscia("-")

# s=Stampa()

# john=StampaAsterischi(s)
# al=StampaTrattini(s)

# john.start()#start è ereditato da Thread ma io nella classe non lo richiamo mai
# al.start()

#quando prendo un thread(una sua istanza) e ci chiamo start di sopra,
#quel thread viene magicamente creato come thread di sistema operativo
#e viene schedulato. il thread esegue il run ma io lo chiamo attraverso
#start. MAI CHIAMARE DIRETTAMENTE RUN

#FINO A QUESTA RIGA C'è SOVRAPPOSIZIONE DI STAMPE
#a riga 39 abbiamo 2 musicisti che suonano due spartiti diversi:
#uno di asterischi e uno di trattini. come fanno a suonare? dipende
#dallo scheduler.ricorda che abbiamo una sola cpu. in questo momento john
#e al solo ready all'esecuzione, lo scheduler ne sceglie uno, ad 
#esempio john, allora a john viene dato il controllo e in questo momento
#viene eseguito il suo run. ad un certo punto il guanto di tempo dedicato a 
#john scade e quando finisce john viene congelato e sospeso.
#john cosa stava facendo quando è stato sospeso? e non lo sappiamo, dipende
#fino a che punto è arrivato in quel momento li. E' IMPREDICIBILE QUANDO
#LO SCHEDULER TI TOGLIE LA VITA. di conseguenza john si ferma.
#ad un certo punto lo scheduler sceglie al e succede la stessa cosa di john.
#la favola finisce con lo scheduler di sistema che alterna john e al in
#maniera del tutto randomatica. l'alternanza non è regolare perché:
#tra al e john vengono eseguiti anche processi di sistema che non c'entrano.
#il secondo motivo è che questi thread fanno anche I/O quando fa le print
#qui abbiamo una RACE CONDITION in quanto i thread concorrono per chi deve 
#accedere prima alla console


#RISOLVIAMO QUESTO BUG
#dobbiamo far sincronizzare i thread possiamo usare:
#SPINLOCK
#TEST & SET
#MONITO
#SEMAFORI

#Il mio primo thread
from threading import Lock, Thread


class Stampa:

    def __init__(self):
        self.lock=Lock()# il lock permette di creare un meccanismo simil semaforo
                        # il lock si può acquisire o rilasciare

    def stampaStriscia(self,c,l):#self è l'oggetto stesso su cui si applica il metodo
        self.lock.acquire()
        for i in range(0,l+1):#stampa l copie del carattere c
            print(c, end='',flush=True)#termina la stampa con la stringa vuota,flush dice a print di stampare subito
        print('')
        self.lock.release()

#creo 2 thread che stampano uno asterisco e l'altro trattini
#nel costruttore troviamo s. questa s è un'istanza della classe Stampa
class StampaAsterischi(Thread):
    def __init__(self,s:Stampa): #per verificare che s è veramente un oggetto di stampa possiamo fare def __inti__(self,s:Stampa)
        super().__init__()
        self.st=s

    def run(self):
        while True:
            self.st.stampaStriscia("*")

class StampaTrattini(Thread):
    def __init__(self,s:Stampa):
        super().__init__()
        self.st=s

    def run(self):
        while True:
            self.st.stampaStriscia("-")

s=Stampa()

john=StampaAsterischi(s)
al=StampaTrattini(s)

john.start()#start è ereditato da Thread ma io nella classe non lo richiamo mai
al.start()


#immagina il lock come un semaforino. il lock ha anche un insieme di thread
# che all'inizio è vuoto e all'inizio john trova il semaforino verde.
# una volta acquisito il blocco il semaforino diventa rosso. john
#fa il proprio lavoro. se a john arriva una richiesta di context switch
#john viene sospeso ed entra nello stato di ready