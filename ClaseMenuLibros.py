class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, libros):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(libros)

    def opcion1(self, libros):
        id = int(input('Ingrese el id del libro: '))
        if id in range(10001, 10002):
            libros.mostrarDatos(id)
        else:
            print('Identificador de libro no encontrado')

    def opcion2(self, libros):
        palabra = input("Ingrese palabra a Buscar: ")
        for libros in libros.buscarPalabra(palabra):
            print("\nTitulo: {} \nAutor: {}".format(libros.getTitulo(), libros.getAutor()))

    def salir(self, libros):
        print('Salir')
