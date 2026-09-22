import os
print("bienvenido")

ini= int(input("digite el precio de su producto\n"))
if ini<0:
    print("precio invalido")
elif ini>20000:
    os.system("pause")
    os.system("cls")
    desc=ini*0.35
    fin= ini-desc
    print(f"ya que su precio es mayor a 20000 entonces se aplica un descuento de 35% entonces su precio final seria de {fin}")


elif ini<20000:
    os.system("pause")
    os.system("cls")
    print(f"ya que su precio no supera los 20000 entonces no se aplica el descuento entonces su precio sigue siendo de {ini}")