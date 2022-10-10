import turtle
import random

leo = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("white")

leo.color("green")
leo.shape("turtle")
leo.speed(0)

distance = 10
angle = 90
in_screen = True

colors = ["green", "blue", "purple"]
while in_screen:
  coin = random.randrange(0,2)
  if coin==0:    #Heads
      leo.left(angle)
  else:     #Tails
      leo.right(angle)
      leo.fd(distance)

x_range = wn.window_width()/2
y_range = wn.window_height()/2
turtleX =leo.xcor()
turtleY = leo.ycor()

leo.colors(colors[0])
colors.append(colors.pop(0))

if abs(turtleX) > x_range or abs(turtleY) > y_range:
  in_screen = False

wn.exitonclick()
