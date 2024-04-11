from database import corso_DAO, studente_DAO, iscrizione_DAO
from model import corso, studente
#import corso, studente

class Model:
    def __init__(self):
        self._corsi = {}
        self._studenti = {}
        self._iscrizioni = []
        self.initialize()

    def initialize(self):
        self.add_corsi()
        self.add_studenti()
        self.add_iscritti()


    def add_corsi(self):
        csDao = corso_DAO.CorsoDao()
        csDao.get_methods()
        for cDao in csDao._lista_corsi:
            c = corso.Corso(cDao['codins'], cDao['crediti'], cDao['nome'], cDao['pd'])
            self._corsi[cDao['codins']] = c

    def add_studenti(self):
        stDao = studente_DAO.StudenteDao()
        stDao.get_methods()
        for sDao in stDao._lista_studenti:
            s = studente.Studente(sDao['matricola'], sDao['cognome'], sDao['nome'], sDao['CDS'])
            self._studenti[sDao['matricola']] = s

    def add_iscritti(self):
        isDao = iscrizione_DAO.Iscrizione_DAO()
        isDao.get_methods()
        for i in isDao._lista_iscrizioni:
            for c in self._corsi.values():
                if i['codins'] == c.codins:
                    for s in self._studenti.values():
                        if i['matricola'] == s.matricola:
                            c.add_studente(s)
                            s.add_corso(c)


    def _cerca_iscritti(self, corso):
        for c in self._corsi.values():
            if c.codins == corso:
                return c._studenti_iscritti.values()

if __name__ == "__main__":
    m = Model()
    m.add_iscritti()

