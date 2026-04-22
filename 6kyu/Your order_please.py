# Problem: Your order, please
# Link: https://www.codewars.com/kata/55c45be3b2079eccff00010f
# Description: Rearrange words in a sentence based on the number present in each word
# Note: This is my approach using digit extraction and placing words at correct positions
 
def order(sentence):
    sentence_list = sentence.split()
    result = [""] * len(sentence_list)
 
    for word in sentence_list:
        for ch in word:
            if ch.isdigit():
                position = int(ch)
                result[position - 1] = word
 
    return " ".join(result)
