total=float(input("ingresar total de la compra"))
descuento=float(input("ingrese el descuento"))
descuento2=descuento/100
precio_descuento=total*descuento2
precio_final=total-precio_descuento
print(f"el precio total de la compra es ${precio_final:.2f}")