from Paziente import Paziente
from Ricetta import Ricetta
from SalaAttesa import SalaAttesa
from Medico import Medico
from GeneraPazienti import GeneraPazienti
from Segretaria import Segretaria

def main():
    salaAttesa=SalaAttesa()
    medico=Medico(salaAttesa)
    segretaria1=Segretaria(salaAttesa)
    segretaria2=Segretaria(salaAttesa)
    generaPazienti= GeneraPazienti(salaAttesa)
    medico.start()
    segretaria1.start()
    segretaria2.start()
    generaPazienti.start()

if __name__=="__main__":
    main()