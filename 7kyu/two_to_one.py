#Link : https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
#disc : In this probelum we have 2 unstructured string for need to join and make it to in alphabelticaly order .
def longest(a1, a2):
    c = sorted(set(a1+a2))
    return ''.join(c)
