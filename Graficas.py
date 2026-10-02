# imports
import numpy as np
import matplotlib.pyplot as plt
import math


#def graficar_sen(datos):
b = 1
if b == 1:
  a = 1
  f = 1
  t = 1
  fase = 1
elif b == 2:
  f= 1
else:
  t=1
angulo = 0

x = a(np.sin(2*(math.pi)*(f)*(t)+(fase)))
y = np.sin(x)

plt.plot(x, y)

plt.title("Función cuadrática")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

plt.grid(True)
plt.show()


# Registro de la cadena de números

def registrar_datos():
  while(1):
    datos = input("Ingresa la lista de números (1's y 0's) no mayor a 10 digitos: ")
    if len(datos) > 0 and len(datos) < 11:
      if datos and all('0' <= c <= '1' for c in datos):
        return datos
      else:
        print("****Vuelve a intertalo****\n")
    else:
        print("****Vuelve a intentarlo****\n")