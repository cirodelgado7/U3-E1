class Carrera:
    __codigoFacultad = ''
    __codigoCarrera = ''
    __nombre = ''
    __titulo = ''
    __duracion = ''
    __tipo = ''

    def __init__(self, codigoFacultad='', codigoCarrera='', nombre='', titulo='', duracion='', tipo=''):
        self.__codigoFacultad = codigoFacultad
        self.__codigoCarrera = codigoCarrera
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__tipo = tipo

    def __str__(self):
        cadena = "\n{:3}{:10}{:50}{:40}{:20}{:20}\n".format(self.__codigoFacultad, self.__codigoCarrera,
                                                            self.__nombre, self.__titulo, self.__duracion,
                                                            self.__tipo)
        return cadena

    def getCodigoCarrera(self):
        return self.__codigoCarrera

    def getNombre(self):
        return self.__nombre

    def getDuracion(self):
        return self.__duracion
