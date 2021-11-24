def sumatoria_1(A,B,C):
  n = len(A)
  s= sum((A[i]*B[i])+C[i] for i in range (n))+(n**2)
  return s

A=[1,2,3]
B=[4,5,6]
C=[7,8,9]
x = sumatoria_1(A,B,C)

print(x)