import turtle

def draw_square(name, size):
    for i in range(4):
        name.forward(size)
        name.left(90)
if __name__ == '__main__':
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    alex = turtle.Turtle()
    alex.color('blue')
    alex.pensize(3)
    boxes = 20 
    
    for i in range(boxes):
        draw_square(alex,200)
        alex.left(360/boxes)
    
    wn.mainloop()
