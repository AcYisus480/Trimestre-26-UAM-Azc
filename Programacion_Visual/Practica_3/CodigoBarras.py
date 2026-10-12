codigo = input("Ingresa el código de barras: ")
lista=[]

def codigo_a_lista():
    for num in codigo:
        lista.append(int(num))
    
    
def verificar_integridad():
    resultado = 0
    tam = len(lista)
    for i in reversed(range(tam)):
        if i % 2 == 1 or i == 0 and i != tam:
            resultado += lista[i] * 3
        if i % 2 == 0 and i != tam:
            resultado += lista[i]
        
    resultado += lista[-1]
    return resultado
    

def identificar_pais():
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
    pais_id = ''
    for i in range(3):
        pais_id += str(lista[i])
        if pais_id in codigos_paises:
            return codigos_paises[pais_id]
    
    else:
        return 'Pais no identificado'
    
    
    
codigo_a_lista()
verificar_integridad()
print(identificar_pais())