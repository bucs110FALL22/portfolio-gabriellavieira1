#Function 1
def percentage_to_letter(score=0):
  if score>=90:
    print("A")
  elif score==80 and score<90:
    print("B")
  elif score==70 and score<80:
    print("C")
  elif score==60 and score<70:
    print("D")
  elif score<=59:
    print("F")

  return score
#score == 80 and score<90

#Function 2
def is_passing(letter=None):
  for score in ("A", "B", "C"):
    print("True")
  else: 
    print(False)


#Main 
score = float(input("Please enter the grade you got: "))
percentage_to_letter(score)
result = (percentage_to_letter)
is_passing(result)
  