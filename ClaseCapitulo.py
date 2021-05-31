class Capitulo:

    __titulo = ''
    __cantPaginas = 0

    def __init__(self, titulo, cantPaginas):
        self.__titulo = titulo
        self.__cantPaginas = cantPaginas

    def __str__(self):
        cadena = "\n{0}\t {1}".format(self.__titulo, self.__cantPaginas)
        return cadena

    def getTitulo(self):
        return self.__titulo

    def getCantPaginas(self):
        return self.__cantPaginas

    def motrarDatos(self,capitulos):
        print(capitulos)

