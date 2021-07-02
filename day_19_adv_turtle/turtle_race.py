from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(height=400,width=500)
is_fiilup = screen.textinput("turtle race","which color of turtle win the race?")
color = ["red","green","blue","purple","yellow","orange"]
distance = [1,2,3,4,5]
member =[]
#objects of turtle
sumit = Turtle(shape="turtle")
sumit.color(color[0])
member.append(sumit)

pratik = Turtle(shape="turtle")
pratik.color(color[1])
member.append(pratik)

darshan = Turtle(shape="turtle")
darshan.color(color[2])
member.append(darshan)

prajyot = Turtle(shape="turtle")
prajyot.color(color[3])
member.append(prajyot)

shreyas = Turtle(shape="turtle")
shreyas.color(color[4])
member.append(shreyas)

nik = Turtle(shape="turtle")
nik.color(color[5])
member.append(nik)


#position of turtle
sumit.penup()
sumit.goto(-230,-100)

pratik.penup()
pratik.goto(-230,-50)

darshan.penup()
darshan.goto(-230,0)

prajyot.penup()
prajyot.goto(-230,50)

shreyas.penup()
shreyas.goto(-230,100)

nik.penup()
nik.goto(-230,150)

def race():
    sumit.forward(random.choice(distance))
    pratik.forward(random.choice(distance))
    prajyot.forward(random.choice(distance))
    darshan.forward(random.choice(distance))
    shreyas.forward(random.choice(distance))
    nik.forward(random.choice(distance))
if is_fiilup:
    state = True
while state:
    for turtle in member:
        if turtle.xcor()>230:
            state=False
            winning_color = turtle.pencolor()
            if is_fiilup==winning_color:
                print("you win!")
            else:
                print("you lose")
    race()



screen.exitonclick()