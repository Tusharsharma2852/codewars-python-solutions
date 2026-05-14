# In this code we find the pell number :
# In this code is mainly difficult part its calculation but once you understand the login then its become simple for us 
# The logic of pell numbers is P(n) = 2 * P(n-1) + P(n-2) the answer should we except is : 0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, 80782, 195025, 470832, ..
# Link : https://www.codewars.com/kata/5818d00a559ff57a2f000082/train/python
def pell(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, 2*b + a
    return a
    
