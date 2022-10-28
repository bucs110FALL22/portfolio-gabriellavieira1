import turtle

def drawSquare(lily, num_sides, side_length):
  '''
   general function description: Creates square
   args: Args are lily the arrow, num_sides is the amount of sides used, and side_length is what makes the object long or short. All are types of strings
   return:  Loops is used to make the for loop run a specific amount and its type is an integer.
  '''
  loops=0
  lily.penup()
  lily.goto(-200,200)
  lily.pendown()
  lily.begin_fill()
  lily.fillcolor("white")
  for i in range (loops,4):
        lily.pencolor("black")
        lily.forward(side_length)
        lily.right(360/num_sides)
  lily.end_fill()
  
  return(loops)

def theCircle(lily):
  '''
   general function description: Creates the circle for the emoji 
   args: Lily is the arrow and is a string function
   return:  Lily is the arrow and is a string function 
  '''
  
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
  '''
   general function description: Creates the eyes
   args: Lily is the arrow and is a string function
   return: Lily is the arrow and is a string function 
  '''
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
  '''
   general function description: Creates the mouth
   args: Lily is the arrow whose type is a string
   return:Lily is the arrow whose type is a string
  '''
  
  lily.penup()
  lily.goto(2, 40)
  lily.pendown()
  lily.pencolor("black")
  lily.dot(80)
  lily.penup()

  return (lily)
  
def drawSick(lily):
  '''
   general function description: This creates the appeareance of throwing up
   args: Lily in this case is the turtle whose type is a string
   return:Lily is the turtle whose type is a string
  '''
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