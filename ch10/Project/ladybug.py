import pygame

class Ladybug:
   def __init__(ladybug1, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     ladybug1.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     ladybug1.rect= ladybug1.image.get_rect()
     ladybug1.rect.topleft = (x,y)
     ladybug1.clicked=False
        
