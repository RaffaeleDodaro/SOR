from threading import Thread
from random import randint, random, randrange
from time import sleep


class Pizzaiolo(Thread):
    def __init__(self, name, pizzeria):
        super().__init__()
        super().setName(name)
        self.pizzeria = pizzeria

    def run(self):
        while True:
            # step 1 --> prende una comanda(ordine)
            ordine = self.pizzeria.getOrdine()
            print("il pizzaiolo %s ha prelevato l'ordine con id %d" %
                  (self.getName(), ordine.id))

            # step 2 --> inizia la preparazione(proporzionale al numero delle pizze)
            seconds = random()
            sleep(seconds*ordine.quantita)
            ordine.prepara()
            print("il pizzaiolo %s ha preparato l'ordine con id %d, %d pizze di tipo %d:%s" % (
                self.getName(), ordine.id, ordine.quantita, ordine.tipoPizza))

            # step 3 --> inserisco l'ordine pronto nel buffer delle pizze
            self.pizzeria.putPizze(ordine)

            # step 4 --> il pizzaiolo riposa
            sleep(randInt(1, 3))
