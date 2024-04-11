


class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self.codins = codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd
        self._studenti_iscritti = {}

    def __str__(self):
        return f"{self.nome} ({self.codins})"

    def add_studente(self, s):
        self._studenti_iscritti[s.matricola] = s

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)