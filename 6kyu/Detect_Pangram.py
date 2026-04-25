# Problem: Detect Pangram
# Link: https://www.codewars.com/kata/545cedaa9943f7fe7b000048
# Description: Check if a given string contains every letter of the alphabet at least once
# Note: This is my approach using set of alphabets and checking each character in the string
 
def is_pangram(st):
    st = st.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    for ch in alphabet:
        if ch not in st:
            return False
    
    return True
