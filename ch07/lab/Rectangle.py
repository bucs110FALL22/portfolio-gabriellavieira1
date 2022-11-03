class Rectangle:
  def __init__(self, x=0, y=0, height=0,width=0):
    self.x=x
    self.y=y
    self.height=height
    self.width=width


  def getX(self):
    return(self.x)

  def getY(self):
    return(self.y)

  def getHeight(self):
    return(self.height)

  def getWidth(self):
    return(self.width)

    
def driver():
  r = Rectangle(5, 7, 10,10)
  print(r.getX())
  print(r.getY())
  print(r.getHeight())
  print(r.getWidth())