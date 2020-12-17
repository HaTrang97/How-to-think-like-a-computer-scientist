import turtle
import math

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.right(135)
    t.forward(10 * math.sqrt(2))
    t.pendown()
    t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    alex = turtle.Turtle()
    alex.pensize(3)
    alex.color('hot pink')
    size = 20
    for i  in range(5):
        draw_square(alex, size)
        size += 20
    wn.mainloop()

main()
