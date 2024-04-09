# Definamos límites para la variable x y ajustemos los parámetros del algoritmo
bounds = (-10, 10)  # Estableciendo un rango más razonable para x

# Redefinamos la función de templado simulado para incluir límites
def simulated_annealing_with_bounds(func, bounds, initial_temp, cooling_rate, stopping_temp, max_iterations):
    lower_bound, upper_bound = bounds
    current_x = np.random.uniform(lower_bound, upper_bound)
    current_f = func(current_x)
    current_temp = initial_temp
    history = [(current_x, current_f)]
    
    for i in range(max_iterations):
        # Asegurarse de que next_x está dentro de los límites
        next_x = np.clip(current_x + np.random.normal(), lower_bound, upper_bound)
        next_f = func(next_x)
        
        # Cálculo de la diferencia de energía
        energy_diff = next_f - current_f
        
        # Criterio de aceptación de Metropolis
        if energy_diff < 0 or np.random.uniform() < math.exp(-energy_diff / current_temp):
            current_x, current_f = next_x, next_f
            history.append((current_x, current_f))
        
        # Enfriamiento
        current_temp *= cooling_rate
        
        # Condición de parada
        if current_temp < stopping_temp:
            break
            
    return current_x, current_f, history

# Ejecutemos de nuevo el algoritmo con límites y parámetros ajustados
initial_temp = 1.0  # Iniciar con una temperatura más baja
cooling_rate = 0.95  # Tasa de enfriamiento más lenta
stopping_temp = 1e-8
max_iterations = 1000

# Ejecutar el algoritmo con límites
min_x1_bound, min_f1_bound, history1_bound = simulated_annealing_with_bounds(
    f1, bounds, initial_temp, cooling_rate, stopping_temp, max_iterations)

min_x1_bound, min_f1_bound
