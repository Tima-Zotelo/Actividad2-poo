import os
import csv
from claseViajeroFrec import ViajeroFrec as vf

class Menu:
    def mostrarMenu(self, xLV=None):
        os.system('cls')
        op = int (input ('''
    -------->Menu<--------
    Seleccione una opcion:
    1. Item 1: Leer archivo y crear lista (inciso 1)
    2. Item 2: Ingresar numero de viajero (inciso 2)
    3. Item 3: 
    0. Salir
    Su opcion: '''))
        return op

    def ManejadorMenu (self, op, xLV):    ## xLV: lista viajeros
        if op == 1:
            self.opcion1(xLV)
        elif op == 2:
            self.opcion2(xLV)
        elif op == 3:
            self.opcion3()

    def opcion1 (self, xLV):
        total = 0
        bandera = True
        path = './Viajeros.csv'
        archivo = open(path, 'r')
        reader = csv.reader(archivo, delimiter =',')
        for fila in reader:
            if bandera:
                bandera = False
            else:
                xNum = fila[0]
                xDNI = fila[1]
                xNombre = fila[2]
                xApellido = fila[3]
                xMillas = fila[4]
                viajero = vf(xNum, xDNI, xNombre, xApellido, xMillas)
                xLV.append(viajero)
                total += 1
        if total > 0:
            print (f'Lista cargada correctamente, se cargaron {total} viajeros')
            os.system('pause')
        else:
            print ('Error en la carga')
            os.system('pause')


    def opcion2 (self, xLV):
        os.system('cls')
        i = 0
        xNum = int (input ('ingrese numero del viajero: '))
        xViajero = xLV[i].getNumero()
        print (f'Primer numero: {xViajero}')
        while (i <= len(xLV) -1) and (xNum != xViajero):
            print (f'i antes: {i}')
            i += 1
            print (f'i despues: {i}')
            if i < len(xLV):
                print ('si')
                xViajero = int (xLV[i].getNumero())
                print (f'iffffff numero: {xViajero}') 
        print (f'iiiiii: {i}')
        print (f'ultimo numero: {xLV[i].getNumero()}')
        if xNum != xViajero:
            print ('Error, numero de viajero invalido')
        else:
            print(f'Viajero encontrado con el numero {xNum} y {xViajero}, indice = {i}, numero de viajero: {xLV[i].getNumero()}')
        os.system('pause')

    def opcion3 (self):
        print ('opc 3')
        os.system('pause')