import os
print("bienvenido al calculo del doble de numeros negativos")

nega= int(input("introduzca su numero\n"))

if nega>0:
    print("ese numero es positivo, es inavalido")

else:
    os.system("pause")
    os.system("cls")
    doble= abs(nega*2)
    print(f" el resultado del doble del numero negativo y convertido en positivo es {doble}")