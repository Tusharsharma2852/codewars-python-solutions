# Problem: Find the unique number
# Link: https: https://www.codewars.com/kata/585d7d5adb20cf33cb000235
# Description: Find the unique number in an array where all elements are equal except one
# Note: This is my approach using sorting to identify the unique element
def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]
