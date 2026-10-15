archivo = open("texto.txt", "r+")

archivo.seek(0)
lineas = archivo.readline(10)
print(lineas)

archivo.seek(0)
lineas_2 = archivo.readline()
print(lineas_2)

archivo.seek(2)
archivo.write("\n---- Sopor Aeternus <3 ----\n")

texto = ["\n", "Sopor is good", "\n"]
archivo.writelines(texto)

archivo.close
