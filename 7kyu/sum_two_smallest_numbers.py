# Problem: Sum of two lowest positive integers
# Link: https://www.codewars.com/kata/558fc85d8fd1938afb000014
# Description: Find the sum of the two smallest positive numbers in a list
# Note: This is my initial approach using sorting

def sum_two_smallest_numbers(numbers):
        numbers.sort()
        n = numbers[0]+numbers[1]
        return n
