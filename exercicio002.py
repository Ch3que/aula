tupla=0
contador=0
a=0
b=0 

while contador !=6:
    tupla=int(input("digite 6 numeros"))
    contador +=1
    a=a + tuple([tupla])
print(a)
indice=int(input("digite outro"))
b=b + tuple ([a[indice:]])
print(b)