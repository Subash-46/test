from turtle import Screen, Turtle


a_turtle = Turtle()
colors = "pink", "yellow", "blue", "green", "white", "red"
Screen().bgcolor("black")

for i in range(200):
    a_turtle.pencolor(colors[i % 6])
    a_turtle.width(i / 300 + 1)
    a_turtle.forward(i)
    a_turtle.left(59)

Screen().done()
