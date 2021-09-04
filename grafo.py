import networkx as nx  
import matplotlib.pyplot as plt # Dibuje imágenes y fotos que muestren paquetes y oraciones
import matplotlib.pyplot as gr
class Grafo():
    def __init__(self, *nodo, arista):
        self.nodo = nodo
        self.arista = arista
    
def rellenarNodos():
    lectura = ''
    opcion = ''
    nodo = []
    while opcion != 'y':
        lectura = input('Ingrese un valores para sus nodos: ')
        nodo.append(lectura)
        opcion = input('Desea salir Y/n: ')
    print(nodo)

def main():
    Grafo = nx.MultiGraph() #Creamos una imagen vacia con la libreria networkx, especificamos que es un grafo multidireccional
    while True:
        print('Bienvenido'.center(100, '*'))
        print('Menu'.center(100, '*'))
        print('Seleccione una de las siguientes opciones: ')
        print('1. Crear Nodos')
        print('7. salir.')

        opcion = int(input('Ingrese una opcion: '))
        
        if opcion == 1:
            rellenarNodos()
        elif opcion == 7:
            print('Saliendo del programa...')
            exit()

if __name__ == '__main__':
    main()



















def main():
    print("\n")
    print("Bienvenido".center(100, '*'))

        



