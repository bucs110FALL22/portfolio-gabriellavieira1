from Rectangle import Rectangle

class Surface:
  def __init__(self, filename , x, y, height, width):
    '''
    general function: Creates the surface incorporated with the Rectangle
    args: self, filename, x, y, height, and width
    
    
    '''
    self.rect=Rectangle(x, y, height, width)
    self.image= filename


  def getRect(self):
    '''
    general function: return the self.rect that makes up the Rectangle x, y, height, and width coordinates
    args: self
    return: self.rect
    
    
    '''
    return(self.rect)