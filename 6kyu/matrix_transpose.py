# Discription : in this code i have to transpose the matrix according to the requirment lets suppose we have 3*2 matrix so we have to tranpose that onto 2*3 :
# Link : https://www.codewars.com/kata/52fba2a9adcd10b34300094c/train/python
def transpose(Matrix):
  return [list(row) for row in zip(*matrix)]
  
