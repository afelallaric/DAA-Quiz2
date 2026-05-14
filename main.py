import turtle
import game_state
from entities.pen import Pen
from entities.player import Player
from levels import levels, setup_maze

# Screen setup
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Treasure Hunter Game")
wn.setup(700, 700)

# Algorithm selection
options = ['dijkstra', 'dfs', 'bfs']
input_message = "Pick an algorithm:\n"
for index, item in enumerate(options):
    input_message += f'{index + 1}) {item}\n'
input_message += 'Your choice (enter number or name): '

choice = input(input_message)
if choice == "1":
    game_state.Algorithm = "dijkstra"
elif choice == "2":
    game_state.Algorithm = "dfs"
elif choice == "3":
    game_state.Algorithm = "bfs"
else:
    print("Invalid choice. Please try again.")
    exit()

# Initialize shared entities
game_state.pen = Pen()
game_state.player = Player()

# Setup level
setup_maze(levels[1])

# Start enemy movement
for enemy in game_state.enemies:
    enemy.set_path()
    enemy.move()

# Keyboard bindings
turtle.listen()
turtle.onkey(game_state.player.go_up, "Up")
turtle.onkey(game_state.player.go_down, "Down")
turtle.onkey(game_state.player.go_left, "Left")
turtle.onkey(game_state.player.go_right, "Right")

wn.tracer(0)

# Main game loop
while True:
    for treasure in game_state.treasures[:]:
        if game_state.player.is_collision(treasure):
            game_state.player.gold += treasure.gold
            print("Player Gold: {}".format(game_state.player.gold))
            treasure.destroy()
            game_state.treasures.remove(treasure)

    for enemy in game_state.enemies:
        if game_state.player.is_collision(enemy):
            print("Player Died!")
            print("Game Over")
            print("Total Player Gold: {}".format(game_state.player.gold))
            game_state.player.destroy()
            enemy.destroy()
            wn.bye()
            raise SystemExit

    wn.update()
