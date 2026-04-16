# problem : Disemvowel Trolls
# Link : https://www.codewars.com/kata/52fba66badcd10859f00097e
# Description : Remove all vowels from a string 
# Note : This is my initial approach using loop and replace method

def disemvowel(string_):
    for i in string_ :
        if i in "aieouAEIOU" :
            string_ = string_.replace(i,"")
            
    return string_
