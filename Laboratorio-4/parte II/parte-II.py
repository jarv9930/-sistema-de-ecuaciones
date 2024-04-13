import numpy as np
import math
import matplotlib.pyplot as plt

def f1(x):
    return x**4 + (3*x)**3 + 2*x**2 - 1

def f2(x):
    return x**4 - (2*x)**3 - 8

def simulated_annealing(func, initial_temp, cooling_rate, stopping_temp, max_iterations):

    current_x = np.random.uniform(-10, 10)
    current_f = func(current_x)
    current_temp = initial_temp
    history = [(current_x, current_f)]
    
    for i in range(max_iterations):
        next_x = current_x + np.random.normal()
        next_f = func(next_x)

        energy_diff = next_f - current_f
        
        if energy_diff < 0 or np.random.uniform() < math.exp(-energy_diff / current_temp):
            current_x, current_f = next_x, next_f
            history.append((current_x, current_f))
        
        current_temp *= cooling_rate
        
        if current_temp < stopping_temp:
            break
            
    return current_x, current_f, history

initial_temp = 10000
cooling_rate = 0.99
stopping_temp = 1e-8
max_iterations = 1000

min_x1, min_f1, history1 = simulated_annealing(f1, initial_temp, cooling_rate, stopping_temp, max_iterations)

min_x2, min_f2, history2 = simulated_annealing(f2, initial_temp, cooling_rate, stopping_temp, max_iterations)

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


plot_function(f1, min_x1, min_f1, 'Gráfico de la Función f1(x)', 'f1(x)')

plot_function(f2, min_x2, min_f2, 'Gráfico de la Función f2(x)', 'f2(x)')