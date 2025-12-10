import math


def area(r):
    #return area of circle
    if(r < 0): return False
    return math.pi * r * r


def perimeter(r):
    #return perimeter of circle
    if(r < 0): return False
    return 2 * math.pi * r

