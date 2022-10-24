class Config:

    def __init__(self):
        self.config = {
            'postgres': {
                'user': 'postgres',
                'password': 'postgres',
                'host': 'localhost',
                'port': '5432',
                'dbname': 'projeto',
                'sslmode': "prefer"

            },
            'mysql': {
                'user': 'root',
                'password': 'teste',
                'host': 'localhost',
                'port': '3306',
            }
        }
