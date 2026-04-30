# Problem : Sum String as Numbers
# link : https://www.codewars.com/kata/5324945e2ece5e1f32000370/train/python
# Description : Given two numbers in string format, return thrir sum as a string. We cannot convert the entire string into integers because inputs can be extremely large ( million digits).
def sum_strings(x, y):
#     c = int(x) + int(y)
#     d = str(c)
#     return (f'{d}')
    carry = 0
    result =[]
    for a, b in zip_longest(x[::-1], y[::-1], fillvalue= '0'):
        total= int(a) + int(b) + carry
        result.append(str(total % 10))
        carry = total // 10
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1]).lstrip('0') or '0'
