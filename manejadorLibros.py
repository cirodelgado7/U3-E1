import csv
from ClaseLibro import Libro


class manejadorLibros:
    __listaLibros = []

    def __init__(self):
        self.__listaLibros = []

    def __str__(self):
        s = "\n"
        for lista in self.__listaLibros:
            s += str(lista) + '\n'
        return s

    def cargarDatos(self):
        archivo = open('Libros.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            idLibro = fila[0]
            titulo = fila[1]
            autor = fila[2]
            editorial = fila[3]
            isbn = fila[4]
            cantCapitulos = int(fila[5])
            unLibro = Libro(idLibro, titulo, autor, editorial, isbn, cantCapitulos)
            for fila1 in reader:
                unLibro.appendCapitulo(fila1[0], fila1[1])
                cantCapitulos -= 1
                if cantCapitulos == 0:
                    break
            self.agregarLibro(unLibro)
        archivo.close()

    def agregarLibro(self, unLibro):
        self.__listaLibros.append(unLibro)

    def buscarLibro(self, clave):
        for indice, Libro in enumerate(self.__listaLibros):
            if int(Libro.getId()) == clave:
                return self.__listaLibros[indice]

    def mostrarDatos(self, id):
        l = self.buscarLibro(id)
        print(l.getTitulo())
        c = l.getCapitulos()
        i = 0
        k = 0
        while i < l.getCantCapitulos():
            k += int(c[i].getCantPaginas())
            cap = c[i].getTitulo()
            print(cap)
            i += 1
        print('\n La cantidad total de paginas del libro es: {}'.format(k))

    def buscarPalabra(self, palabra):
        lista = []
        for libro in self.__listaLibros:
            if palabra in libro.getTitulo():
                lista.append(libro)
            else:
                for i in range(libro.getCantCapitulos()):
                    if palabra in libro.mostrarCapitulo(i).getTitulo():
                        lista.append(libro)
        return lista