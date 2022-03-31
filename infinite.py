import turtle
screen = turtle.Screen()
screen.setup(550, 600, startx=0, starty=100)
# setup sirve para establecer el tamaño y la posicion de la ventana principal
t = turtle.Turtle() #* misma interface pero dibuja sobre un objeto por defecto 'Screen?
turtle.bgcolor('orange')
turtle.color('white')
turtle.speed(15)
# speed para la velocidad que en realidad podriamos poner simplemente 0 porque solo acepta enteros del 1-10
turtle.right(45)
for i in range(150):
    turtle.circle(25)
    if 7  < i < 62:
        turtle.left(5)
    if 80 < i < 133:
        turtle.right(5)
    if i < 80:
        turtle.forward(10)
    else:
        turtle.forward(5)

