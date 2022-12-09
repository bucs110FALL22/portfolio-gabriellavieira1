import pygame

class Write:
   def __init__(write1, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     write1.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     write1.rect= write1.image.get_rect()
     write1.rect.topleft = (x,y)
     write1.clicked=False
      