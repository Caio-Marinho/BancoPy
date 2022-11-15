import mysql.connector
from Code_Support.Config import Config


class Connection(Config):
    """

    """
    def __init__(self):

        Config.__init__(self)

        try:
            self.con = mysql.connector.connect(**self.config["mysql"])
            self.cursor = self.con.cursor()
        except Exception as erro:
            print("Erro na conexão: ", erro)
            exit(1)

    def connection(self):
        return self.con()

    def cursor(self):
        return self.cursor()

    def commit(self):
        return self.con.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self):
        return self.cursor.execute()

    def close(self):
        pass
