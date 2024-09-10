calificacion1 = float(input("Ingrese la primera calificación:"))
calificacion2 = float(input("Ingrese la segunda calificación:"))
calificacion3 = float(input("Ingrese la tercera calificación:"))
calificacion4 = float(input("Ingrese la cuarta calificación:"))
Pago = float(input("Ingrese el valor de su matricula:"))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4
print("Tu promedio es de:",promedio)
Excelente = 20
Bien = 100
Deficiente = 100

if promedio >=4:
    print("Excelente obtienes descuento del",Excelente)
elif promedio >=3 and 3.99:
    print("Bien cancela el",Bien)
elif promedio >=0 and 2.99:
    print("Deficiente cancela el",Deficiente)
else:
    print("Error dato errado")

if promedio >=4:
    Desc = Pago * 0.20
    Totalmat = Pago - Desc
    print("Tu matricula queda en:",Totalmat)
else:
    print("No tiene Beneficio")