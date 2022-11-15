class Caracteristica:
    def __init__(self, processador, ram, interna, expansivel, cod):
        self.__processador = processador
        self.__ram = ram
        self.__interna = interna
        self.__expansivel = expansivel
        self.__cod = cod

    def get_processador(self):
        return self.__processador

    def set_processador(self, processador):
        self.__processador = processador

    def get_ram(self):
        return self.__ram

    def set_ram(self, ram):
        self.__ram = ram

    def get_interna(self):
        return self.__interna

    def set_interna(self, interna):
        self.__interna = interna

    def get_expansivel(self):
        return self.__expansivel

    def set_expansivel(self, expansivel):
        self.__expansivel = expansivel

    def get_cod(self):
        return self.__cod

    def set_cod(self, cod):
        self.__cod = cod
