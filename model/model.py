from database import corso_DAO, studente_DAO
from model import corso, studente


class Model:
    def __init__(self):
        self._corsi = list()
        self._studenti = list()
        self.initialize()

    def initialize(self):
        self.add_corsi()
        self.add_studenti()


    def add_corsi(self):
        csDao = corso_DAO.CorsoDao()
        csDao.get_methods()
        for cDao in csDao._lista_corsi:
            c = corso.Corso(cDao['codins'], cDao['crediti'], cDao['nome'], cDao['pd'])
            self._corsi.append(c)

    def add_studenti(self):
        stDao = studente_DAO.StudenteDao()
        stDao.get_methods()
        for sDao in stDao._lista_studenti:
            s = studente.Studente(sDao['matricola'], sDao['cognome'], sDao['nome'], sDao['CDS'])
            self._studenti.append(s)

if __name__ == "__main__":
    m = Model()
    for i in m._studenti:
        print(i)