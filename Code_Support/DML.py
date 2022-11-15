class DML:
    def __init__(self,coluna,dado):
        self.__coluna = coluna
        self.__dado = dado
        self.__coluna_u = coluna
        self.__dado_u = dado

    def get_coluna_U(self):
        return self.__coluna_u

    def set_coluna_U(self,coluna):
        self.__coluna_u = coluna

    def get_dado_U(self):
        return self.__dado_u

    def set_dado_U(self,dado):
        self.__dado_u = dado

    def get_coluna(self):
        return self.__coluna

    def set_coluna(self,coluna):
        self.__coluna = coluna

    def get_dado(self):
        return self.__dado

    def set_dado(self,dado):
        self.__dado = dado
