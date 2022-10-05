import turtle
import random

leo = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("blue")

leo.color("green")
leo.shape("turtle")

leo.up()
leo.goto(0,0) 

def isinscreen(wn, leo):
  if random.random() > 0.1:
    return True
  else:
    return False


while isinscreen(wn, leo):
  num = random.randrange(2)
  if num == 0:   
   (leo.left(90))
else:
   (leo.right(90))

leo.forward(50)


wn.exitonclick()
