t = int(input())
for i in range (t):
    n = int(input())
    sum = 0
  
    sum += 3 * ((n-1) // 3)*((n-1) // 3 + 1) // 2

    sum += 5 * ((n-1) // 5)*((n-1) // 5 + 1) // 2

    sum -= 15 * ((n-1) // 15)*((n-1) // 15 + 1) // 2

    print(sum)
