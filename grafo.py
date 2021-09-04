# paso1: crear una imagen vacía
import networkx as nx  
import matplotlib.pyplot as plt # Dibuje imágenes y fotos que muestren paquetes y oraciones
import matplotlib.pyplot as gr
class Grafo():
    def __init__(self, nodo, arista):
        self.nodo = nodo
        self.arista = arista

Grafo = nx.MultiGraph() #Creamos una imagen vacia con la libreria networkx, especificamos que es un grafo multidireccional 

Grafo.add_node(1)

nx.draw(Grafo)