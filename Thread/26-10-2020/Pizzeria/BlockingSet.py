from threading import RLock,Condition


class BlockingSet(set): # set viene ereditata da python. Sets are used to store multiple items 
                        # in a single variable.

    lock = RLock()
    condition= Condition(lock)

    def __init__(self,maxSize):
        super().__init__()
        self.maxSize=maxSize

    def add(self,element):
        self.lock.acquire()

        try:
            while len(self)>=self.maxSize:
                self.condition.wait()
            
            super().add(element)
            self.condition.notifyAll()
        finally:
            self.lock.release()

    def remove(self,element):
        self.lock.acquire()
        try:

            #fintantoche non c'e' l'elemento da rimuovere vado in wait
            returnValue=element in self
            
            while not returnValue:
                self.condition.wait()
                returnValue=element in self
            super.remove(element)
            self.condition.notifyAll()
            return returnValue
        finally:
            self.lock.release()