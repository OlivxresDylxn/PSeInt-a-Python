import os
print("bienvenido a la calculadora")
suma=0
for i in range (1, 11):
    

    numeros= int(input(f"digite su numero por {i} vez\n"))


    suma= suma + numeros
os.system("pause")
os.system("cls")
print(f" la suma de todos sus numeros es {suma}")
