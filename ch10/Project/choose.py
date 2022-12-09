import pygame

class Choose:
   def __init__(flower7, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     flower7.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     flower7.rect= flower7.image.get_rect()
     flower7.rect.topleft = (x,y)
     flower7.clicked=False
      
  
  
  
  