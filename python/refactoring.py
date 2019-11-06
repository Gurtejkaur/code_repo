import turtle
y=200
def draw_lines(color,y):
    turtle.color(color)
for x in range (10):
    turtle.penup()
    turtle.setposition(-200,y)
    turtle.pendown()
    turtle.forward(400)
    y+=10
    
turtle.tracer(0)

draw_lines("red",-200)
draw_lines("blue",-100)
draw_lines("green",0)    
draw_lines("black",100)
turtle.update()
turtle.done()

    
