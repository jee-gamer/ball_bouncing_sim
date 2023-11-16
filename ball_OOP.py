import turtle
import random

class Ball:
    def __init__(self, ball_radius, canvas_width, canvas_height):
        self.xpos = random.randint(-1*canvas_width + ball_radius,
                                   canvas_width - ball_radius)
        self.ypos = random.randint(-1*canvas_height + ball_radius,
                                   canvas_height - ball_radius)
        self.vx = random.randint(1, 0.01*canvas_width)
        self.vy = random.randint(1, 0.01*canvas_height)
        self.color = ((random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255)))
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius

    def move(self):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        self.xpos += self.vx
        self.ypos += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (self.canvas_width - self.ball_radius):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (self.canvas_height - self.ball_radius):
            self.vy = -self.vy

    def draw_circle(self):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.xpos,self.ypos)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.ball_radius)
        turtle.end_fill()

class BallScreen:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.balls_radius = 0.05 * self.canvas_width
        self.ball_list = []

    def run(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        for i in range(self.num_balls):
            self.ball_list.append(Ball(self.balls_radius,
                                       self.canvas_width,
                                       self.canvas_height))
        while True:
            turtle.clear()
            for ball in self.ball_list:
                ball.draw_circle()
                ball.move()
            turtle.update()

        # hold the window; close it by clicking the window close 'x' mark
        # turtle.done()

screen = BallScreen(40)
screen.run()


