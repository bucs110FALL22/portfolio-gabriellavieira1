import pygame

class No:
   def __init__(no1, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     no1.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     no1.rect= no1.image.get_rect()
     no1.rect.topleft = (x,y)
     no1.clicked=False
      