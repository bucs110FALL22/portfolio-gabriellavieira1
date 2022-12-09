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








#Part C- Couldn't get to work
#window.fill("white")
#blue=pygame.draw.rect(window,"blue",(150,125,100,50 ))
#red=pygame.draw.rect(window,"red",(300,150,100 ,50))
#pygame.display.flip()
#pygame.time.wait(2000)

#guess= print("Please select either (player 1) Blue or (player 2) Red as your choice for the winner?  ")

#player= int(input("Pick 1 for player blue or 2 for player red: "))

#player_blue=random.randrange(0,500)
#player_blue1=random.randrange(0,500)
#player_red=random.randrange(0,500)
#player_red2=random.randrange(0,500)
#players = ["blue", "red"]
#blue_score = 0
#red_score = 0

#window= pygame.display.set_mode((500,500))
#window.fill("blue")
#pygame.display.flip()
#window_size = pygame.display.get_window_size()

#radius = window_size[0]/2

#pygame.draw.circle(window, "pink", (window_size[0]/2, window_size[1]/2), radius)
#pygame.display.flip()


#x1=0
#y1=250
#start_pos1= (x1, y1)
#x2=500
#y2=250
#end_pos1= (x2,y2)
          
#pygame.draw.line(window, "black", start_pos1, end_pos1, width=2)
#pygame.display.flip()


#x3= 250
#y3=500
#start_pos2=(x3,y3)
#x4=250
#y4=0
#end_pos2=(x4,y4)
#pygame.draw.line(window, "black", start_pos2, end_pos2, width=2)
#pygame.display.flip()


#for i in range(11):
  #width=500
  #point1= (player_blue,player_blue1)
  #point2=(player_red, player_red2)
  
  #distance_from_center = math.hypot(player_blue-250, player_blue1-250)
  #distance_from_center2 = math.hypot(player_red-250, player_red2-250)
  
  #is_in_circle = distance_from_center <= width/2
  #is_in_circle2 = distance_from_center2 <= width/2
  
  #player_blue=random.randrange(0,500)
  #player_blue1=random.randrange(0,500)
 # player_red=random.randrange(0,500)
  #player_red2 =random.randrange(0,500)
  
  #if is_in_circle== True:
  #  pygame.draw.circle(window, "blue", (player_blue,player_blue1),10)
  #  pygame.display.flip()
  #  pygame.time.wait(2000)
  #  print("Hit")
  #if player is players[0]:
 #   blue_score += 1
 # if is_in_circle== False:
   # pygame.draw.circle(window, "yellow", (player_blue,player_blue1),10)
   # pygame.display.flip()
   # pygame.time.wait(2000)
   # print("Miss!")
   # blue_score += 0
    
 # if is_in_circle2== True:
  #  pygame.draw.circle(window, "orange", (player_red,player_red2),10)
   # pygame.display.flip()
   # pygame.time.wait(2000)
   # print("Hit")
  #if player is players[1]:
 #   red_score += 1
 # if is_in_circle2== False:
 #   pygame.draw.circle(window, "white", (player_red,player_red2),10)
  #  pygame.display.flip()
  #  pygame.time.wait(2000)
  #  print("Miss!")
 #   red_score += 0
  
 # if i == 10: 
 #   if blue_score > red_score:
 #       print(players[0], "has won the game")
 #   if player is players[1]:
 #       print(players[1], "has won the game")
#    if blue_score == red_score:
#        print("The game finishes with a tie")
#pygame.display.flip()
#pygame.time.wait(2000)



#player_is_right = True
#while player_is_right == True:
 #   for event in pygame. event.get():
 #     if event.type == pygame.MOUSEBUTTONDOWN:
#        if event.button == 1:
#          player = "1"
#          player_is_right = False
          
#        if event.button == 2 :
 #         player = "2"  #answer_for_player
#          player_is_right = False
#print("Your choice was: ", player)

#while player_is_right == True:
#    if player == player_is_right:
#        print("You got the right answer, congrats!")
#    else:
#        print("You did not choose the right person. Good luck next time.")
  
#pygame.display.flip()
#pygame.time.wait(2000)

#window.exitonclick()