from menu import Menu
import os

if __name__ == '__main__':
    listaViaj = []
    xMenu = Menu()
    op = xMenu.mostrarMenu()
    while op != 0 & op <=3:
        xMenu.ManejadorMenu (op, listaViaj)
        op = xMenu.mostrarMenu(listaViaj)
    print ('saliendo...')
    os.system('pause')
    os.system('exit')


