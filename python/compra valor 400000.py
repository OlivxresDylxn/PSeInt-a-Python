import os
print("bienvenido al super")

precio= int(input("indique el valor de su compra\n"))

if precio>400000:
    nombre=input("introduzca su nombre\n")
    edad= input("introduzca su edad\n")
    os.system("pause")
    os.system("cls")

    print(f"hola {nombre} su pedido valorado en {precio} ha sido aceptado")
    print("gracias por su compra")

else:
    os.system("cls")
    print("determinamos que usted no es solvente")
    print("pedido rechazado")