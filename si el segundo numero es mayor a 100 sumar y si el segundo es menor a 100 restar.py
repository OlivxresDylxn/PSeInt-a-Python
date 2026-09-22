import os
print("bienvenido")

num1= int(input("digite su primer numero\n"))
num2= int(input("digite su segundo numero\n"))

if num1<0 or num2<0:
    print("numeros invalidos")

elif num2>100:
    suma= num1+ num2
    os.system("pause")
    os.system("cls")
    print(f"la suma de sus numeros es de {suma}")

elif num2<100:

    resta= num1-num2
    os.system("pause")
    os.system("cls")
    print(f"la resta de sus 2 numeros es de {resta}")

