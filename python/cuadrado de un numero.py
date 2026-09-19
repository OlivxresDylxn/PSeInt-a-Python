import os
print("bienvenido como sacar el cuadrado a un numero")

num= int(input("indique el numero al que le desea sacar el cuadrado\n"))

operacion= num * num
os.system("pause")
os.system("cls")
print(f"el cuadrado del numero {num} es {operacion}")