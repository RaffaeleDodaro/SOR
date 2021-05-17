from threading import Thread, RLock, Condition


class Candidato:
    def __init__(self,nome):
        self.nome = nome
        self.voti = 0


class Elezione:
    def __init__(self, candidati: list, elettori: int):
        self.candidati = candidati
        self.elettori = elettori
        self.statoElezioni = False
        self.lock = RLock()
        self.conditionStatoAperto = Condition(self.lock)
        self.statoAperto = False
        self.conditionStatoChiuso = Condition(self.lock)
        self.statoChiudi = False
        self.votanti=1000
        self.votantiAttuali=0

    def apriElezione(self):
        with self.lock:
            if not self.statoAperto:
                self.statoElezioni = True
                self.statoAperto = True
                self.conditionStatoAperto.notify_all()

    def chiudiElezione(self):
        with self.lock:
            while not self.statoAperto and not self.statoChiudi:  # da verificare
                self.conditionStatoAperto.wait()
            self.statoChiudi = True
            self.statoElezioni = False
            self.conditionStatoChiuso.notify_all()

    def vota(self, c: Candidato):
        with self.lock:
            while self.statoChiudi:
                self.conditionStatoAperto.wait()
            if c.voti+1<=self.votanti:
                c.voti+=1
                self.votantiAttuali+=1
            else:
                self.statoChiudi = True
                self.statoElezioni = False


    def getVoti(self):
        with self.lock:
            return self.votantiAttuali

    def waitForRisultati(self):
        with self.lock:
            while not self.statoElezioni:
                self.conditionStatoChiuso.wait()
            if self.votantiAttuali>self.votanti:
                return []
            
            for i in range(0,len(self.candidati)):
                if self.candidati[i].voti>self.candidati[i+1].voti:
                    appoggio=self.candidati[i]
                    self.candidati[i]=self.candidati[i+1]
                    self.candidati[i+1]=appoggio
            return self.candidati
