import os
print("bienvenido a la pesa")

peso= int(input("indique su peso en libras por favor\n"))

print("su peso en libras sera medido en kilos")
os.system("pause")
os.system("cls")
pasar= peso/2.205
if pasar>120:
    print(f"tu peso es de {pasar} tienes que cuidar mas tu salud")
