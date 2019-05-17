import math 

def is_prime( x ):
  for i in range(2, math.sqrt(x) ):
    if x % i == 0:
      return False  
  return True

t = int(input())
for j in range(t):
  n = int(input())
  most=0
  for i in range(int(math.sqrt(n))+1):
    if n % i == 0 and is_prime(i) and most < i :
      most = i
  print(most)
