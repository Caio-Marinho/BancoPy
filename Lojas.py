class Lojas:
    def __init__(self, cod, preco, local, cnpj,nome):
        self.__cod = cod
        self.__nome = nome
        self.__preco = preco
        self.__local = local
        self.__cnpj = cnpj

    def get_cod(self):
        return self.__cod

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_local(self):
        return self.__local

    def get_cnpj(self):
        return self.__cnpj

    def set_cod(self, cod):
        self.__cod = cod

    def set_nome(self,nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco

    def set_local(self, local):
        self.__local = local

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj
