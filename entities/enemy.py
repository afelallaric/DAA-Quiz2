import heapq
import turtle
from collections import deque
import game_state
from utils import get_neighbours

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
        if game_state.Algorithm == "dijkstra":
            return self.dijkstra(start, finish)
        elif game_state.Algorithm == "dfs":
            return self.dfs(start, finish)
        elif game_state.Algorithm == "bfs":
            return self.bfs(start, finish)
        else:
            print("Algorithm not found")
            return None

    def dijkstra(self, start, finish):
        pq = [(0, start, [start])]
        visited = set()
        while pq:
            cost, current, path = heapq.heappop(pq)
            if current == finish:
                return path
            if current in visited:
                continue
            visited.add(current)
            for neighbour in get_neighbours(current):
                if neighbour not in visited:
                    heapq.heappush(pq, (cost + 1, neighbour, path + [neighbour]))

    def dfs(self, start, finish):
        stack = [(start, [start])]
        visited = set()
        while stack:
            current, path = stack.pop()
            if current == finish:
                return path
            if current in visited:
                continue
            visited.add(current)
            for neighbour in get_neighbours(current):
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour]))

    def bfs(self, start, finish):
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            current, path = queue.popleft()
            if current == finish:
                return path
            if current in visited:
                continue
            visited.add(current)
            for neighbour in get_neighbours(current):
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour]))

    def set_path(self):
        start = (self.xcor(), self.ycor())
        finish = (game_state.player.xcor(), game_state.player.ycor())
        self.path = self.chooseAlgorithm(start, finish)

    def reset_path(self):
        start = (self.xcor(), self.ycor())
        finish = (game_state.player.xcor(), game_state.player.ycor())
        self.path = self.chooseAlgorithm(start, finish)
        self.move_index = 1

    def move(self):
        if self.move_index >= len(self.path):
            self.reset_path()
        if self.move_index < len(self.path):
            next_pos = self.path[self.move_index]
            self.goto(next_pos[0], next_pos[1])
            self.move_index += 1
        turtle.ontimer(self.move, t=132)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
