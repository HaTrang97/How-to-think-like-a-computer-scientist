import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('Tess becomes a traffic light!')
tess = turtle.Turtle()

def draw_housing():
    tess.pensize(3)
    tess.color('gray', 'black')
    tess.begin_fill()
    tess.forward(80)
    tess.lt(90)
    tess.fd(200)
    tess.circle(40,180)
    tess.fd(200)
    tess.lt(90)
    tess.end_fill()

draw_housing()

tess.penup()
tess.forward(40)
tess.lt(90)
tess.fd(50)
tess.shape('circle')
tess.shapesize(3)
tess.fillcolor('red')

a = 0
def turtle_red():
    global a
    if a == 0:
        tess.forward(70)
        tess.fillcolor('yellow')
        a = 1
    elif a == 1:
        tess.forward(70)
        tess.fillcolor('lightgreen')
        a = 2
    elif a == 2:
        tess.back(140)
        tess.fillcolor('red')
        a = 0
        
showTurtle = 0
def show_turtle():
    global showTurtle
    if showTurtle == 0:
        tess.showturtle()

hideTurtle = 0
def hide_turtle():
    global hideTurtle
    if hideTurtle == 0:
        tess.hideturtle()
        
wn.onkey(turtle_red, 'space')
wn.onkey(hide_turtle, 'h')
wn.onkey(show_turtle, 's')

wn.listen()
wn.mainloop()
