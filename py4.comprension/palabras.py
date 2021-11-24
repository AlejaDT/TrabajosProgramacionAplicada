def palabra(A):
  #A lista de palabras
  lista=[]
  lista =[word for word in A if word[-1] == 'a']
  return lista

palabras = ['Banana', 'Luis', 'Florero', 'Marta', 'Cama', 'Pablo']

pal = palabra (palabras)
print(pal)
