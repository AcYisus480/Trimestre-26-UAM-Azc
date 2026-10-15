def divicion(a, b):
    try:
        r = a/b
    except ZeroDivisionError:
        print("Indeterminado")
    else:
        print(r)
    finally:
        print("Finalizando")

divicion(4, 0.02)
print("\n")
divicion(23, 0)