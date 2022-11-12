import pygame, sys
from pygame.locals import QUIT


pygame.init()
dislay= pygame.display.set_mode((400, 300))
pygame.dsiplay.set_caption("Hello World")

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  canvas = pygame.Surface((200,150))
  canvas.fill("red")
  display.blit(canvas, (10,10))
  pygame.display.update 
  