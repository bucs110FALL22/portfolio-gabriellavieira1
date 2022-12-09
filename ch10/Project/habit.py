import pygame

class Habit:
   def __init__(flower4, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     flower4.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     flower4.rect= flower4.image.get_rect()
     flower4.rect.topleft = (x,y)
     flower4.clicked=False
      
  
  
  
  