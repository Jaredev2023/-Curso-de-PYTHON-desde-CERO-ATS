edad = int(input("digite su edad: "))
if edad>0 and edad<100:
    print("edad correcta")
    if edad>=18:
        print("es mayor de edad")
else:
    print("edad incorrecta")
    # if 0<edad<100: