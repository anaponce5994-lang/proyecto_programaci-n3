import csv
from Dijkstra import dijkstra   # depende de cómo se llame la función en tu archivo

grafo = {}
with open('aristas.csv', encoding='utf-8') as archivo:
    for fila in csv.DictReader(archivo):
        origen, destino = fila['origen'], fila['destino']
        peso = float(fila['distancia'])
        grafo.setdefault(origen, {})[destino] = peso
        grafo.setdefault(destino, {})[origen] = peso   # si el camino va en ambos sentidos

origen = input("¿Desde qué nodo? ")
print(dijkstra(grafo, origen))