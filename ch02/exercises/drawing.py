import turtle

wn=turtle.Screen()
wn.bgcolor("green")

turtle.color("blue")
turtle.shape("turtle")

sides = int(input("How many sides do you want the image to have?:"))
length = int(input("How much do you want the length to be for the image?:"))

for i in range(0,sides):
  turtle.fd(length)
  turtle.lt(360/sides)


wn.exitonclick()