import turle

def draw_multicolor_square(t, sz):
  for i in ['red', yellow', 'hotpink', 'blue']:
      t.color(i)
      t.forward(sz)
      t.left(90)
      
wn = turtle.Screen(
wn.bgcolor('lightgreen')
tess = turtle.Turtle()
tess.pensize(3)
tess.speed(10)

size = 20
for i in range(20):
    draw_multicolor_square(tess,size)
    size += 10 
    tess.forward(10)
    tess.right(15)
    
wn.mainloop()
