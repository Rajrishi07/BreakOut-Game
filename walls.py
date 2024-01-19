from turtle import Turtle
import random
COLOR = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue',
         'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray']


class Wall:

    def __init__(self):
        self.segments = []
        self.create_wall()

    def create_wall(self):
        for ycor in range(160, 60, -30 ):
            for xcor in range(-455, 500, 90):
                wall = Turtle()
                wall.shape('square')
                wall.turtlesize(stretch_len=4, stretch_wid=1)
                wall.penup()
                wall.goto(x=xcor, y=ycor)
                wall.fillcolor(random.choice(COLOR))
                self.segments.append(wall)

    def check_collision(self, ball):
        for wall in self.segments:
            if wall.distance(ball) <= 50 and ball.ycor()==wall.ycor():
                wall.hideturtle()
                self.segments.remove(wall)
                print(len(self.segments))
                ball.bounce_y()
                return True
        return False

    def get_walls(self):
        return len(self.segments)