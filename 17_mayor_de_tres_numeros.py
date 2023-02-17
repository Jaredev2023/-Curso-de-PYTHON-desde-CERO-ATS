n1 = int(input("digite un numero"))
n2 = int(input("digite un numero"))
n3 = int(input("digite un numero"))

if n2<n1>n3:
    print(f"{n1} es el mayor")
elif n1<n2>n3:
    print(f"{n2} es el mayor")
elif n1<n3>n2:
    print(f"{n3} es el mayor")
elif n1==n2>n3:
    print(f"{n1} y {n2} son mayores")
elif n1<n2==n3:
    print(f"{n2} y {n3} son mayores")
elif n1==n3>n2:
    print(f"{n1} y {n3} son mayores")
else:
    print("son iguales")