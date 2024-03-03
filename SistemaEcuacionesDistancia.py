# Sistema de ecuaciones
# Nava Izquierdo César
# Candia Navarro Iván
# Brandon Aldair Diaz Ortiz
# Flores Estopier Rodrigo
# Rodriguez Valle Josue Abraham
# 6CV2
import numpy as np
from random import randint

valoresCercanos = [0, 0, 0, 0]
solucionesCercanas = [0, 0, 0, 0]
distanciaCercana = 0.0

# Función para comprobar si la combinación de valores satisface el sistema de ecuaciones
def es_solucion(B, D, E, F):
    return (16 * B - 6 * D + 4 * E + F == -36 and
            B - 8 * D + E + F == -64 and
            16 * B + 2 * D - 4 * E + F == -4 and
            9 * B + 8 * D - 3 * E + F == -64)
    
def calcularDistancia(B, D, E, F ,tipo):
    global valoresCercanos, solucionesCercanas, distanciaCercana
    #Calculamos los resultados que se obtienen con los valores actuales
    x1 = 16 * B - 6 * D + 4 * E + F
    x2 = B - 8 * D + E + F
    x3 = 16 * B + 2 * D - 4 * E + F
    x4 = 9 * B + 8 * D - 3 * E + F
    #Calculamos la distancia entre los resultados y los valores esperados
    dist1 = np.linalg.norm(x1 - (-36))
    dist2 = np.linalg.norm(x2 - (-64))
    dist3 = np.linalg.norm(x3 - (-4))
    dist4 = np.linalg.norm(x4 - (-64))
    
    #Calculamos la distancia total
    distTotal = dist1 + dist2 + dist3 + dist4
    
    if tipo == 1:
        valoresCercanos = [B, D, E, F]
        solucionesCercanas = [x1, x2, x3, x4]
        distanciaCercana = distTotal
    else:
        #Si la distancia total es menor a la distancia mas cercana encontrada hasta el momento se actualiza la solucion mas cercana
        if distTotal < distanciaCercana:
            valoresCercanos = [B, D, E, F]
            solucionesCercanas = [x1, x2, x3, x4]
            distanciaCercana = distTotal
            print(f"Se econtró una solucion mas cercana con los valores B = {B}, D = {D}, E = {E}, F = {F} con una distancia de {distanciaCercana}")
    
    #print(f"Distancia 1: {dist1} Distancia 2: {dist2} Distancia 3: {dist3} Distancia 4: {dist4}")
    

# Contador de intentos
numero_de_pruebas = 0
maximo_pruebas = 100000 # Número máximo de pruebas

# Proceso de búsqueda de solución
encontrado = False
while numero_de_pruebas < maximo_pruebas and not encontrado:
    # Incrementar el contador de intentos
    numero_de_pruebas += 1

    # Generar valores aleatorios
    valores = [randint(-100, 100) for _ in range(4)]

    # Asignamos los valores aleatorios a las variables
    B, D, E, F = valores
    
    # Imprimir el progreso cada intento
    print(f"Progreso: {numero_de_pruebas} intentos realizados.")
    print(f"B = {B}, D = {D}, E = {E}, F = {F}")
    
    # Verificar si los valores actuales son solución
    if es_solucion(B, D, E, F):
        encontrado = True
        print("Solución encontrada:")
        print(f"B = {B}, D = {D}, E = {E}, F = {F}")
        print(f"Número de intentos: {numero_de_pruebas}")
        break
    else:
        #Si no es solucion, calculamos que tan cerca estamos de una solucion
        if numero_de_pruebas == 1:
            calcularDistancia(B, D, E, F, 1)
        else:
            calcularDistancia(B, D, E, F, 0)
            
#En caso de no encontrar una solucion se imprime la solucion mas cercana
if not encontrado:
    print("---------------------------------------------")
    print(f"No se encontró una solución después de {maximo_pruebas} iteraciones.")
    print(f"La solucion mas cercana se encontro con los valores B = {valoresCercanos[0]}, D = {valoresCercanos[1]}, E = {valoresCercanos[2]}, F = {valoresCercanos[3]}")
    print(f"Con las soluciones cercanas de: EQ1={solucionesCercanas[0]}, EQ2={solucionesCercanas[1]}, EQ3={solucionesCercanas[2]}, EQ4={solucionesCercanas[3]} para cada ecuacion")
    print(f"Se intento buscar una solucion para los siguientes resultados E1=-36, E2=-64, E3={-4}, E4={-64}")