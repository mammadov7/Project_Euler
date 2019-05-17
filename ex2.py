def fibo( x ):
  a, b = 1, 2
  sum = 0
  while( b < x ):
    a, b = b, a + b
    if a % 2 == 0:
      sum +=a
  return sum
   
t = int(input())
for j in range(t):
  n = int(input())
  print(fibo(n))
