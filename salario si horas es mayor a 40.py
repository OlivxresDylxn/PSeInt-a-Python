import os
print("bienvenido al area de pagos")
sala=5000
extras=1500

horas= int(input("introduzca cuantas horas trabajo\n"))

if horas<0:
    print("horas invalidas")


elif horas>40:
    ext= int(input("cuantas horas extra trabajo\n"))

    suma= ext * extras
    sal= horas*sala
    fin= sal+suma
    os.system("pause")
    os.system(("cls"))
    print(f"su salario total con horas extra es de {fin}")

elif horas<40:
    sal= horas*sala
    os.system("pause")
    os.system(("cls"))
    print(f"su salario ya que no tiene horas extra es de {sal}")