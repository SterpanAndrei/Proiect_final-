class Carte:
    def __init__(self, titlu: str,autor: str, gen :str, status='Disponibil'):
        self.titlu = titlu
        self.autor = autor
        self.gen = gen
        self.status = status

class Cititor:
    def __init__(self, nume : str, telefon : str, varsta : int):
        self.nume = nume
        self.telefon = telefon
        self.vastra = varsta
