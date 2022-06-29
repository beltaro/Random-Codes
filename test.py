import turtle
import random
turtle.setup(600 ,600)
t_color = turtle.textinput("hello!", "what color do you want the background to be ?")
turtle.bgcolor(t_color)
x1 = 2
y1 = 4
l_p = turtle.textinput("name", "left player's name")
r_p = turtle.textinput("name", "right player's name")
l_ps = 0
r_ps = 0
p = 0
scripts = (str(l_p)+':'+str(l_ps)+'   '+str(r_p)+':'+str(r_ps))
pen = turtle.Turtle()
a=turtle.Turtle()
b=turtle.Turtle()
sketch = turtle.Turtle()
esc_b = turtle.Turtle()
esc_t = turtle.Turtle()
res_b = turtle.Turtle()
res_t = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
if turtle.bgcolor()=='black':
    sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 250)
sketch.write(scripts, font = ("Verdana", 15, "normal"), align = 'center')
pen.penup()
a.penup()
b.penup()
esc_b.penup()
esc_t.penup()
res_t.penup()
res_b.penup()
def forwarda():
    a.forward(50)
def backwarda():
    a.backward(50)
def forwardb():
    b.forward(50)
def backwardb():
    b.backward(50)
def  esc():
    p = 1
turtle.penup()
turtle.addshape("untitled.gif")
a.shape("untitled.gif")
turtle.addshape("untitled2.gif")
b.shape("untitled2.gif")
a.forward(280)
a.left(90)

b.backward(280)
b.left(90)
def res():
    p = 0
turtle.shape('circle')
turtle.speed('fastest')
if turtle.bgcolor()=='black':
    turtle.color('white')
sketch.clear()
while p<1:
    scripts = (str(l_p)+':'+str(l_ps)+'   '+str(r_p)+':'+str(r_ps))
    turtle.onkey(esc, 'Escape')
    turtle.onkey(forwarda,'Up')
    turtle.onkey(backwarda,'Down')
    turtle.onkey(forwardb,'w')
    turtle.onkey(backwardb,'s')
    x ,y = turtle.position()
    x2,y2=a.position()
    x3,y3=b.position()
    sketch.write(scripts, font = ("Verdana", 15, "normal"), align = "center")
    turtle.goto(x+x1 ,y+y1)
    if 260<x<270:
        if y2-72<y<y2+78:
            x1 = random.randint(-7,-2)
        else:
            sketch.clear()
            turtle.goto(0 ,0)
            l_ps = l_ps+1
    if -270<x<-260:
        if y3-72<y<y3+78:
            x1 = random.randint(2,7)
        else:
            sketch.clear()
            turtle.goto(0 ,0)
            r_ps = r_ps+1
    if y>300:
        y1 = random.randint(-7,-2)
    if y<-300:
        y1 = random.randint(2,7)

        
    turtle.listen()
#