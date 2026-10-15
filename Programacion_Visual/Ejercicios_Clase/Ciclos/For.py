# imprimiendo elementos de una lista
print("--------------------------------------------------")
array = ["Hola","xd","Que","Paso","?"]
for palabra in array:
    print(palabra)

print("--------------------------------------------------")
dic = {"o":11111,"l":22222,"a":33333,"xd":44444,"d":55555}

for palabra in dic:
    print (palabra)
    print (dic[palabra])

print("--------------------------------------------------")
for key, value in dic.items():
    print("llave:  " + key + "   Valor:  " + str(value))

print("--------------------------------------------------")
set1 = {1,"hola",2,"asa"}
for caracteres in set1:
    print(caracteres)

print("--------------------------------------------------")
lista = [1,2,3,4,5,6]
for i in range(len(lista)):
    print(lista[i])

print("--------------------------------------------------")
lista = [1,2,3,4,5,6]

for i in range(len(lista)):
    print(lista[i])
else:
    print("Terminar ciclo")

print("--------------------------------------------------")

for i in range(len(lista)):
    print(lista[i])
    
    if i == 3:
        break
else:
    print("Terminar ciclo")

print("--------------------------------------------------")

i = 0
while i < 6:
    print(i)
    i=i+1
    