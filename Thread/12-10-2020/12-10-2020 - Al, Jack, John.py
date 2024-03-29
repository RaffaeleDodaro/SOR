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
#e al sono ready all'esecuzione, lo scheduler ne sceglie uno, ad 
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
#accedere prima alla console per stampare senza nessun tipo di coordinamento


#RISOLVIAMO QUESTO BUG chiamato race condition
#dobbiamo far sincronizzare i thread possiamo usare:
#SPINLOCK
#TEST & SET
#MONITOR
#SEMAFORI

#Il mio primo thread
from threading import Lock, Thread


class Stampa:

    def __init__(self):
        self.lock=Lock()    # il lock permette di creare un meccanismo simil semaforo
                            # il lock si può acquisire o rilasciare

    # la nostra console e' la risorsa condivisa che viene acceduta senza disciplina
    def stampaStriscia(self,c,l):   # self è l'oggetto stesso su cui si applica il metodo
        self.lock.acquire() # aggancio una sorta di semaforo alla console
                            # facendo in modo che chi vuole stampare prima occupa la console e pone 
                            # il semaforo a rosso, quando finisce di stampare la console il semaforo e' verde.
                            # se il semaforo e' rosso e arriva un secondo, terzo, quarto thread e 
                            # trova il semaforo rosso non puo' usare la risorsa e ti devi mettere in wait e
                            # non puoi prenotare la risorsa fino a che il semaforo non torna verde
        
                            # con il lock acquire prendo il lock.
                            # il thread che arriva e trova il semaforo rosso si blocca li.
                            # quando viene fatta la release il lock passa da rosso a verde,
                            # un thread che si era bloccato sull'acquire viene svegliato e
                            # puo' ripartire da li

        for i in range(0,l+1):#stampa l copie del carattere c
            print(c, end='',flush=True)#termina la stampa con la stringa vuota,flush dice a print di stampare subito
        print('')
        self.lock.release() # quando faccio la release il semaforino passa da rosso a verde,
                            # un eventuale thread che sta in attesa di acquisire il lock verra' sbloccato

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