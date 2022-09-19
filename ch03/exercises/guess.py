import random

num = random.randrange(1,11)
num_guesses= 0 
for i in range(3):
   guess_num = int(input("Please enter a guess:"))
   num_guesses = num_guesses + 1
   if guess_num < num:
    print("Too Low")
   elif guess_num > num:
    print("Too High")
   elif guess_num == num:
    print("Correct")
    break
print("It took you", num_guesses, "guesses")



# numbers_first = ("mylist")
# mylist = list(range(0,11))
# y = (random.choice(mylist))
# result = (y)
# print("Result: ", result)

