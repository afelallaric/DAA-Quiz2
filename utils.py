import game_state

def get_neighbours(pos):
    x, y = pos
    candidates = [(x + 24, y), (x - 24, y), (x, y + 24), (x, y - 24)]
    return [n for n in candidates if n not in game_state.walls]
