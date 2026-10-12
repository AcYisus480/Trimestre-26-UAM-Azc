import random

listaInmuebles=[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
                {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
                {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
                {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
                {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]   

def calcular_precios():
    for diccionario_inmueble in listaInmuebles:
        antiguedad = 2026 - diccionario_inmueble['año']
        precio_m = diccionario_inmueble['metros'] * 1000 
        precio_h = diccionario_inmueble['habitaciones'] * 5000
        precio_g = diccionario_inmueble["garaje"] * 15000 
        precio_a = 1 - (antiguedad / 100)
        
        if diccionario_inmueble['zona'] == 'B':
            precio = ((precio_m + precio_h + precio_g) * precio_a)*1.5
            
        else:
            precio = (precio_m + precio_h + precio_g) * precio_a
        
        n = random.randint(0, 999)
        codigo = f"{n:03d}"
        id_inmueble = diccionario_inmueble['zona'] + str(codigo)
        
        diccionario_inmueble['id'] = id_inmueble
        diccionario_inmueble['precio'] = precio

def busqueda_inmueble():
    calcular_precios()
    precio = float(input("Ingresa tu presupuesto: "))
    print("Id Inmueble\taño\tMetros\tHabitaciones\tGaraje\tPrecio")
    for inmuebles in listaInmuebles:
        if precio >= inmuebles['precio']:
            id_in = inmuebles['id']
            anio = inmuebles['año']
            mts = inmuebles['metros']
            hab = inmuebles['habitaciones']
            gar = inmuebles['garaje']
            pre = inmuebles['precio']
            
            print(f"{id_in}\t\t{anio}\t{mts}\t{hab}\t\t{gar}\t{str(pre)}")


busqueda_inmueble()