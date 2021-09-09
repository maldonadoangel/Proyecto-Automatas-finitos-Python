import pandas as pd

class Tabla():
    def __init__(self, archivo = '', tabla = ''):
        self._archivo = archivo
        self._tabla = tabla
    
    @property
    def archivo(self):
        return self._archivo
    @archivo.setter
    def ruta(self, archivo):
        self._archivo = archivo
        
    @property
    def tabla(self):
        return self._tabla
    @tabla.setter
    def tabla(self, tabla):
        self._tabla = tabla
        
    #Abrimos la hoja de excel
    def cargarTabla(self):
        self._tabla = pd.read_excel(self._archivo, sheet_name= "Hoja1")
        print(self._tabla.head())
    




if __name__ == "__main__":
    excel = Tabla("Tabla-transiciones.xlsx")
    excel.cargarTabla()