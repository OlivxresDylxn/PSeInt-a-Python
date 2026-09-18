import os
for i in range(10):
    print("binevenido a la seleccion de 3 programas")
   
    options= int(input("digite 1 si desea entrar al programa de area y perimetro, 2 si desea entrar al programa de millas y 3 si desea entrar al programa de salarios\n"))
    os.system("cls")

    if options==1:

        print(" bienvenido a la calculadora de area y perimetro")

        esco=int(input("Si desea sacar el perimetro escriba 1 y si quiere sacar area escriba 2 \n"))
        if esco <=0 or esco>2:

            print("usted digito un numero incorrecto")
        elif esco == 1:

            peri1= int(input("escriba su primer radio"))
            peri2= int(input("escriba su segundo radio"))

            perimetro= 3.14 * peri1 * peri2

            print(f"su perimetro es de {perimetro}")
            os.system("pause")
            os.system("cls")
        elif  esco==2:

            peri3= int(input("digite su perimetro"))

            area= 2* 3.14 * peri3

            print(f"su area es de {area}")
            os.system("pause")
            os.system("cls")

    if options==2:

        print(" bienvenido al convertidor de millas marinas y metros")
        
        esco= int(input("si desea pasar de millas a metros perione 1 y si desea pasar de metros a millas presione 2\n"))
        if esco<=0 or esco>2:
                print("digito un numero incorrecto")
                os.system("cls")
        elif esco==1:
                print("bienvenido al convertidor de millas a metros")
        
                millas= int(input("introduzca la cantidad de millas que le gustaria cambiar a metros\n"))
        
                opera= millas * 1852
        
                print(f"su cantidad de millas convertidas en metros es de {opera}")
                os.system("pause")
                os.system("cls")
        
        elif esco==2:
                print("bienvenido al convertidor de metros a millas")
        
                metros= int(input("introduca la cantidad de metros que quiere pasar a millas\n"))
        
                cion= metros * 0.00054
                print(f"su cantidad de metros convertido en millas es de {cion}")
                os.system("pause")
                os.system("cls")

    if options==3:
        print("bienvenido al programa de horas")
        persal= 5000
        salext=1500
        horas=int(input("cuantas horas trabajo?\n"))

        if horas<40:

            pago= horas * persal
            print(f"su pago sin horas extra es de {pago}")
            os.system("pause")
            os.system("cls")


        else:

            ext= int(input("cuantas horas extra trabajo\n"))


            fin=salext*horas
            os.system("pause")
            os.system("cls")
            print(f"el total con extras es de {fin}")
            os.system("pause")
            os.system("cls")
    


    