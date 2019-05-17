#!/bin/python3
import sys

def sum_of_squares(x):
    return int(round(x**3/3 + x**2/2 + x/6))

def square_of_sum( x ):
    return int( (x*(x+1)//2)**2 )

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(square_of_sum( n )-sum_of_squares(n))