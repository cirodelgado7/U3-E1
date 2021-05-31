from ClaseCapitulo import Capitulo


class Libro:
    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = ''
    __cantCapitulos = 0
    __capitulos = []

    def __init__(self, idLibro=0, titulo='', autor='', editorial='', isnb='', cantCapitulos=0):
        self.__idLibro = idLibro
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__isnb = isnb
        self.__cantCapitulos = cantCapitulos
        self.__capitulos = []

    def __str__(self):
        cadena = '\n{} {} {} {} {} {}\n'.format(self.__idLibro, self.__titulo, self.__autor,
                                                self.__editorial, self.__isbn, self.__cantCapitulos)

        for capitulo in self.__capitulos:
            cadena += str(capitulo)

        return cadena

    def getId(self):
        return self.__idLibro

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getCantCapitulos(self):
        return self.__cantCapitulos

    def getCapitulos(self):
        return self.__capitulos

    def mostrarCapitulo(self, i):
        return self.__capitulos[i]

    def appendCapitulo(self, titulo, cantidadPaginas):
        unCapitulo = Capitulo(titulo, cantidadPaginas)
        self.__capitulos.append(unCapitulo)