import pygame

class Button:
   def __init__(bee, x, y, image, scale):
     width= image.get_width()
     height= image.get_height()
     bee.image = pygame.transform.scale(image, (int(width * scale ), int(height*scale)))
     bee.rect= bee.image.get_rect()
     bee.rect.topleft = (x,y)
     bee.clicked=False

 ##  def create(self,surface):
     # movement= True
     # pos = pygame.mouse.get_pos()
      
      # if self.rect.collidepoint(pos):
      #   if pygame.mouse.get_pressed()[0]==1 and self.clicked == False:
      #     self.clicked= True
      #     movement = True
          
      # if pygame.mouse.get_pressed()[0] ==0:
      #     self.clicked= False
      # surface.blit(self.image, (self.rect.x, self.rect.y))
    #  return movement

        
