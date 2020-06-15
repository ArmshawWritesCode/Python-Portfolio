#Hexagon art: nested
#make a geometric rainbow pattern
import turtle

#pick the order for the colors in the hexagon
colors = ['pink', 'blue', 'yellow', 'orange', 'green', 'pink']
star = turtle.Turtle()
turtle.bgcolor('black') #turn background color
#nested hexagonal pattern - 36 hexagons, each 10 degrees apart
for n in range(36):
    #repeat 6 times - move forward and turn
    for i in range(6):
        star.color(colors[i])
        star.forward(100)
        star.left(60)
    star.right(10)  #add a turn

#get ready to draw 36 white circles
star.penup()
star.color('white')

#repeat 36 times to match 36 hexagons
for i in range(36):
    star.forward(220)
    star.pendown()
    star.circle(5)
    star.penup()
    star.backward(220)
    star.right(10)
#hide turtle to finish drawing
star.hideturtle()
