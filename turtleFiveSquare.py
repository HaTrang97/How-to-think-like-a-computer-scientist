import turtle 

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.forward(sz*2)
    t.pendown()

def draw_five_square():
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    alex = turtle.Turtle()
    alex.color('hot pink')
    for i in range(5):
        draw_square(alex, 20)
    wn.exitonclick()
    
draw_five_square()
