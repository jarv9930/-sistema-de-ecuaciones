import numpy as np
import math
import matplotlib.pyplot as plt

def f1(x):
    return x**4 + (3*x)**3 + 2*x**2 - 1

def f2(x):
    return x**4 - (2*x)**3 - 8

def recocido_simulado(funcion, temperatura_inicial, tasa_enfriamiento, temperatura_final, iteraciones_maximas):
    x_actual = np.random.uniform(-10, 10)
    f_actual = funcion(x_actual)
    temperatura_actual = temperatura_inicial
    historial = [(x_actual, f_actual)]
    
    for i in range(iteraciones_maximas):
        x_siguiente = x_actual + np.random.normal()
        f_siguiente = funcion(x_siguiente)

        diferencia_energia = f_siguiente - f_actual
        
        if diferencia_energia < 0 or np.random.uniform() < math.exp(-diferencia_energia / temperatura_actual):
            x_actual, f_actual = x_siguiente, f_siguiente
            historial.append((x_actual, f_actual))
        
        temperatura_actual *= tasa_enfriamiento
        
        if temperatura_actual < temperatura_final:
            break
            
    return x_actual, f_actual, historial

# Parámetros de la simulación
temperatura_inicial = 10000
tasa_enfriamiento = 0.99
temperatura_final = 1e-8
iteraciones_maximas = 1000

min_x1, min_f1, historial1 = recocido_simulado(f1, temperatura_inicial, tasa_enfriamiento, temperatura_final, iteraciones_maximas)
min_x2, min_f2, historial2 = recocido_simulado(f2, temperatura_inicial, tasa_enfriamiento, temperatura_final, iteraciones_maximas)

def graficar_funcion(func, min_x, min_f, titulo, etiqueta):
    x = np.linspace(-10, 10, 400)
    y = func(x)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label=etiqueta)
    plt.scatter(min_x, min_f, color='red', zorder=5, label=f'Mínimo encontrado: x={min_x:.2f}, f(x)={min_f:.2f}')
    plt.title(titulo)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

graficar_funcion(f1, min_x1, min_f1, 'Gráfico de la Función f1(x)', 'f1(x)')
graficar_funcion(f2, min_x2, min_f2, 'Gráfico de la Función f2(x)', 'f2(x)')
