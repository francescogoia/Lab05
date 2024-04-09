
class Studente:

    def __init__(self, matricola, nome, cognome, cds):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.cds = cds

    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"