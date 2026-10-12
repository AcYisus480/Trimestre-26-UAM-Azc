codigos_paises = {
    "0": "EE.UU.",
    "380": "Bulgaria",
    "50": "Inglaterra",
    "539": "Irlanda",
    "560": "Portugal",
    "70": "Noruega",
    "759": "Venezuela",
    "850": "Cuba",
    "890": "India"
    }
codigo = input("Ingresa el código de barras: ")
lista=[]

def verificar_integridad(codigo, lista):    
    if len(codigo) < 8:
        codigo = codigo.zfill(8)
        
    elif 9 <= len(codigo) <= 12:
        codigo = codigo.zfill(13)
        
    elif len(codigo)!=8 and len(codigo)!=13:
        return "Error, intenta de nuevo", None
    
    for num in codigo:
        lista.append(int(num))
    
    tam =len(codigo)-1
    resultado = 0
    
    a, b = (0, 1) if len(codigo) == 8 else (1, 0)
    
    for i in reversed(range(len(lista)-1)):
        if i % 2 == a and i != tam:
            resultado += (lista[i] * 3)

        elif i % 2 == b and i != tam:
            resultado += lista[i]
    
    resultado += lista[-1]
    
    if resultado % 10 == 0:
        return "El código de barras es valido", a
    return "El código de barras NO es valido", -1
    

def identificar_pais(codigo, codigos_paises):
    pais_id = ''
    for i in range(3):
        pais_id += codigo[i]
        if pais_id in codigos_paises:
            return "pais " + codigos_paises[pais_id]
    else:
        return 'pais no identificado'

mensaje, tipo =verificar_integridad(codigo, lista)

if tipo == 1:
    mensaje_pais = identificar_pais(codigo, codigos_paises)
    print(f"{mensaje} y el {mensaje_pais}")
else:
    print(f"{mensaje}")