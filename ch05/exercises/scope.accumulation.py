
def multiply(a=0, b=0):
  accumulator=0
  for i in range(b):
    accumulator= accumulator + a
    return accumulator


def exponent(a=0, b=0):
  accumulator=1
  for i in range(b):
    accumulator= accumulator*a

  return accumulator

def square(var):
  return multiply(var, var)


def main():
  result= multiply(a=3, b=5)
  print(result)

  result=multiply()
  print(result)

  result= multiply(a=3,b=5)
  print(result)


  result= exponent(a=6,b=7)
  print(result)

  result= square(2)
  print(result)
main()