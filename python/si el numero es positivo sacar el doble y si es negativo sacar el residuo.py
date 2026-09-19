import os
print("bienvenido al calculador de numeros positivos y negativos")

num= int(input("introduzca su numero\n"))

if num>0:

    doble= num **2
    print(f"el doble de ese numero positivo es {doble}")
else:
    residuo= num % 2
    esresiduocero= residuo==0
    print(f"el resultado de dicidir {num} entre 2 es {residuo}")

    print(f"el residuo es cero?, {esresiduocero}")
