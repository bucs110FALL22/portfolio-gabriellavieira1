def star_pyramid(): 
  print("How many rows do you want?: ")
  guess = int(input(""))
              
  for i in range (1, guess + 1):
    print(i * "*")

star_pyramid()
