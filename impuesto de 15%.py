precio= int(input("digite el precio del producto\n"))

if precio<0:
    print("su precio es invalido")

else:

    imp=precio*0.15
    fin=imp+precio
    print(f"su precio final es de {fin}")
    print(f"y su impuesto es de {imp}")