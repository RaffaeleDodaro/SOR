from Pizzeria import Pizzeria
from Pizzaiolo import Pizzaiolo
from Cliente import Cliente
from Ordine import Ordine

def main():
    pizzaioli=[Pizzaiolo]*3
    clienti=[Cliente]*10
    pizzeria=Pizzeria()

    for i in range(0..3):
        pizzaioli[i]=Pizzaiolo("Claudio_" + str(i),pizzeria)
        pizzaioli[i].start()
    for i in range(0..10):
        clienti[i]=Clienti("Salvetore_" + str(i),pizzeria)
        clienti[i].start()

if __name__ == "__main__":
    main()
