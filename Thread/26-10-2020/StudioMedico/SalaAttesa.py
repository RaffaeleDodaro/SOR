from queue import Empty, Queue
from threading import RLock, Condition

class SalaAttesa:
    codaVisita=Queue()
    codaRicetta=Queue()
    codaRicettaPrioritaria=Queue()
    lockSegretaria=RLock()
    conditionNessunaRicetta = Condition(lockSegretaria)
    def putPazienteVisita(self,paziente):
        self.codaVisita.put(paziente)
        paziente.ricetta.attendiEsito()
        return paziente.ricetta

    def getPazienteVisita(self):
        return self.codaVisita.get()

    def putPazienteRicetta(self,paziente):
        self.codaRicetta.put(paziente)
        #abbiamo appena risvegliato  una possibile segretaria in pausa
        self.lockSegretaria.acquire()
        self.conditionNessunaRicetta.notifyAll()
        self.lockSegretaria.release()
        #########################################################
        paziente.ricetta.attendiEsito()
        return paziente.ricetta

    def putPazienteRicettaPrioritaria(self,paziente):
        self.codaRicettaPrioritaria.put(paziente)
        #abbiamo appena risvegliato  una possibile segretaria in pausa
        self.lockSegretaria.acquire()
        self.conditionNessunaRicetta.notifyAll()
        self.lockSegretaria.release()
        #########################################################
        paziente.ricetta.attendiEsito()
        return paziente.ricetta

    def getProssimoPaziente(self):
        #verifica se ci sono pazienti in coda prioritaria
        self.lockSegretaria.acquire()
        try:
            while(self.codaRicettaPrioritaria.empty() and self.codaRicetta.empty()):
                self.conditionNessunaRicetta.wait()

            if (not self.codaRicettaPrioritaria.empty()):
                return self.codaRicettaPrioritaria.get()
            
            return self.codaRicetta.get()
        finally:
            self.lockSegretaria.release()
                #entro in pausa
            # se non ce ne sono controllo la coda classica
            # altrimenti entra in pausa
