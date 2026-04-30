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
