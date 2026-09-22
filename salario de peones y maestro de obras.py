import os
print(("bienvenido al area de pagos"))

sele= int(input("digite 1 si usted es maestro de obras y 2 si usted es peon\n"))
hor= int(input("introduzca la cantidad de horas que trabajo"))
if hor<0 or sele<1 or sele>2:
    print("usted ingreso datos invalidos")
elif sele==1:
    os.system("pause")
    os.system("cls")
    mob= hor* 3000
    print(f"ya que usted es maestro de obras su sueldo con las horas que trabajo es de {mob}")

elif sele==2:

    peon= hor*1500
    os.system("pause")
    os.system("cls")
    print(f"ya que usted es peon su sueldo con las horas que trabajo es de {peon} ")
