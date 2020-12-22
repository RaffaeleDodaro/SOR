class Ordine:
    nextId = 0  # variabile statiche

    def __init__(self, tipoPizza, quantita):
        self.tipoPizza = tipoPizza
        self.quantita = quantita
        self.id = Ordine.nextId
        self.nextId += 1
        self.pizze = ""  # mi serve per l'output

    def prepara(self):
        for i in range(0, self.quantita):
            if(self.tipoPizza == 1):
                tipo = "-"
            elif self.tipoPizza == 2:
                tipo = "+"
            elif self.tipoPizza == 3:
                tipo = "/"
            else:
                tipo = "*"
            self.pizze += "("+tipo+")"
        