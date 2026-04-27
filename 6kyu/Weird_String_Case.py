# Problem: Weird String Case
# Link: https://www.codewars.com/kata/52b757663a95b11b3d00062d
# Description: Given a string, convert it so that in each word : 
# Characters at even index are uppercase
# Characters at odd index are lowercase
def to_weird_case(words):
    result = []
    
    for word in words.split():
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        result.append(new_word)
    return " ".join(result)
