import Rectangle

class Surface:
  def __init__(self, Rectangle , x, y, height, width):
    self.rect= (x,y,height,width)
    self.image= Rectangle

  def getRect(self):
    return(self.rect)