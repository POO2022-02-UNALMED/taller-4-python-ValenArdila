class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon
    
    def setNombre(self,nombre):
        self._nombre=nombre
    def getNombre(self):
        return self._nombre
    def setSalon(self,salon):
        self._salon=salon
    def getSalon(self):
        return self._salon
    def __str__(self):
        cadena=self._nombre+" "+self._salon
        return cadena
