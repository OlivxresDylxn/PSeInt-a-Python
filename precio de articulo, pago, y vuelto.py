import os
print("bienvenido al cajero")

precio= int(input("digite el precio del articulo\n"))
pago= int(input("digite la cantidad con la que va a pagar\n"))

if precio<0 or pago<0:
    print("dinero o precio invalido")



elif pago> precio:
    os.system("pause")
    os.system(("cls"))
    vuelto= pago - precio
    imp=vuelto*0.15
    print(f"el precio inicial de su factura es de {vuelto}")
    print(f"el total de su factura con el 15% de impusto es de {imp}")


elif precio> pago:
    print("falta dinero")

