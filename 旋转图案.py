import turtle
turtle.width(1)
turtle.bgcolor("black")
colors=["red","yellow","blue","green","orange","purple"]
turtle.tracer(False)
for x in range(182):
    turtle.forward(2*x)
    turtle.color(colors[x%6])
    turtle.left(-299)
    turtle.width(x*6/210)
turtle.tracer(Ture)
turtle.done()
