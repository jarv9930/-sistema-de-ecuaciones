# Puzle Lineal con busqueda en amplitud
import time

from collections import deque
from arbol import Nodo
from memory_profiler import memory_usage

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado=False
    nodos_visitados= deque()
    nodos_frontera= deque()
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0 :
        
        nodo=nodos_frontera.popleft()
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            # solucion encontrada
            solucionado=True
            return nodo
        else:
            # expandir nodos hijo
            dato_nodo = nodo.get_datos()
            
            # operador central
            hijo=[dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)
            # operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)
            
            # operador izquierdo
            hijo=[dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)
                
            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

if __name__ == "__main__":
    estado_inicial = [4,3,2,1]
    solucion = [1, 2, 3, 4]
    
    ##Comenzamos a contar el tiempo
    start = time.perf_counter()
    
    #Calculamos el uso de memoria, obteniendo el pico de uso de memoria al ejecutar el algoritmo BFS
    mem_usage, nodo_solucion = memory_usage((buscar_solucion_BFS, (estado_inicial, solucion)), retval=True)
    
    ##Terminamos de contar el tiempo
    end_time = time.perf_counter()
    tiempo = (end_time - start)
    print('Tiempo de ejecucion %f s' % tiempo)
    
    print('Uso maximo de memoria MiB: %s' % max(mem_usage))
    # mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        #print(resultado)
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)

##LOS RESULTADOS DE LA EJECUCION NOS MUESTRAN QUE EL ALGORITMO BFS TARDA MENOS TIEMPO EN EJECUTARSE QUE EL ALGORIZMO DFS,
##PERO EL USO DE MEMORIA ES MAYOR QUE EL DEL ALGORITMO DFS. SIN EMBARGO, EL ALGORITMO BFS ENCUENTRA LA SOLUCION MAS OPTIMA
##EN ESTE PROBLEMA, LAS DIFERENCIAS NO SON TAN GRANDES EN EL USO DE MEMORIA Y TIEMPO DE EJECUCION, 
# PERO EN PROBLEMAS MAS GRANDES, EL USO DE MEMORIA PODRIA SER UNA
##DE LAS PRINCIPALES DESVENTAJAS DE ESTE ALGORITMO.