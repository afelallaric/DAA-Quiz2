import math
import turtle
import heapq
from collections import deque

Algorithm = "bfs"

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Treasure Hunter Game")
wn.setup(700, 700)

# Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)   

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        #Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        #Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
    
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.path = []       
        self.move_index = 0

    def chooseAlgorithm(self, start, finish):
        if Algorithm == "dijkstra":
            return Enemy.dijkstra(self, start, finish)
        elif Algorithm == "dfs":
            return Enemy.dfs(self, start, finish)
        elif Algorithm == "bfs":
            return Enemy.bfs(self, start, finish)
        else:
            print("Algorithm not found")
            return None

    def dijkstra(self,start, finish):
        pq = [(0, start, [start])]
        visited = set()

        while pq:
            cost, current, path = heapq.heappop(pq)

            if current == finish:
                return path
            if current in visited:
                continue
            visited.add(current)

            neighbours = get_neighbours(current)
            for neighbour in neighbours:
                if neighbour not in visited:
                    heapq.heappush(pq, (cost + 1, neighbour, path + [neighbour]))

    def dfs(self, start, finish):
        stack = [(start, [start])]
        visited = set()

        while stack:
            current, path = stack.pop() # Ambil value paling depan di queue

            if current == finish:
                return path               
            if current in visited:
                continue               
            visited.add(current)

            neighbours = get_neighbours(current)
            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour]))

    def bfs(self, start, finish): 
        queue = deque([(start, [start])]) # Berisi {(posisi tile, path menuju posisi tersebut), (posisi tile, path menuju posisi tersebut), dst)}
        visited = set()

        while queue:
            current, path = queue.popleft() # Ambil value paling depan di queue

            if current == finish:
                return path               
            if current in visited:
                continue               
            visited.add(current)

            neighbours = get_neighbours(current)
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour])) # Masukkan value baru ke bagian paling belakang queue

    def set_path(self):
        start = (self.xcor(), self.ycor())
        finish = (player.xcor(), player.ycor())
        self.path = self.chooseAlgorithm(start, finish)  

    def reset_path(self):
        start = (self.xcor(), self.ycor())
        finish = (player.xcor(), player.ycor())
        self.path = self.chooseAlgorithm(start, finish)
        self.move_index = 1

    def move(self):
        # Jika sudah sampai di akhir path, dapatkan path yang baru
        if self.move_index >= len(self.path):
            self.reset_path()

        # Gerak ke tile berikutnya sesuai path
        if self.move_index < len(self.path):
            next_pos = self.path[self.move_index]
            self.goto(next_pos[0], next_pos[1])
            self.move_index += 1

        turtle.ontimer(self.move, t=132) # gerak setiap 132 ms ke tile berikutnya sesuai path

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


#Create Level List
levels = [""]

#Define first level
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
"XXXXXXXXXXXXXXXXXXXXXXXXX"        
]

#Add a treasures list
treasures = []

#Add an enemies list
enemies = []

#Add maze to mazes list
levels.append(level_1)

#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate
            #NOTE the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen s, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X (representing a wall))
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x, screen_y))
            
            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)

            #Check if it is a T (representing a treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            #Check if it is an E (representing an enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

#Create class instances
pen = Pen()
player = Player()

#Create wall coordinate list
walls = []

# helper: neighbour positions on the grid
def get_neighbours(pos):
    x, y = pos
    candidates = [(x + 24, y), (x - 24, y), (x, y + 24), (x, y - 24)]
    return [n for n in candidates if n not in walls]


#Set up the level
options = ['dijkstra', 'dfs', 'bfs']
input_message = "Pick an algorithm:\n" 

for index, item in enumerate(options):
  input_message += f'{index + 1}) {item}\n'

input_message += 'Your choice (enter number or name): '

Algorithm = input(input_message)
if Algorithm == "1":
    Algorithm = "dijkstra"
elif Algorithm == "2":
    Algorithm = "dfs"
elif Algorithm == "3":
    Algorithm = "bfs"
else:
    print("Invalid choice. Please try again.")
    exit()




setup_maze(levels[1])

#Start enemy movement
for enemy in enemies:
    enemy.set_path()
    enemy.move()

#Keyboard Binding
turtle.listen()
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")

#Turn off screen updates
wn.tracer(0)

#Main Game Loop
while True:
    #Check for player collision with treasure
    #Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #Add the treasure's gold to the player's gold
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            #Destroy the treasure
            treasure.destroy()
            #Remove the treasure from the treasures list
            treasures.remove(treasure)

    #Iterate through the enemy list
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player Died!")
            print("Game Over")
            #Print player total gold
            print("Total Player Gold: {}".format(player.gold))
            #Destroy the player and enemy
            player.destroy()
            enemy.destroy()
            #Close the window and stop the program
            wn.bye()
            raise SystemExit

    #Update the screen
    wn.update()