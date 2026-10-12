cantidad_alumnos = int(input("Ingresa la cantidad de alumnos en la lista: "))
datos_alumnos = {}
lista_materias = ["CI","CD","DL","Fis","Quim"]


def solicitar_calificaciones():
    b = 0
    materias = ["Cálculo integra", "Cálculo diferencial", "Diseño lógico", "Física", "Quimica"]
    while b < cantidad_alumnos: 
        matricula = input("Ingresa la matricula del alumno: ")
        k = 0
        if len(matricula) == 6:   
            datos_alumnos[matricula] = {}
            while k < len(lista_materias):
                calificacion = float(input(f"Del alumno {matricula}, Ingresa la calificación de {materias[k]}: "))
                
                if calificacion >= 0 and calificacion <= 10:
                    datos_alumnos[matricula][lista_materias[k]] = calificacion
                    k += 1
                
                else:
                    print("La calificación tiene que estar en el rango 0-10")
            b += 1

        else:
            print("**La matricula consta de 6 números, intentalo de nuevo**")    
    
def calcular_promedios():
    promedio = 0
    for matricula in datos_alumnos:
        for i in range(5):
            calificacion = datos_alumnos[matricula][lista_materias[i]]
            promedio += calificacion
    
    return promedio / 5


def imprimir_lista(promedio):
    print(f"Alumno\t{lista_materias[0]}\t{lista_materias[1]}\t{lista_materias[2]}\t{lista_materias[3]}\t{lista_materias[4]}\tPromedio")
    
    for matricula in datos_alumnos:
        ci = datos_alumnos[matricula][lista_materias[0]]
        cd = datos_alumnos[matricula][lista_materias[1]]
        dl = datos_alumnos[matricula][lista_materias[2]]
        fis = datos_alumnos[matricula][lista_materias[3]]
        quim = datos_alumnos[matricula][lista_materias[4]]
        
        print(f"{matricula}\t{ci}\t{cd}\t{dl}\t{fis}\t{quim}\t{promedio}")

solicitar_calificaciones()
prom = calcular_promedios()
imprimir_lista(prom)