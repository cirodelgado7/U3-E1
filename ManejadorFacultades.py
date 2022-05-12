import csv
from Facultad import Facultad


class ManejaFacultades:
    __facultades = []

    def __init__(self):
        self.__facultades = []

    def __str__(self):
        s = "\n"
        for lista in self.__facultades:
            s += str(lista) + '\n'
        return s

    def cargarArchivo(self):
        archivo = open('Facultades.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        fila = next(reader)
        bandera = True
        while bandera:
            unaFacultad = Facultad(fila[0], fila[1], fila[2], fila[3], fila[4])
            self.__facultades.append(unaFacultad)
            filaCarrera = next(reader)
            while bandera and fila[0] == filaCarrera[0]:
                try:
                    unaFacultad.appendCarrera(filaCarrera[0], filaCarrera[1], filaCarrera[2], filaCarrera[3],
                                              filaCarrera[4], filaCarrera[5])
                    filaCarrera = next(reader)
                except StopIteration:
                    bandera = False
            fila = filaCarrera
        archivo.close()

    def mostrarNombre(self):
        c = int(input('Código de Facultad: '))
        if int(self.__facultades[c - 1].getIdFacultad()) == c:
            print('{}'.format(self.__facultades[c - 1].getNombre()))
            for carrera in self.__facultades[c - 1].getCarreras():
                print('{:50}{}'.format(carrera.getNombre(), carrera.getDuracion()))

    def mostrarCodigo (self):
        n = input('Nombre de la Carrera: ')
        i = 0
        bandera = True
        while bandera and i < len( self.__facultades ):
            for carrera in self.__facultades[i].getCarreras():
                if carrera.getNombre() == n:
                    bandera = False
                    print('Nombre de la Facultad: {} \nLocalidad: {}'.format(self.__facultades[i].getNombre(), self.__facultades[i].getLocalidad()))
                    print('Codigo de Facultad: {} \nCódigo de Carrera: {}'.format(self.__facultades[i].getIdFacultad(), carrera.getCodigoCarrera()))
            i += 1
