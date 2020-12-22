from threading import Thread
from random import randint,random,randrange
from time import sleep

class Segretaria(Thread):
    def __init__(self,salaAttesa):
        super().__init__()
        self.salaAttesa=salaAttesa

    def run(self):
        while True:
            paziente=self.salaAttesa.getProssimoPaziente()

            sleep(random())
            medicina=random()
            if medicina>0.6666:
                paziente.ricetta.medicina="Aulin"
            elif medicina>0.3333:
                paziente.ricetta.medicina="oki"
            else:
                paziente.ricetta.medicina="maalox"
            paziente.ricetta.ricettaPronta()