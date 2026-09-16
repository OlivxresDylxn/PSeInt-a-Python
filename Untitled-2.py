import os
persal= 5000
salext=1500
horas=int(input("cuantas horas trabajo?\n"))

if horas<40:

    pago= horas * persal
    print(f"su pago sin horas extra es de {pago}")


else:

    ext= int(input("cuantas horas extra trabajo\n"))


    fin=salext*horas
    os.system("pause")
    os.system("cls")
    print(f"el total con extras es de {fin}")