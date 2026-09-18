print(" bienvenido a la calculadora de area y perimetro")

sele=int(input("Si desea sacar el perimetro escriba 1 y si quiere sacar area escriba 2 \n"))
if sele <=0 or sele>2:

    print("usted digito un numero incorrecto")
elif sele == 1:

        peri1= int(input("escriba su primer radio"))
        peri2= int(input("escriba su segundo radio"))

        perimetro= 3.14 * peri1 * peri2

        print(f"su perimetro es de {perimetro}")

else:

        peri3= int(input("digite su perimetro"))

        area= 2* 3.14 * peri3

        print(f"su area es de {area}")
