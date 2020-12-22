from threading import Thread
from random import randint,random,randrange
from time import sleep

class Medico(Thread):
    def __init__(self,salaAttesa):
        super().__init__()
        self.salaAttesa=salaAttesa

    def run(self):
        while(True):
            paziente = self.salaAttesa.getPazienteVisita()
            sleep(random())
            #genero un numero casuale tra 0 e 1 per decidere cosa fare del paziente
            prescrizione=random()

            if prescrizione>0.6666:
                paziente.ricetta.medicina="nulla da prescrivere"
                paziente.ricetta.ricettaPronta()
            elif (prescrizione>0.3333):
                paziente.ricetta.medicina="stai bene"
                paziente.ricetta.ricettaPronta()
            else: 
                self.salaAttesa.putPazienteRicettaPrioritaria(paziente)
                paziente.ricetta.attendiEsito()