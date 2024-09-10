def Menu_tarifas_costo():
    print("Seleccione una operacion")
    print("1. Estados Unidos")
    print("2. Canada")
    print("3. Europa")
    print("4. Resto del mundo")
    print("5. Finalizar opciones")
while True:
    Menu_tarifas_costo()
    opcion = input("Ingrese el número correspondiente a la operación deseada: ")
    Duramin = float(input("Ingrese los minutos de la llamada: "))
    if opcion =='1':
        if Duramin  <= 14.59:
            Costfin = Duramin * 900
            print(f"El costo de la llamada es de: {Costfin}")
        if Duramin >= 15:
            Costfin = Duramin * 900
            Desc = Costfin * 0.20
            Costdes = (Duramin * 900) - Desc
            print(f"El costo de la llamada con el 20% es de: {Costdes}")
    elif opcion =='2':
        if Duramin  <= 14.59:
            Costfin = Duramin * 800
            print(f"El costo de la llamada es de: {Costfin}")
        if Duramin >= 15:
            Costfin = Duramin * 800
            Desc = Costfin * 0.20
            Costdes = (Duramin * 800) - Desc
            print(f"El costo de la llamada con el 20% es de: {Costdes}")
    elif opcion =='3':
        if Duramin  <= 14.59:
            Costfin = Duramin * 950
            print(f"El costo de la llamada es de: {Costfin}")
        if Duramin >= 15:
            Costfin = Duramin * 950
            Desc = Costfin * 0.20
            Costdes = (Duramin * 950) - Desc
            print(f"El costo de la llamada con el 20% es de: {Costdes}")
    elif opcion =='4':
        if Duramin  <= 14.59:
            Costfin = Duramin * 1250
            print(f"El costo de la llamada es de: {Costfin}")
        if Duramin >= 15:
            Costfin = Duramin * 1250
            Desc = Costfin * 0.20
            Costdes = (Duramin * 1250) - Desc
            print(f"El costo de la llamada con el 20% es de: {Costdes}")
    elif opcion =='5':
        print("Finaliza el progama")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")