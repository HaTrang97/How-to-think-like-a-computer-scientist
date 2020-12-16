% let the turtle move a shape like a clock
import turtle
screen = turtle.Screen() % view screen
screen.bgcolor('lightgreen') % set back ground color
screen.title('Hello, Trang!') % set the title 

alex = turtle.Turtle() % give him a name!
alex.shape('turtle') % let alex be a turtle
alex.color('blue') % set the color for the turtle
alex.pensize(3) 
alex.speed(5) % speed can be from 0 to 10

for i in range(12):
    alex.penup()
    alex.forward(90)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(20)
    alex.stamp()
    alex.backward(120)
    alex.right(30)
    
alex.stamp()
screen.mainloop() % wait for user to close window
