

from sympy import re


def climb_stairs(n):
    #n is one or two 
    if n ==1:
        return 1
    elif n==2:
        return 2
    else:
        return climb_stairs(n-1)+climb_stairs(n-2)

k = int(input("Enter the number:"))
print(climb_stairs(k))
