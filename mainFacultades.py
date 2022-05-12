from ManejadorFacultades import ManejaFacultades
from menuFacultades import Menu

if __name__ == '__main__':
    f = ManejaFacultades()
    f.cargarArchivo()
    menu = Menu()
    menu.opciones(f)
