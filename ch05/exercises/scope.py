import turtle

#def drawEqShape(leo, num_sides, side_length):
def drawEqShape():
  wn=turtle.Screen()
  wn.bgcolor("yellow")
  
  leo = turtle.Turtle()
  leo.shape("turtle")
  leo.color("green")
  
  side_length = int(input("How long do you want the  sides to be?: "))
  num_sides = int(input("How many sides do you want?:"))
  
  for i in range (0, side_length):
        leo.forward(side_length)
        leo.left(360/num_sides)
#wn.exitonclick()
#nums = [leo, num_sides, side_length]
#drawEqShape(nums)
#print(nums )
drawEqShape()

