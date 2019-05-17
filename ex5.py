import math  

def nok( x , y ):
    rang, i = x, 2
    if rang > y:
        rang = y
     
    while i <= rang :
        if x % i == 0 and y % i == 0:
            x /= i
            y /= i
            i -= 1
        i += 1    
    return x

t = int(input())
for a0 in range(t):
    multiple=1
    n = int(input())
    for i in range (1,n+1):
        if multiple % i != 0:
            multiple *= int(nok(i,multiple))       
    print(multiple)