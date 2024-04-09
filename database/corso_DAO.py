# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection

class CorsoDao:
    def __init__(self):
        pass
    def get_methods(self):
        self.connessione = get_connection()
        self.cursore =self.connessione.cursor(dictionary = True)
        query = """select * 
                from corso c 
                """
        self.cursore.execute(query)
        self.rows = self.cursore.fetchall()
        self._lista_corsi = list()
        for row in self.rows:
            self._lista_corsi.append(row)

        self.cursore.close()
        self.connessione.close()

if __name__ == "__main__":
    csDao = CorsoDao()
    csDao.get_methods()
    for i in csDao._lista_corsi:
        print(i)
