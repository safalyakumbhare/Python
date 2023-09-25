# Holi Special Python Code

import turtle
import random

# set up turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.bgcolor("black")

# create all RGB colors
colors = []
for i in range(100):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors.append((r,g,b))

# set up colors position and count
x = -300
y = 200
count = 0

# use for loop and if statement to repeat 100 colors
for i in range(100):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(colors[count])
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    x += 50
    
    if x > 300:
        y -= 50
        x = -300
        
    count += 1
    
# write Happy Holi!
t.penup()
t.goto(-150,-250)
t.pendown()
t.color("white")
t.write("Happy Holi!", font=("Arial",40,"bold"))

turtle.done()
