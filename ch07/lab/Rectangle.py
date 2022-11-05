class Rectangle:
  def __init__(self, x, y, height,width):
    '''
    general function: Creates the Rectangle surface
    args: self, x, y, height, and width
    '''
    self.x=x
    self.y=y
    self.height=height
    self.width=width



def __str__(self):
  '''
  general function: Creates a string that contains the x, y, height, and width arguments that is then returned
  args: self 
  return: result_str
  
  
  '''
  result_str = f" x is {self.x}, y is{self.y}, height is{self.height}, width is{self.width}"
  return(result_str)
