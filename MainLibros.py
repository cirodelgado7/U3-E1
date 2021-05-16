from manejadorLibros import manejadorLibros
from ClaseMenuLibros import Menu

if __name__ == '__main__':
    libros = manejadorLibros()
    libros.cargarDatos()
    print(libros)
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n"
              "1. Inciso 1"
              "\n2. Inciso 2"
              "\n3. Salir")
        op = input('Ingrese una opcion: ')
        if op in range(1, 4) and type(op) is not str:
            menu.opcion(op, libros)
            salir = op == 3
        else:
            print('La opción ingresada no es valida. Ingrese una opción válida')
