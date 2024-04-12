from database.DB_connect import get_connection

class Iscrizione_DAO:
    def __init__(self):
        pass

    def get_methods(self):
        self.connessione = get_connection()
        self.cursore =self.connessione.cursor(dictionary = True)
        query = """select *
                from iscrizione i 
                """
        self.cursore.execute(query)
        self.rows = self.cursore.fetchall()
        self._lista_iscrizioni = list()
        for row in self.rows:
            self._lista_iscrizioni.append(row)

        self.cursore.close()
        self.connessione.close()

    def add_row(self, matricola, codins):
        self.connessione = get_connection()
        self.cursore = self.connessione.cursor(dictionary=True)

        query = """insert into iscrizione
                            (matricola, codins)
                            values (%s, %s)"""
        self.cursore.execute(query, (matricola, codins))

        self.connessione.commit()
        self.cursore.close()
        self.connessione.close()

if __name__ == "__main__":
    isDao = Iscrizione_DAO()
    isDao.get_methods()
    for i in isDao._lista_iscrizioni:
        print(i)
    print(len(isDao._lista_iscrizioni))