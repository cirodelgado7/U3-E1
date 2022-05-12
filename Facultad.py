from Carrera import Carrera


class Facultad:
    __idFacultad = ''
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __cantidadCarreras = ''
    __carreras = []

    def __init__(self, idFacultad='', nombre='', direccion='', localidad='', telefono='', cantidadCarrera=''):
        self.__idFacultad = idFacultad
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__cantidadCarreras = cantidadCarrera
        self.__carreras = []

    def __str__(self):
        cadena = '\n{} {} {} {} {}\n'.format(self.__idFacultad, self.__nombre, self.__direccion,
                                             self.__localidad, self.__telefono)
        for carrera in self.__carreras:
            cadena += str(carrera)

        return cadena

    def getIdFacultad(self):
        return self.__idFacultad

    def getNombre(self):
        return self.__nombre

    def getLocalidad(self):
        return self.__localidad

    def getCarreras(self):
        return self.__carreras

    def appendCarrera(self, idFacultad, codCarrera, nombre, titulo, duracion, tipo):
        unaCarrera = Carrera(idFacultad, codCarrera, nombre, titulo, duracion, tipo)
        self.__carreras.append(unaCarrera)
