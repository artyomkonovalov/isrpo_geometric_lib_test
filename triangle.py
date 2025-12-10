def area(a, h):
#    return area of triangle
#       parameters:
#            (int) a: triangle side
#            (int) h: triangle height
#        output value:
#            (int) area of triangle
    if(a < 0 or h < 0): return False
    return a * h / 2

def perimeter(a, b, c):
#   return perimeter of triangle by 3 sides
    if(a < 0 or b < 0 or c < 0): return False
    if(2*max(a,b,c) > a + b + c): return False
    return a + b + c
