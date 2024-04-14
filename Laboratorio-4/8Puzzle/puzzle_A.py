# 8 Puzzle
# Nava Izquierdo César
# Candia Navarro Iván
# Brandon Aldair Diaz Ortiz
# Flores Estopier Rodrigo
# Rodriguez Valle Josue Abraham
# 6CV2
from queue import PriorityQueue



# Funcion heuristica (distancia de Manhattan)
#Una heurística admisible y consistente ,
# que calcula la suma de las distancias que separa cada ficha de su posición objetivo.
def heuristica(estado):
    distancia = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] != 0:
                #Se calcula la posicion en la que deberia estar el numero    
                fila_objetivo = (estado[i][j] - 1) // 3
                columna_objetivo = (estado[i][j] - 1) % 3
                #Se calcula la diferencia entre la posicion actual y la posicion objetivo
                distancia += abs(i - fila_objetivo) + abs(j - columna_objetivo)
    print("distancia")
    print(distancia)
    return distancia

# Algoritmo de busqueda A*
def resolver_puzzle(estado_inicial, estado_objetivo):
    # Se define la cola de prioridad
    cola = PriorityQueue()
    cola.put((0, estado_inicial))

    
    # Se define la lista de visitados
    visitados = set()
    
    # Se define la lista de padres
    padres = {}
    
    # Se define la lista de costos cada estado
    tupla = tuple(map(tuple, estado_inicial))
    cost = {}
    cost[tupla] = 0

    
    
    while not cola.empty():
        # Obtener el estado con el menor coste
        costo_actual, nodo_actual = cola.get()
        tupla_actual = tuple(map(tuple, nodo_actual))
        print("nodo_actual")
        print(nodo_actual)
        print("costo_actual")
        print(costo_actual)
        
        # Comprobar si el estado actual es el estado objetivo
        if nodo_actual == estado_objetivo:
            break
        
        # Agregar el estado actual a la lista de visitados
        visitados.add(tuple(map(tuple, nodo_actual)))
        
        # Generar los posibles movimientos
        # Movimientos: izquierda, derecha, arriba, abajo
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for movimiento in movimientos:
            nuevo_estado = list(map(list, nodo_actual))
            fila_cero, columna_cero = 0, 0
            
            # Encontrar la posicion del cero del estado actual. fila y columna
            for i in range(3):
                for j in range(3):
                    if nuevo_estado[i][j] == 0:
                        fila_cero, columna_cero = i, j
                        break
                    
            
            # Definimos la posicion del cero en la nueva fila y columna
            nueva_fila = fila_cero + movimiento[0]
            nueva_columna = columna_cero + movimiento[1]
            
            # Comprobar si el movimiento es valido, es decir, si la nueva fila y columna estan dentro del rango de 0 a 2
            if 0 <= nueva_fila < 3 and 0 <= nueva_columna < 3:
                #Generar el nuevo estado con el movimiento
                nuevo_estado[fila_cero][columna_cero], nuevo_estado[nueva_fila][nueva_columna] = nuevo_estado[nueva_fila][nueva_columna], nuevo_estado[fila_cero][columna_cero]
                print("nuevo_estado")
                print(nuevo_estado)
                tupla_nuevo_estado = tuple(map(tuple, nuevo_estado))
                
                if tupla_nuevo_estado not in visitados:
                    
                    cost[tupla_actual] = costo_actual + 1
                    
                    #calcular la prioridad del nuevo estado
                    prioridad = costo_actual + 1 + heuristica(nuevo_estado)
                    cola.put((prioridad, nuevo_estado))
                    visitados.add(tupla_nuevo_estado)
                    padres[tupla_nuevo_estado] = tupla_actual
    
    # Reconstruir el camino
    movimientos_realizados = []
    tupla_actual = tuple(map(tuple, estado_objetivo))
    #print(tupla_actual)
    while tupla_actual != tuple(map(tuple, estado_inicial)):
        #print(tupla_actual)
        movimientos_realizados.append(tupla_actual)
        tupla_actual = padres[tupla_actual]
    movimientos_realizados.append(tuple(map(tuple, estado_inicial)))
    movimientos_realizados.reverse()
    
    return movimientos_realizados

# Definimos el estado inicial y el estado objetivo
estado_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
estado_inicial = [[1, 5, 3], [8, 2, 6], [0, 7, 4]]

#Resolvemos el puzzle e imprimimos los pasos realizados para encontrar la solucion
movimientos_realizados = resolver_puzzle(estado_inicial,estado_objetivo)
for estado in movimientos_realizados:
    print("Paso", movimientos_realizados.index(estado))
    for fila in estado:
        print(fila)
print()
