import os
print("bienvenido al programa de bonos y ventas")
ventm= int(input("digite aqui sus ventas mensuales"))

por= int(input(" si desea ver el procedimiento del porcentaje 1/si 2/no\n"))

if por==1:

    porcen=ventm*0.23
    os.system("pause")
    os.system("cls")

    print("se multiplican sus ventas mensuales por el bono que es de 0.23% en la multiplicacion es 0.23%")
    print(f"en su caso es {porcen}")
    print("luego se suman las ventas mensuales + el bono")
    bonovent= ventm + porcen
    print(f"su venta mas el bono es de {bonovent}")

else:
    print("adios")