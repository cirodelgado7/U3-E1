import sys


class Menu:
    __switcher = None

    def __init__(self):
        __switcher = None
        self.__switcher = {
            1: self.mostrarNombre,
            2: self.mostrarCodigo,
            3: self.salir
        }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, f):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(f)

    def opciones(self, f):
        salir = False
        while not salir:
            print("\n-----------------Menu--------------------")
            print(" 1 - Mostrar por Código")
            print(" 2 - Mostrar por Nombre")
            print(" 3 - Salir")
            op = int(input(' Ingrese una opcion: '))
            self.opcion(op, f)
            if op == 3:
                salir = True

    def mostrarNombre(self, f):
        f.mostrarNombre()

    def mostrarCodigo(self, f):
        f.mostrarCodigo()

    def salir(self, f):
        sys.exit(0)
