#Part A
import pygame 
import random
import math
pygame.display.init()


window= pygame.display.set_mode((500,500))
window.fill("blue")
pygame.display.flip()
window_size = pygame.display.get_window_size()

radius = window_size[0]/2

pygame.draw.circle(window, "pink", (window_size[0]/2, window_size[1]/2), radius)
pygame.display.flip()


x1=0
y1=250
start_pos1= (x1, y1)
x2=500
y2=250
end_pos1= (x2,y2)
          
pygame.draw.line(window, "black", start_pos1, end_pos1, width=2)
pygame.display.flip()


x3= 250
y3=500
start_pos2=(x3,y3)
x4=250
y4=0
end_pos2=(x4,y4)
pygame.draw.line(window, "black", start_pos2, end_pos2, width=2)
pygame.display.flip()


#Part B
for i in range(11):
  x5=random.randrange(0,500)
  y5=random.randrange(0,500)
  width=500
  points= (x5,y5)
  distance_from_center = math.hypot(x5-250, y5-250)
  is_in_circle = distance_from_center <= width/2
  
  if is_in_circle == True:
    pygame.draw.circle(window, "green", (x5,y5),10)
    pygame.display.flip()
    pygame.time.wait(2000)
  if is_in_circle == False:
    pygame.draw.circle(window, "red", (x5,y5),10)
    pygame.display.flip()
    pygame.time.wait(2000)

print(points)
print(distance_from_center)
print(is_in_circle)
pygame.time.wait(2000)


#Part C
window.fill("white")
pygame.draw.rect(window,"blue",(150,125,100,50 ))
pygame.display.flip()
pygame.time.wait(2000)

pygame.draw.rect(window,"red",(300,150,100 ,50))
pygame.display.flip()
pygame.time.wait(2000)


print("Please select either (player 1) Blue or (player 2) Red as your choice for the winner?  ")
guess= ""
player= ""

player_1=random.randrange(0,500)
player_2 =random.randrange(0,500)
width=500
points= (x5,y5)
distance_from_center = math.hypot(x5-250, y5-250)
is_in_circle = distance_from_center <= width/2

players = ["blue", "red"]
blue_score = 0
red_score = 0

for i in range(10):
  player_1=random.randrange(0,500)
  player_2 =random.randrange(0,500)
  if if is_in_circle== True:
    pygame.draw.circle(window, "green", (x5,y5),10)
    pygame.display.flip()
    pygame.time.wait(2000)
    print("Hit")
  if player is players[0]:
      blue_score += 1
  if player is players[1]:
      red_score += 1
  if is_in_circle== False:
    pygame.draw.circle(window, "yellow", (x5,y5),10)
    pygame.display.flip()
    pygame.time.wait(2000)
    print("Miss!")

  
  if i == 9: 
    if blue_score > red_score:
        print(players[0], "has won the game")
    if player is players[1]:
        print(players[1], "has won the game")
    if blue_score == red_score:
        print("The game finishes with a tie")
pygame.display.flip()
pygame.time.wait(2000)



guess_is_right = True
while guess_is_right == True:
  player_1=random.randrange(0,500)
  player_2 =random.randrange(0,500)
  for event in pygame. event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          answer_for_guess = "blue"
          guess_is_right = False
          
        if event.button == 3 :
          answer_for_guess = "red"
          guess_is_right = False
print("Your choice was: ", guess)

while guess_is_right == True:
  if guess == guess_is_right:
        print("You got the right answer, congrats!")
  else:
        print("You did not choose the right person. Good luck next time.")
  
pygame.display.flip()
pygame.time.wait(2000)

#window.exitonclick()