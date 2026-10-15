from Cuadrado import Cuadrado as c
from Rectangulo import Rectangulo as r
from Figura import Figura as f
print("-----------------------------")
rec = r("rojo",5.05,45.15)
print(rec.calcular_area())
print(rec)

rec.color = "Amarillo"

print(rec)
print(rec.color)
print("-----------------------------")
cua = c("AmaAzul", 5)
print(cua.calcular_area())
print(cua)