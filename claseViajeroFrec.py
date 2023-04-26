class ViajeroFrec:
    __numViajero = int
    __dni = str
    __nom = str
    __apellido = str
    __millasAcum = int

    def __init__ (self, numViajero=None, dni=None, nombre=None, apellido=None, millasAcum=None):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nom = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum

    def cantidadTotalDeMillas (self):
        return self.__millasAcum
    
    def acumularMillas (self, xMillas):
        self.__millasAcum += xMillas
        return self.__millasAcum

    def canjearMillas (self, xMillas):
        if xMillas <= self.__millasAcum:
            self.__millasAcum -= xMillas
        else:
            print('Error, cantidad de millas insuficiente')
        return self.__millasAcum
    
    def getNumero(self):
        return self.__numViajero