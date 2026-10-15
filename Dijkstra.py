def dijkstra(self, inicio, destino):
    distancias = {}
    anteriores = {}
    visitados = set()

    for nombre in self.nodos:
            distancias[nombre] = float("inf")
            anteriores[nombre] = None

    distancias[inicio] = 0

    while len(visitados) < len(self.nodos):
        # Buscar el nodo más cercano
        nodo_actual = None
        menor_distancia = float("inf")

        for nombre in self.nodos:

            if nombre not in visitados:

                if distancias[nombre] < menor_distancia:
                    menor_distancia = distancias[nombre]
                    nodo_actual = nombre

        if nodo_actual is None:
            break

        # Si llegamos al destino, terminamos
        if nodo_actual == destino:
            break

        visitados.add(nodo_actual)

        # Revisar vecinos
        nodo = self.nodos[nodo_actual]

        for vecino, peso in nodo.vecinos.items():

            nueva_distancia = (
                distancias[nodo_actual] + peso
            )

            if nueva_distancia < distancias[vecino]:

                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo_actual

    # Construir el camino
    camino = []
    actual = destino
    
    while actual is not None:
        camino.append(actual)
        actual = anteriores[actual]

    camino.reverse()
    return distancias[destino], camino