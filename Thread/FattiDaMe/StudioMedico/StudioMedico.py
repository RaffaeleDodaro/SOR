#  lo studio medico è fornito di una Sala  di  Attesa  presso la quale devono attendere
#  il proprio turno i pazienti in cura dal medico. Ciascun Paziente, al suo arrivo, occupa
#  un posto nella sala di attesa ed attende il proprio turno. In particolare, i pazienti 
#  saranno “serviti” nell'ordine di arrivo, secondo una politica di gestione FIFO. 
#  Inoltre,  un  paziente  può  recarsi  presso  lo  studio  medico  o  per  effettuare  
#  una  visita  medica o, in alternativa, per richiedere il rilascio di una ricetta medica.



#  1.SalaDiAttesa:  gestisce  l'arrivo  dei  pazienti  che  lì  aspetteranno  per  effettuare  una  visita  medica
#  oppure per avere una ricetta medica;
#  2.Medico: richiama i pazienti in attesa di una visita medica, visita il paziente e al termine si prepara per la 
#  successiva visita (chiama il successivo paziente);
#  3.Segretaria: richiama i pazienti in attesa di una ricetta medica, fornisce la ricetta al paziente e al termine 
#  si prepara per servire la richiesta successiva (chiama il successivo paziente);
#  4.Paziente: entra  nella  sala  di  attesa  e  attende  il  proprio  turno,  ovvero,  attende  di  essere  
#  chiamato  dal  Medico o  dalla  Segretaria. Un  paziente  in  attesa  di  una  ricetta  medica,  una  volta  
#  ottenuta  quest’ultima,  lascia  la  sala.  Un  paziente  in  attesa  di  una  visita  medica,  una  volta  
#  terminata  quest’ultima,  lascia  la  sala  se  il  medico  non  gli  ha  prescritto  alcuna  ricetta  medica,  
#  oppure  torna  in  attesa  in  sala  e  verrà  richiamato  dalla  segretaria  non  appena  possibile. 
#  Al termine il paziente lascia la sala. 

from threading import Thread,Lock,Condition,
from queue import Queue
from time import sleep
from random import random

class StudioMedico:
    def __init__(self):
        pass

class SalaDiAttesa:
# 1.SalaDiAttesa:  gestisce  l'arrivo  dei  pazienti  che  lì  aspetteranno  per  effettuare  una  visita  medica
# oppure per avere una ricetta medica;
    def __init__(self):
        self.codaVisitaMedica=Queue()
        self.codaRicetta=Queue()
    
    def putPaziente(self, p:Paziente):
        pass

class Paziente:
    def __init__(self):
        pass

class Segretaria:
    def __init__(self):
        pass


# Tra  i  pazienti  in  attesa  nella  sala,  il  Medico  ne  chiamerà  uno  per  volta  per
# la  visita  medica  (rispettando  rigorosamente  l'ordine  di  arrivo).  Inoltre,  dei  pazienti
# in  attesa  visiterà  solo quelli  che  aspettano  di  essere  visitati  (mentre  tralascerà  i  
# pazienti  che  attendono  per  una  ricetta  medica).  Infatti,  il  medico  non  si  occupa  
# direttamente  di  rilasciare  ricette,  ma  si  avvale  del  lavoro  di  una  Segretaria  il  cui  
# compito  è  quello  di  smaltire  velocemente  le  richieste  di  pazienti  che  necessitano  solo 
# di  avere  una  ricetta  medica.  Tra  i  pazienti  in  attesa  nella  sala,  la  Segretaria  ne  
# chiamerà  uno  per  volta  tra  quelli  che  attendono  per  una  ricetta  medica  (rispettando  
# rigorosamente  l'ordine  di  arrivo). 

# Un paziente che era in attesa di una ricetta, una volta ottenuta, lascerà lo studio medico. Un paziente 
# che era in attesa di essere visitato, una volta terminata la visita si metterà nuovamente in attesa per 
# avere la ricetta medica, qualora a seguito della visita si fosse reso necessario.  In tal caso, però, il 
# paziente acquisisce una priorità rispetto agli altri in attesa di avere una ricetta. Infatti, sarà il primo 
# ad essere servito dalla segretaria non appena si libera (Bonus).

