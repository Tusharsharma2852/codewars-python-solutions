# Problem: You're a square!
# Link: https://www.codewars.com/kata/54c27a33fb7da0db0100040e
# Description: Check if a number is a perfect square
# Note: This is my initial approach using math.isqrt

from math import isqrt
def is_square(n):
    if n<0 :
        return False
    elif isqrt(n) ** 2 == n :
        return True
    else :
        return False
