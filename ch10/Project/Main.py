import pygame
import button

def main():
  pygame.init()
  screen_width= 650
  screen_height= 700
  screen = pygame.display.set_mode([screen_width, screen_height])
  screen_color = (210, 231, 214)
  screen.fill(screen_color)
  pygame.display.flip()
  text_color = (1,50,32)
  pygame.display.set_caption("Grow Your Garden")
  font = pygame.font.Font(None, 80)
  text = font.render("Grow Your Garden",True,text_color)
  text_rect = text.get_rect(center=(screen_width/2, screen_height/7))
  screen.blit(text,text_rect)
  pygame.display.flip()

  pygame.display.set_caption("Grow Your Garden")
  flower = pygame.image.load('Flower Icon.png')
  pygame.display.set_icon(flower)

  flower_1 = pygame.image.load('Flower 4.png')
  flower_1x= 200
  flower_1y= 280

  flower_2 = pygame.image.load('Flower 5.png')
  flower_2x=-20
  flower_2y=280

  flower_3 = pygame.image.load('Flower 6.png')
  flower_3x=420
  flower_3y= 280

  screen.blit(flower_1, (flower_1x, flower_1y))

  screen.blit(flower_2, (flower_2x, flower_2y))

  screen.blit(flower_3, (flower_3x, flower_3y))
  pygame.display.update()
  pygame.time.wait(2000)

  start=pygame.image.load('Bee.png').convert_alpha()
  bee =button.Button(260,150 , start, 0.8)

  running= True
  while running:
        for event in pygame.event.get(): 
          # movement= True
           # pos = event.pos
           # pos= pygame.mouse.get_pos()
           
          pos= pygame.mouse.get_pos()
        if bee.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and bee.clicked == False:
              bee.clicked= True
              #movement = True
              
        if pygame.mouse.get_pressed()[0] ==0:
              bee.clicked= False
        screen.blit(bee.image, (bee.rect.x, bee.rect.y))
        #return movement
    
        if bee.image(screen):
           print("START")
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
              running = False
        pygame.display.update()
        pygame.display.flip()

  pygame.quit() 
main()