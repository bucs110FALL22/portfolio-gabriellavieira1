# CS 110 Midterm Exam

## SHORT DESCRIPTION *(1 or 2 sentences describing your program)*
#This program draws my attempt at creating a variation of the emoji #who is sick and throwing up, which are then all outlined by a #square in the background.

## KNOWN BUGS AND INCOMPLETE PARTS *(list any known bugs or non working parts)*
#None

## REFERENCES *(any resource you use outside class materials)*
#None

## MISCELLANEOUS COMMENTS *(anything else you would like the grader to know)*
#None


import turtle

def drawSquare(lily, num_sides, side_length, loops=0):
  lily.penup()
  lily.goto(-200,200)
  lily.pendown()
  for i in range (loops):
     lily.pencolor("black")
     lily.forward(side_length)
     lily.right(360/num_sides)
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

def theOpenmouth(lily):
  lily.penup()
  lily.goto(2, 40)
  lily.pendown()
  lily.pencolor("black")
  lily.dot(80)
  lily.penup()

def drawSick(lily):
  lily.pendown()
  lily.pencolor("green")
  lily.pensize(50)
  lily.shape("turtle")
  lily.goto(-5,-500)


def main():

  wn=turtle.Screen()
  wn.bgcolor("white")
  
  lily=turtle.Turtle()
  lily.shape("arrow")
  lily.color("yellow")

  num_sides= 4
  side_length= 400

  drawSquare(lily, num_sides, side_length, loops=4)
  theCircle(lily)
  theEyes(lily)
  theOpenmouth(lily)
  drawSick(lily)
  
  wn.exitonclick()
  
main()


