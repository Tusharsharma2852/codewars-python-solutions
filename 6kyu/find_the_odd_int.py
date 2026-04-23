# Problem: Find the odd int
# Link: https://www.codewars.com/kata/54da5a58ea159efa38000836
# Description: Find the integer that appears an odd number of times in the array
# Note: This is my approach using count method to identify the odd occurring element
 
def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num
