# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection

# Add whatever it is needed to interface with the DB Table corso



class StudenteDao:
    def __init__(self):
        pass
    def get_methods(self):
        self.connessione = get_connection()
        self.cursore =self.connessione.cursor(dictionary = True)
        query = """select * 
                from studente s
                """
        self.cursore.execute(query)
        self.rows = self.cursore.fetchall()
        self._lista_studenti = list()
        for row in self.rows:
            self._lista_studenti.append(row)

        self.cursore.close()
        self.connessione.close()

if __name__ == "__main__":
    stDao = StudenteDao()
    stDao.get_methods()
    for i in stDao._lista_studenti:
        print(i)
