


class Studente:

    def __init__(self, matricola, nome, cognome, cds):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.cds = cds
        self._corsi = {}

    def add_corso(self, c ):
        self._corsi[c.codins] = c


    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"


    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)