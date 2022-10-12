def star_pyramid(): 
  print("How many rows do you want?: ")
  guess = int(input(""))
              
  for i in range (1, guess + 1):
    print(i * "*")

star_pyramid()

def rstar_pyramid():
  print("How many rows do you want?: ")
  question = int(input(""))

  for i in range (question, 0, -1):
    print(i * "*")

rstar_pyramid()



