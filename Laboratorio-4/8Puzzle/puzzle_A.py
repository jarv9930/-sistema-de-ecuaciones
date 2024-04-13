from queue import PriorityQueue



# Define the heuristic function (Manhattan distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row = (state[i][j] - 1) // 3
                goal_col = (state[i][j] - 1) % 3
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

# Define the A* algorithm
def solve_puzzle(initial_state, goal_state):
    # Define the priority queue
    queue = PriorityQueue()
    queue.put((0, initial_state))
    
    # Define the visited set
    visited = set()
    
    # Define the parent dictionary
    parent = {}
    
    # Define the cost dictionary
    tupla = tuple(map(tuple, initial_state))

    cost = {}
    cost[tupla] = 0

    
    
    while not queue.empty():
        # Get the state with the lowest cost
        current_cost, current_state = queue.get()
        tupla_current = tuple(map(tuple, current_state))
        
        # Check if the current state is the goal state
        if current_state == goal_state:
            break
        
        # Add the current state to the visited set
        visited.add(tuple(map(tuple, current_state)))
        
        # Generate the next possible states
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_state = list(map(list, current_state))
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
                    priority = current_cost + 1 + heuristic(new_state)
                    queue.put((priority, new_state))
                    visited.add(new_state_tuple)
                    parent[new_state_tuple] = tupla_current
    
    # Reconstruct the path
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

# Test the algorithm
# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
initial_state = [[1, 5, 3], [8, 2, 6], [0, 7, 4]]

path = solve_puzzle(initial_state,goal_state)
for state in path:
    print("Step", path.index(state))
    for row in state:
        print(row)
print()
