import pygame

class Choice:
   def __init__(flower5, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     flower5.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     flower5.rect= flower5.image.get_rect()
     flower5.rect.topleft = (x,y)
     flower5.clicked=False
      
  
  
  
  