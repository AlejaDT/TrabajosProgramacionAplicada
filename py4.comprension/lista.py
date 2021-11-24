def lista(A,B):
  #Las listas A,B tiene la misma longitud

  n=len(B)//2
  C=[] #Lista vacía

  C=[(((A[i+1])**2)*B[2*i])+B[n+i] for i in range (n)]

  return C

A=[1,3,5,7,9,11]
B=[1,2,3,4,5,6]
c=lista(A,B)

print(c)

