import turtle

screen = turtle.Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.bgcolor("tan")

t = turtle.Turtle()

t.penup()
t.goto(80,15)
t.pendown()
t.pencolor("red")
t.setheading(0)
t.circle(35)
t.end_fill()

t.penup()
t.goto(0,15)
t.pendown()
t.pencolor("black")
t.circle(35)
t.end_fill()

t.penup()
t.goto(-80,15)
t.pendown()
t.pencolor("blue")
t.circle(35)
t.end_fill()

t.penup()
t.goto(40,-15)
t.pendown()
t.pencolor("green")
t.circle(35)
t.end_fill()

t.penup()
t.goto(-40,-15)
t.pendown()
t.pencolor("yellow")
t.circle(35)
t.end_fill()

t.penup()
t.goto(0,100)
t.pencolor("purple")
t.pendown()
t.write("Winter Olympics", font=("Arial",30,"bold"),align="center")

t.penup()
t.goto(0,-85)
t.pendown()
t.write("2026", font=("Arial",30,"bold"),align="center")

# No code beyond this line
turtle.done()