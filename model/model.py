from database import corso_DAO, studente_DAO, iscrizione_DAO
from model import corso, studente
#import corso, studente

class Model:
    def __init__(self):
        self._corsi = list()
        self._studenti = list()
        self._iscrizioni = list()
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
            self._corsi.append(c)

    def add_studenti(self):
        stDao = studente_DAO.StudenteDao()
        stDao.get_methods()
        for sDao in stDao._lista_studenti:
            s = studente.Studente(sDao['matricola'], sDao['cognome'], sDao['nome'], sDao['CDS'])
            self._studenti.append(s)

    def add_iscritti(self):
        isDao = iscrizione_DAO.Iscrizione_DAO()
        isDao.get_methods()
        for corso in self._corsi:
            iscritti_corso = dict()
            studenti_corso = list()
            for iDao in isDao._lista_iscrizioni:
                if iDao['codins'] == corso.codins:
                    for stu in self._studenti:
                        if stu.matricola == iDao['matricola']:
                            studenti_corso.append(stu)
            corso._iscritti_corso(studenti_corso)
            iscritti_corso[corso.codins] = studenti_corso
            self._iscrizioni.append(iscritti_corso)


    def _cerca_iscritti(self, corso):
        for c in self._corsi:
            if c.codins == corso:
                return c._studenti_iscritti

if __name__ == "__main__":
    m = Model()
    for i in m._iscrizioni:
        print(i)