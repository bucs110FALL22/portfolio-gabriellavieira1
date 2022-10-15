def part2_a():
  n=0
  while (n<101) and (n!=1): 
    if n%2 ==0:
     n = n//2
    print("Even values: ", n)
  else: 
    n = n*3 +1
  print("Odd values: ", n)
part2_a()