ventas_totales_anual={}
ventas_totales_tri={}
datos=open('datos.csv', 'r')#abrir y leer
_=datos.readline()
next(datos)  # Saltea la primera línea

for linea in datos.readlines():
    datos_separados = linea.split(";")
    #clasifico los datos segun su posicion, convierto a int
    año = int(datos_separados[0])
    trimestre_1 = int(datos_separados[1])
    trimestre_2 = int(datos_separados[2])
    trimestre_3 = int(datos_separados[3])
    trimestre_4 = int(datos_separados[4])

    ventas = trimestre_1 + trimestre_2 + trimestre_3 + trimestre_4

    # VENTAS ANUALES
    if año in ventas_totales_anual:
        ventas_totales_anual[año]+=ventas #si el año existe, se actualiza ventas
    else:
        ventas_totales_anual[año]=ventas #si el año no existe como una key en el diccionario, se crea uno nuevo

    # VENTAS TRIMESTRALES
    if año in ventas_totales_tri: # se actualiza el diccionario: busca el año y luego trimestre
        ventas_totales_tri[año][1]+= trimestre_1
        ventas_totales_tri[año][2]+= trimestre_2 #si el año y trimestre existen, se actualizan los datos
        ventas_totales_tri[año][3]+= trimestre_3
        ventas_totales_tri[año][4]+= trimestre_4
    else: # sino, se le asocian los valores de los trimestres al año
        ventas_totales_tri[año] = {
            1: trimestre_1,
            2: trimestre_2,
            3: trimestre_3,
            4: trimestre_4
        }

datos.close()

while True:
    print("1. Ventas totales\n2. Ventas anuales\n3. Ventas trimestrales\n4. Mostrar todo\n5. Salir")
    opcion=int(input()) #ingresa la opcion del menú

    if opcion==1: #Se suman los valores del diccionario (las ventas anuales)
        total_ventas=sum(ventas_totales_anual.values())
        print(f"Ventas totales de la empresa: {total_ventas}")

    elif opcion == 2: #si el año existe, se sacan del diccionario sus ventas 
        año=int(input("Ingrese el año que desea ver: "))
        if año in ventas_totales_anual:
            ventas_anuales=ventas_totales_anual[año]
            print(f"Ventas totales del año {año}: {ventas_anuales}")
        else:
            print("No disponible")

    elif opcion==3:
        año=int(input("Ingrese el año que desea ver: "))
        if año in ventas_totales_tri:
            ventas_trimestrales = ventas_totales_tri[año] #saca las ventas trimestrales y las asigna en otra variable
            for trimestre, ventas in ventas_trimestrales.items(): #itera trimestre y ventas, dentro de la nueva variable
                print(f"Trimestre {trimestre}: {ventas}")
        else:
            print("No disponible")

    elif opcion==4:
        print("-----------  RESUMEN GENERAL  -----------\n")
        print(f"  . Ventas totales: {total_ventas}") #variable de la opcion 1
        #suma los valores del diccionario y los divide por la cantidad de años, luego redondea a 2 decimales
        promedio_anual=round(sum(ventas_totales_anual.values()) / len(ventas_totales_anual),2)
        print(F"  . Promedio de ventas totales: {promedio_anual}")

        print("  . Ventas totales por año:\n")
        for año, ventas in ventas_totales_anual.items():#muestra las ventas de cada año del diccionario
            print(f"Año {año}: {ventas}")

        print("\n  . Ventas totales por trimestre:\n")
        for trimestre, ventas in ventas_totales_tri.items():
            print(f"Trimestres de {trimestre}: {ventas}")

    elif opcion==5:
        print("Cerrando...")
        break
