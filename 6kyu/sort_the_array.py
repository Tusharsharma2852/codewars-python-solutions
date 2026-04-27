# Problem : sort the odd
# Link : https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
# Description : Given an array of numbers, we need to sort only the odd numbers, while keeping even numbers in their original positions.

def sort_array(source_array):
    odd= sorted([x for x in source_array if x % 2])
    i = 0 
    for j in range(len(source_array)):
        if source_array[j] % 2:
            source_array[j] = odd[i]
            
            i+=1
    return source_array
