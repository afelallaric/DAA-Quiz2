import game_state
from entities.treasure import Treasure
from entities.enemy import Enemy

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX   T    XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X  T      XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXXT XXXXXXXXXX      T  X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX             TX",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXX  XXXXXX",
    "XX    TXXXXXXXXXX  XXXXXX",
    "XX         XXXX        TX",
    "XXXXE                   X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

levels = ["", level_1]

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
