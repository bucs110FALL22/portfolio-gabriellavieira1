import JokeAPI 
import YodaAPI 
import pygame



def main():
  pygame.init()
  screen_width= 600
  screen_height= 600
  screen = pygame.display.set_mode([screen_width, screen_height])
  screen_color = (255,255, 255)
  screen.fill(screen_color)
  pygame.display.flip()

  text_color= (0,0,0)
  font_1 = pygame.font.Font(None,40)
  text_1 = font_1.render("Joke: ",True, text_color)
  

  text_2 = font_1.render("Yoda Joke: ",True, text_color)
  screen.blit(text_1,(50, 150))
  screen.blit(text_2,(50, 250))
  
  pygame.display.flip()

def showjoke(self):
  '''
  general function: To show the joke on the pygame screen and the shell
  args: self
  return: self
  '''
  text= (f"{joke['jokes']} Joke is:")
  print(text)
  statement= joke['jokes']
  text_3 = font_1.render(statement,True, text_color)
  screen.blit(text_3, (100, 150))
  pygame.display.flip()
  return self

def version(self):
  '''
  general function: Show the joke translated in Yoda on the pygame screen and the shell.
  args: self
  return: self
  '''
  new= (f"{yoda['translated(text)']} Joke in Yoda is:")
  print(new)
  statement2= yoda['translated(text)']
  text_4 = font_1.render(statement2,True, text_color)
  screen.blit(text_4, (100, 250))
  pygame.display.flip()
  return self

main()