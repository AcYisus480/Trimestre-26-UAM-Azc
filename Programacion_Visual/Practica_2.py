cadena = input("Cadena >> ") 
numeros = ['0','1','2','3','4','5','6','7','8','9']

numeros_encontrados = []
numero = ""

for j in cadena:
    if j in numeros:
        numero += j 
    elif j == " ":
        if numero !="":
            numeros_encontrados.append(int(numero)) 
            numero = "" 

if numero != "":
    numeros_encontrados.append(int(numero))

num_max = -100
for i in numeros_encontrados:
    if num_max < i:
        num_max = i
        

num_min = 1000
for i in numeros_encontrados:
    if num_min > i:
        num_min = i
        

num_par = 0
for i in numeros_encontrados:
    if i % 2 == 0:
        num_par += 1
        

print(cadena + " >>  " + str(num_max)+ " " + str(num_min) + " " +str(len(numeros_encontrados))+ " "+ str(num_par))