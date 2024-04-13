import random
import math
import time

def f(x):
    return x**4 + (3*x)**3 + 2*x**2 - 1 #x**4 - (2*x)**3 - 8


def random_range(a, b):
    return a + (b - a) * random.random()

def simulated_annealing():
    T_inicial = 1000.0
    T_final = 0.1
    alfa = 0.95
    num_iteraciones = 10000
    
    x_actual = random_range(-10.0, 10.0)
    f_actual = f(x_actual)
    
    mejor_x = x_actual
    mejor_f = f_actual
    
    T = T_inicial
    
    while T > T_final:
        for i in range(num_iteraciones):
            x_vecino = x_actual + random_range(-0.1, 0.1)
            f_vecino = f(x_vecino)
            
            delta_E = f_vecino - f_actual
            
            if delta_E < 0 or random.random() < math.exp(-delta_E / T):
                x_actual = x_vecino
                f_actual = f_vecino
                
                if f_actual < mejor_f:
                    mejor_x = x_actual
                    mejor_f = f_actual
                    
        T *= alfa
    
    print(f"Minimo valor de f(x) encontrado: {mejor_f} en x = {mejor_x}")

# Inicializa el generador de números aleatorios
random.seed(time.time())

# Ejecuta el algoritmo
simulated_annealing()