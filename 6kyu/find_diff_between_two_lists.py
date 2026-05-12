#Description : In this cpde i have two given list so my work is remove that element which is common in both list
# Link : https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
def diff(a,b):
  c = a+b
  for i in c:
    if i in a and i in b:
      a.remove(i)
  print(a)

diff([1, 2, 2, 2, 3],[2])
