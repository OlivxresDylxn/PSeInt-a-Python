import os
print("bienvenido al identificador de numeros pares e impares")

numero=int(input("digame su numero para saver si es par o impar\n"))

if numero %2 == 0:
    os.system("pause")
    os.system("cls")
    print(f"el numero {numero} si es par")

else:
    os.system("pause")
    os.system("cls")
    print(f"el numero {numero} es impar")