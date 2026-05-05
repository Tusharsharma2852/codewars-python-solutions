#Link : https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
#In this program i have to find a samllest and largest number for the given , challenging part is given numbers is as string.
def high_and_low(numbers):
    k = list(map(int, numbers.split()))
    max1= max(k)
    min1= min(k)
    return f"{max1} {min1}"
