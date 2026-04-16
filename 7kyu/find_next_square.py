# Problem: Find the next perfect square
# Link: (paste your Codewars link here)
# Description: Find the next perfect square after a given number, or return -1 if not a perfect square
# Note: This is my approach using square root check

from math import sqrt
def find_next_square(sq):
    root = int(sqrt(sq))
    return(root + 1)**2 if root*root == sq else -1
