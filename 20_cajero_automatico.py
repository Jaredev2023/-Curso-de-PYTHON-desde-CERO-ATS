opcion= input("1.ingresar dinero\n2.retirar dinero\n3.mostrar dinero disponible\n4.salir")
dinero= 1000

if opcion=="1":
    ingreso= int(input("caunto dinero desea ingresar"))
    dinero+= ingreso
    print(f"{dinero}$")
elif opcion=="2":
     retiro= int(input("caunto dinero desea ingresar"))
     dinero-= retiro
     print(f"{dinero}$")
elif opcion=="3":
    print(f"{dinero}$")
elif opcion=="4":
    print("cerrando sesion")

#ATS SOLUCION: if retirar>saldo: print("no tiene esa cantidad de dinero")
#ATS SOLUCION: else: print("se equivoco de opcion")