def is_palindrom( x ):
    rev_x, temp = 0, x
    while temp > 0 :
        rev_x = rev_x*10 + temp%10
        temp = temp // 10

    if rev_x == x:
        return 1
    return 0

def dig_count( x ):
    count = 0
    if x % 1 != 0 :
        return 0
    while x > 0:
        x = x // 10
        count += 1
    return count

def product( x ):
    temp = x
    for i in range(101,1000):
        if x % i == 0  and  dig_count( x / i ) == 3 :
            return 1
    return 0

product(1)

n = int( input() )
while 1:
    n -= 1
    if is_palindrom( n ) and product( n ) :   
       break 

print( n ) 