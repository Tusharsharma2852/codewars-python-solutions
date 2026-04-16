# Problem: Ones and Zeros
# Link: https://www.codewars.com/kata/578553c3a1b8d5c40300037c
# Description: Convert a binary array to its integer value
# Note: This is my approach using string conversion and base 2

def binary_array_to_number(arr):
    binary_str = ''.join(map(str, arr))
    return int(binary_str, 2)

