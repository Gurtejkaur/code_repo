import turtle
y=-200
turtle.color("blue")
for x in range(10):
    turtle.penup()
    turtle.setposition(-200,y)
    turtle.pendown()
    turtle.forward(400)
    y += 10
turtle.color("green")
for x in range(10):
    turtle.penup()
    turtle.setposition(-200,y)
    turtle.pendown()
    turtle.forward(400)
    y += 10
        
