import time
start_time = time.perf_counter()
def solve_maze(maze, start, end):
    stack = [start]
    while stack:
        x, y = stack[-1]

        # If reached the end point
        if (x, y) == end:
            return True, stack

        # Mark as visited
        maze[x][y] = '2'

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':
                    stack.append((nx, ny))
                    break
        else:
            stack.pop()

    return False, []


if __name__ == "__main__":
    # 0 = open path, 1 = wall, S = start, E = end

    maze = [
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['S', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '0', '1', '1', '0', '1'],
        ['1', '0', '1', '0', '1', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '1', '0', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '1', '0', '0', '0', '0', '1'],
        ['1', '0', '0', '0', '1', '0', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '1', '0', '0', '1', '0', 'E'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    ]

    start = (1, 0)
    end = (8, 9)

    solved, path = solve_maze(maze, start, end)

    if solved:
        print("Maze Solved!")
        for x, y in path:
            if maze[x][y] != 'S' and maze[x][y] != 'E':
                maze[x][y] = '*'
        for row in maze:
            print("".join(row))
    else:
        print("No solution found.")

end_time = time.perf_counter()
execution_time = (end_time - start_time)*1000

print(f"El tiempo de ejecución fue: {execution_time} milisegundos")