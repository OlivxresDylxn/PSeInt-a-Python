import os
for i in range(10):

    print(" bienvenido al convertidor de millas marinas y metros")

    sele= int(input("si desea pasar de millas a metros perione 1 y si desea pasar de metros a millas presione 2\n"))
    os.system("cls")
    if sele<=0 or sele>2:
        print("digito un numero incorrecto")
        os.system("cls")
    elif sele==1:
        print("bienvenido al convertidor de millas a metros")

        millas= int(input("introduzca la cantidad de millas que le gustaria cambiar a metros\n"))

        opera= millas * 1852

        print(f"su cantidad de millas convertidas en metros es de {opera}")
        os.system("pause")
        os.system("cls")

    else:
        print("bienvenido al convertidor de metros a millas")

        metros= int(input("introduca la cantidad de metros que quiere pasar a millas\n"))

        cion= metros * 0.00054
        print(f"su cantidad de metros convertido en millas es de {cion}")
        os.system("pause")
        os.system("cls")
        