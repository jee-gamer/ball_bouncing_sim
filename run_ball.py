import turtle
from ball import Ball

num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)
ball_list = []
for i in range(num_balls):
    ball_list.append(Ball(ball_radius,
                          canvas_width,
                          canvas_height))
while True:
    turtle.clear()
    for ball in ball_list:
        ball.draw_circle()
        ball.move()
    turtle.update()
# hold the window; close it by clicking the window close 'x' mark
turtle.done()
