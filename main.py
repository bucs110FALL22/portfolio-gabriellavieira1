import BitcoinAPI #Proxy Class
import pygame



def main():
  pygame.init()
  screen_width= 400
  screen_height= 400
  screen = pygame.display.set_mode([screen_width, screen_height])
  screen_color = (255,255, 255)
  screen.fill(screen_color)
  pygame.display.flip()

  text_color= (0,0,0)
  font_1 = pygame.font.Font(None,40)
  text_1 = font_1.render("Bitcoin",True, text_color)
  screen.blit(text_1,(50, 150))
  
  pygame.display.flip()
  pygame.display.update()


  

main()