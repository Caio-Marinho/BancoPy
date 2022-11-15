class login:
    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha

    def get_login(self):
        return self.__login

    def set_login(self,login):
        self.__login = login

    def get_senha(self):
       return self.__senha

    def set_senha(self,senha):
        self.__senha = senha