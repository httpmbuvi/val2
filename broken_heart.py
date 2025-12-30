import turtle

t = turtle.Turtle()
t.fillcolor("red")
t.pensize(3)
t.speed(3)

# Draw left half of heart
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)

# Save the top center position for the crack
top_notch = t.pos()

# Move to right side
t.left(120)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

# Draw crack
t.penup()
t.goto(top_notch)
t.pendown()
t.pencolor("black")
t.pensize(5)

# Draw a bold zig-zag crack to the bottom tip
t.goto(-15, 80)
t.goto(10, 50)
t.goto(-5, 25)
t.goto(0, 0)

t.hideturtle()
turtle.done()
