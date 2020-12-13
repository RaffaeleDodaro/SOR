from threading import Thread
from random import randint, random, randrange
from time import sleep

class Cliente(Thread):
    def __init__(self, name, pizzeria):
        super().__init__()
        super().setName(name)
        self.pizzeria = pizzeria

    def run(self):
        while True:
            # step 1 --> il cliente genera un ordine  
            tipoPizza=randint(1,4)
            quantita=randint(1,4)

            # step 2 --> L'ordine viene inserito nel buffer ordini
            ordine = self.pizzeria.putOrdine(tipoPizza, quantita)
            print ("il cliente %s ha inserito l'ordine con id %d" % (self.getName(),ordine.id))

            # step 3 --> il cliente entra in un'attesa NON bloccante
            sleep(randint(1,4)*quantita)

            # step 4 --> il cliente controlla se l'ordine e' pronto; se non lo e' entra in un'attesa bloccante(c'e' una wait sul thread)
            self.pizzeria.getPizze(ordine)
            print ("il cliente %s ha prelevato l'ordine con id %d" % (self.getName(),ordine.id))

            # step 5 --> il cliente mangia la pizza e poi va via
            sleep(randint(1,5))