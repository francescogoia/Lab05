class Corso:
    def __init__(self, codins, crediti, nome, pd):
        self.codins = codins
        self.crediti = crediti
        self.nome = nome
        self.pd = pd
        self._studenti_iscritti = None

    def __str__(self):
        return f"{self.nome} ({self.codins})"

    def _iscritti_corso(self, lista_studenti):
        self._studenti_iscritti = lista_studenti