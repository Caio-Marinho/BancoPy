import psycopg2
from Config import Config


class Connection(Config):
    def __init__(self):

        Config.__init__(self)

        try:
            self.conn = psycopg2.connect(**self.config['postgres'])
            self.cursor = self.conn.cursor()
        except Exception as erro:
            print("Erro na conexão: ", erro)
            exit(1)

    def connection(self):
        return self.conn()

    def cursor(self):
        return self.cursor

    def commit(self):
        return self.conn.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self):
        return self.cursor.execute()

    def close(self):
        pass


