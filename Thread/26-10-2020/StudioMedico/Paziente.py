from Ricetta import Ricetta
class Paziente:
    idPaziente=0
    def __init__(self,nome):
        self.nome = "Paziente_" + str(Paziente.idPaziente)
        self.ricetta = Ricetta()
        Paziente.idPaziente += 1