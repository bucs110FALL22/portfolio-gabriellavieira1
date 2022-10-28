import turtle

def drawSquare(lily, num_sides, side_length):
  loops=4
  lily.penup()
  lily.goto(-200,200)
  lily.pendown()
  lily.begin_fill()
  lily.fillcolor("white")
  for i in range (loops):
        lily.pencolor("black")
        lily.forward(side_length)
        lily.right(360/num_sides)
  lily.end_fill()
  
  return(loops)

def theCircle(lily):

  
  lily.penup()
  lily.goto(0,0)
  lily.pendown()
  lily.begin_fill()
  lily.fillcolor("yellow")
  lily.circle(100)
  lily.end_fill()
  lily.penup()
  
  return(lily)
  
def theEyes(lily):

  
  lily.goto(50, 120)
  lily.pendown()
  lily.pencolor("black")
  lily.dot(30)
  lily.penup()

  lily.goto(-50, 120)
  lily.pendown()
  lily.pencolor("black")
  lily.dot(30)
  lily.penup

  return(lily)
  
def theOpenmouth(lily):

  
  lily.penup()
  lily.goto(2, 40)
  lily.pendown()
  lily.pencolor("black")
  lily.dot(80)
  lily.penup()

  return (lily)
  
def drawSick(lily):
 
  
  lily.pendown()
  lily.pencolor("green")
  lily.pensize(50)
  lily.shape("turtle")
  lily.goto(-5,-500)

  return (lily)
  
def main():

  wn=turtle.Screen()
  wn.bgcolor("blue")
  
  lily=turtle.Turtle()
  lily.shape("arrow")
  lily.color("yellow")

  num_sides= 4
  side_length= 400

  drawSquare(lily, num_sides, side_length)
  theCircle(lily)
  theEyes(lily)
  theOpenmouth(lily)
  drawSick(lily)
  
  wn.exitonclick()
  
main()