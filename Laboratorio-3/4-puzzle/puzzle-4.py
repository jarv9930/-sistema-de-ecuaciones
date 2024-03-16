# Puzle Lineal con búsqueda en profundidad
from collections import deque
import time
from arbol import Nodo
from memory_profiler import memory_usage


def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = deque()
    nodos_frontera = deque()
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0 :        
        nodo = nodos_frontera.pop()
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo
        else:
            
            
            # expandir nodos hijo
            dato_nodo = nodo.get_datos()
            
            #EL OPERADOR DERECHO SE MOVIO AQUI, PARA QUE SE EVALUE COMO ULTIMO CASO, SI ES QUE YA NO HAY HIJOS IZQUIERDOS NI CENTRALES
            # operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2],]
            hijo_derecho = Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados) \
                    and not hijo_derecho.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_derecho)      
            
                
            # operador central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) \
                    and not hijo_central.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_central)

            #SE MOVIO EL OPERADOR IZQUIERDO AQUI, PARA QUE SE EVALUE PRIMERO EN LA SIGUIENTE ITERACION, Y ASI FUNCIONE COMO EL ALGORITMO DFS, 
            # QUE EVALUA PRIMERO EL HIJO IZQUIERDO
            # operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) \
                    and not hijo_izquierdo.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_izquierdo)


            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho]) 



if __name__ == "__main__":
    estado_inicial=[4,3,2,1]  # Estado inicial
    solucion=[1,2,3,4]
    ##Comenzamos a contar el tiempo
    start = time.perf_counter()
    
    #Calculamos el uso de memoria, obteniendo el pico de uso de memoria al ejecutar el algoritmo BFS
    mem_usage, nodo_solucion = memory_usage((buscar_solucion_DFS, (estado_inicial, solucion)), retval=True)
     ##Terminamos de contar el tiempo
    end_time = time.perf_counter()
    tiempo = (end_time - start)
    print('Tiempo de ejecucion %f s' % tiempo)
    print('Uso maximo de memoria: %s MiB' % max(mem_usage))
    
    # mostrar resultado
    resultado=[]
    nodo=nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print("Estado Inicial: ",estado_inicial)
    print("Estado objetivo: ",solucion)
    print("Solucion: ",resultado)