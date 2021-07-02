# import colorgram
#
# colors = colorgram.extract("color.jpg",25)
# x=[]
# for i in colors:
#     red = i.rgb.r
#     green = i.rgb.g
#     blue = i.rgb.b
#     x.append((red,green,blue))
#
# print(x)
import turtle as t
import random
t.colormode(255)
t.penup()
t.hideturtle()
t.speed(10.0)
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138),
              (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151),
              (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]


t.setheading(225)
t.forward(350)
t.setheading(0)


for i in range(1,101):
    t.dot(20,random.choice(color_list))
    t.forward(50)
    if i % 10 ==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)



my_screen = t.Screen()
my_screen.exitonclick()