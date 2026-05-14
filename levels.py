import game_state
from entities.treasure import Treasure
from entities.enemy import Enemy
from maze_generator import build_level

levels = ["", build_level()]

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                game_state.pen.goto(screen_x, screen_y)
                game_state.pen.stamp()
                game_state.walls.append((screen_x, screen_y))

            if character == "P":
                game_state.player.goto(screen_x, screen_y)

            if character == "T":
                game_state.treasures.append(Treasure(screen_x, screen_y))

            if character == "E":
                game_state.enemies.append(Enemy(screen_x, screen_y))
