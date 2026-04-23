# Problem: RGB To Hex Conversion
# Link: https://www.codewars.com/kata/513e08acc600c94f01000001
# Description: Convert RGB decimal values (0–255) into a hexadecimal color code
# Note: This is my approach using manual conversion (division by 16 and ASCII mapping for A–F)
 
def rgb(r, g, b):
    res = ''
    
    for x in (r, g, b):
        if x <= 0:
            x = 0
        if x > 255:
            x = 255
        
        q = x // 16
        r = x % 16
        
        if q >= 10:
            q = chr(q - 10 + ord('A'))
        if r >= 10:
            r = chr(r - 10 + ord('A'))
        
        res += str(q) + str(r)
    
    return res
