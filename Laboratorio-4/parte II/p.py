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


"""import numpy as np
import math
from scipy.optimize import minimize_scalar

# Define la primera función dada
def f1(x):
    return x**4 + (3*x)**3 + 2*x**2 - 1



# Algoritmo de templado simulado (simulated annealing)
def simulated_annealing(func, initial_temp, cooling_rate, stopping_temp, max_iterations):
    # Generar un punto inicial aleatorio
    current_x = np.random.uniform(-10, 10)
    current_f = func(current_x)
    current_temp = initial_temp
    history = [(current_x, current_f)]
    
    for i in range(max_iterations):
        next_x = current_x + np.random.normal()
        next_f = func(next_x)
        
        # Diferencia de energía entre el estado actual y el nuevo
        energy_diff = next_f - current_f
        
        # Si el nuevo estado tiene una energía menor, o si la probabilidad
        # es favorable, aceptar el nuevo estado
        if energy_diff < 0 or np.random.uniform() < math.exp(-energy_diff / current_temp):
            current_x, current_f = next_x, next_f
            history.append((current_x, current_f))
        
        # Disminuir la temperatura
        current_temp *= cooling_rate
        
        # Parar si la temperatura ha alcanzado el límite
        if current_temp < stopping_temp:
            break
            
    return current_x, current_f, history

# Parámetros del algoritmo de templado simulado
initial_temp = 10000
cooling_rate = 0.99
stopping_temp = 1e-8
max_iterations = 1000

# Ejecución del algoritmo para la primera función
min_x1, min_f1, history1 = simulated_annealing(f1, initial_temp, cooling_rate, stopping_temp, max_iterations)

min_x1, min_f1
# Vamos a imprimir los resultados de una manera más legible.
print(f"El valor mínimo de x encontrado es: {min_x1}")
print(f"El valor mínimo de la función f1(x) es: {min_f1}")

import numpy as np
import math
import matplotlib.pyplot as plt

# Definición de las funciones
def f1(x):
    return x**4 + (3*x)**3 + 2*x**2 - 1

def f2(x):
    return x**4 - (2*x)**3 - 8

# Algoritmo de templado simulado (simulated annealing)
def simulated_annealing(func, initial_temp, cooling_rate, stopping_temp, max_iterations):
    # Generar un punto inicial aleatorio
    current_x = np.random.uniform(-10, 10)
    current_f = func(current_x)
    current_temp = initial_temp
    history = [(current_x, current_f)]
    
    for i in range(max_iterations):
        next_x = current_x + np.random.normal()
        next_f = func(next_x)
        
        # Diferencia de energía entre el estado actual y el nuevo
        energy_diff = next_f - current_f
        
        # Si el nuevo estado tiene una energía menor, o si la probabilidad
        # es favorable, aceptar el nuevo estado
        if energy_diff < 0 or np.random.uniform() < math.exp(-energy_diff / current_temp):
            current_x, current_f = next_x, next_f
            history.append((current_x, current_f))
        
        # Disminuir la temperatura
        current_temp *= cooling_rate
        
        # Parar si la temperatura ha alcanzado el límite
        if current_temp < stopping_temp:
            break
            
    return current_x, current_f, history

# Parámetros del algoritmo de templado simulado
initial_temp = 10000
cooling_rate = 0.99
stopping_temp = 1e-8
max_iterations = 1000

# Ejecución del algoritmo para la primera función
min_x1, min_f1, history1 = simulated_annealing(f1, initial_temp, cooling_rate, stopping_temp, max_iterations)

# Ejecución del algoritmo para la segunda función
min_x2, min_f2, history2 = simulated_annealing(f2, initial_temp, cooling_rate, stopping_temp, max_iterations)

# Función para graficar y visualizar los resultados
def plot_function(f, min_x, min_f, title, label):
    x = np.linspace(-10, 10, 400)
    y = f(x)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=label)
    plt.scatter(min_x, min_f, color='red', zorder=5, label=f'Mínimo encontrado: x={min_x:.2f}, f(x)={min_f:.2f}')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Visualización para la primera función
plot_function(f1, min_x1, min_f1, 'Gráfico de la Función f1(x)', 'f1(x)')

# Visualización para la segunda función
plot_function(f2, min_x2, min_f2, 'Gráfico de la Función f2(x)', 'f2(x)')"""