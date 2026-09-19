import os

print("bienvenido a la calculadora de centimetros a pulgadas")

opt= int(input("si quiere pasar de centimetros a pulgadas digite 1 y si quiere pasar de pulgadas a centimetros digite 2\n"))

os.system("cls")
if opt==1: 

    cent= int(input("introduzca la cantidad de centimetros que quiere pasar a pulgadas\n"))

    opera= cent/2.54

    print(f"la cantidad de centimetros introducidos en pulgadas es de{opera}")


else:
    pulg= int(input("introduzca la cantidad de pulgadas que quiere pasar a centimetros\n"))

    operac=pulg *30.48

    print(f"la cantidad de pulgadas pasadas a centimetros es de {operac}")