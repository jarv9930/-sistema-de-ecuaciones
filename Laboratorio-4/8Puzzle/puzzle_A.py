from queue import PriorityQueue



# Funcion heuristica (distancia de Manhattan)
def heuristica(estado):
    distancia = 0
    for i in range(3):
        for j in range(3):
            if estado[i][j] != 0:
                fila_objetivo = (estado[i][j] - 1) // 3
                columna_objetivo = (estado[i][j] - 1) % 3
                distancia += abs(i - fila_objetivo) + abs(j - columna_objetivo)
    return distancia

# Algoritmo de busqueda A*
def resolver_puzzle(initial_state, goal_state):
    # Se define la cola de prioridad
    queue = PriorityQueue()
    queue.put((0, initial_state))

    
    # Se define la lista de visitados
    visited = set()
    
    # Se define la lista de padres
    parent = {}
    
    # Se define la lista de costos cada estado
    tupla = tuple(map(tuple, initial_state))
    cost = {}
    cost[tupla] = 0

    
    
    while not queue.empty():
        # Obtener el estado con el menor coste
        current_cost, nodo_actual = queue.get()
        tupla_current = tuple(map(tuple, nodo_actual))
        
        # Comprobar si el estado actual es el estado objetivo
        if nodo_actual == goal_state:
            break
        
        # Agregar el estado actual a la lista de visitados
        visited.add(tuple(map(tuple, nodo_actual)))
        
        # Generar los posibles movimientos
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_state = list(map(list, nodo_actual))
            zero_row, zero_col = 0, 0
            for i in range(3):
                for j in range(3):
                    if new_state[i][j] == 0:
                        zero_row, zero_col = i, j
                        break
            
            new_row = zero_row + move[0]
            new_col = zero_col + move[1]
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
                new_state_tuple = tuple(map(tuple, new_state))
                
                if new_state_tuple not in visited:
                    
                    cost[tupla_current] = current_cost + 1
                    priority = current_cost + 1 + heuristica(new_state)
                    queue.put((priority, new_state))
                    visited.add(new_state_tuple)
                    parent[new_state_tuple] = tupla_current
    
    # Reconstruir el camino
    path = []
    tupla_current = tuple(map(tuple, goal_state))
    #print(tupla_current)
    while tupla_current != tuple(map(tuple, initial_state)):
        #print(tupla_current)
        path.append(tupla_current)
        tupla_current = parent[tupla_current]
    path.append(tuple(map(tuple, initial_state)))
    path.reverse()
    
    return path

# Definimos el estado inicial y el estado objetivo
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
initial_state = [[1, 5, 3], [8, 2, 6], [0, 7, 4]]

path = resolver_puzzle(initial_state,goal_state)
for state in path:
    print("Paso", path.index(state))
    for row in state:
        print(row)
print()
