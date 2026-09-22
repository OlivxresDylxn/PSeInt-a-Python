import os
print("bienvenido a la demostracion de cual numero es mayor")

num1= int(input("digite su primer numero\n"))
num2= int(input("digite su segundo numero\n"))

if num1>num2:
    os.system("pause")
    os.system("cls")
    print(f"el numero 1-  {num1} es mayor al 2- {num2}")


else:
    os.system("pause")
    os.system("cls")
    print(f"el numero 2- {num2} es mayor al numero 1- {num1}")