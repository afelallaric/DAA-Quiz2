import math
import turtle
import game_state

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
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in game_state.walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        #Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in game_state.walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        #Calculate the spot to move to
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in game_state.walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        #Calculate the spot to move to
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        
        #Check if the space has a wall
        if (move_to_x, move_to_y) not in game_state.walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        return distance < 5

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
