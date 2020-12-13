from threading import Thread
from random import randint,random,randrange
from time import sleep
from Paziente import Paziente

class PazienteRun(Thread):
    def __init__(self,salaAttesa):
        super().__init__()
        self.salaAttesa=salaAttesa
    
    def run(self):
        paziente = Paziente("Paziente_"+ str(randint(1,10000)))

        if(random()>0.5):
            self.salaAttesa.putPazienteVisita(paziente)
        else:
            self.salaAttesa.putPazienteRicetta(paziente)
        
        print("paziente %s e' uscito con la prescrizione %s"%(paziente.nome,paziente.ricetta.medicina))


class GeneraPazienti(Thread):

    def __init__(self,salaAttesa):
        super().__init__()
        self.salaAttesa=salaAttesa
    
    def run(self):
        while True:
            pazienteRun=PazienteRun(self.salaAttesa)
            pazienteRun.start()

            sleep(randrange(0,2))