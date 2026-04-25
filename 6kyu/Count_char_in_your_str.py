# Problem: Count characters in your string
# Link: https://www.codewars.com/kata/52efefcbcdf57161d4000091
# Description: Count the number of occurrences of each character in a string
# Note: This is my approach using dictionary to store frequency of each character
 
def count(s):
    result = {}
    
    for ch in s:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    
    return result
