import random

def generate_maze(rows=25, cols=25):
    maze = [['X'] * cols for _ in range(rows)]
    visited = set()
    step = 3

    def open_cell(r, c):
        maze[r][c] = ' '
        maze[r][c + 1] = ' '
        maze[r + 1][c] = ' '
        maze[r + 1][c + 1] = ' '

    start = (1, 1)
    open_cell(1, 1)
    visited.add(start)
    stack = [start]

    while stack:
        r, c = stack[-1]
        neighbours = []
        for dr, dc in [(0, step), (0, -step), (step, 0), (-step, 0)]:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= rows - 3 and 1 <= nc <= cols - 3 and (nr, nc) not in visited:
                neighbours.append((nr, nc, dr, dc))

        if neighbours:
            nr, nc, dr, dc = random.choice(neighbours)
            if dr == 0: # horizontal : buka 2 sel dinding secara vertikal
                wall_c = c + (2 if dc > 0 else -1)
                maze[r][wall_c] = ' '
                maze[r + 1][wall_c] = ' '
            else: # vertikal : buka 2 sel dinding secara horizontal
                wall_r = r + (2 if dr > 0 else -1)
                maze[wall_r][c] = ' '
                maze[wall_r][c + 1] = ' '
            open_cell(nr, nc)
            visited.add((nr, nc))
            stack.append((nr, nc))
        else:
            stack.pop()

    return maze


def build_level(rows=25, cols=25, num_treasures=5):
    maze = generate_maze(rows, cols)

    # Player : pojok kiri atas
    maze[1][1] = 'P'

    # Enemy : pojok kanan bawah
    maze[rows - 3][cols - 3] = 'E'

    # Treasure : random di sel yang terbuka
    open_cells = [
        (r, c)
        for r in range(1, rows - 1)
        for c in range(1, cols - 1)
        if maze[r][c] == ' '
    ]
    random.shuffle(open_cells)

    for r, c in open_cells[:num_treasures]:
        maze[r][c] = 'T'

    return [''.join(row) for row in maze]
