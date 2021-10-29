import random
import turtle

s_width = 1000
s_height = 1000
x_indent = 20
y_indent = 20
dot_indent = 50
dot_diameter = 20

xy_tuples = []
y_cor = 0 - s_height / 2 + y_indent * 2
while y_cor < s_height / 2 - y_indent:
    x_cor = 0 - s_width/2 + x_indent * 2
    while x_cor < s_width/2 - x_indent:
        xy_tuples.append((x_cor, y_cor))
        x_cor += dot_diameter + dot_indent
    y_cor += dot_diameter + dot_indent

print(xy_tuples)

color_list = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]

screen = turtle.Screen()
screen.title("The Hirst Random Painting")
screen.setup(width=s_width, height=s_height)

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.penup()
timmy.speed("normal")
timmy.hideturtle()

while True:
    rand_tuple = random.choice(xy_tuples)
    timmy.goto(rand_tuple)
    timmy.color(random.choice(color_list))
    timmy.dot(20)
    xy_tuples.remove(rand_tuple)
    if len(xy_tuples) == 0:
        break

screen.exitonclick()
