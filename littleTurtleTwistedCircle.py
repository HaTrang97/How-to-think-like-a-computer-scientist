% let the turtle shape a twisted circle 

import turtle
screen = turtle.Screen()
screen.bgcolor('lightgreen')

alex = turtle.Turtle()
alex.shape('turtle')
alex.color('blue')

alex.penup()
size = 20    % the distance between the steps 
for i in range(30):
    alex.stamp()
    size = size + 3  % increase the size on every iteration
    alex.forward(size) % move alex along 
    alex.right(24)  %and turn him
    
screen.mainloop()   % wait for user close the window 
