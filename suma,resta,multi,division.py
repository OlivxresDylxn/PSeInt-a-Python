import os
for i in range(10):
    print("bienvenido a la calculadora de sumas, restas, multiplicaciones y divisiones")

    options=int(input("si quiere sumar escriba 1, si quiere restar escriba 2, si quiere multiplicar escriba 3 y si quiere dividir escriba 4\n"))


    if options==1:  

        print("bienvenido a la seccion de sumar")

        num1= int(input("digite su primer numero\n"))
        num2= int(input("digite su segundo numero\n"))

        suma= num1+ num2

        print(f"la suma de sus 2 numeros es de{suma}")
        os.system("pause")
        os.system("cls")

    elif options==2:
        print("bienvenido a la seccion de restar")

        res1= int(input("digite su primer numero\n"))
        res2= int(input("digite su segundo numero\n"))

        resta= res1 - res2
        print(f"la resta de sus 2 numeros es de {resta} ")
        os.system("pause")
        os.system("cls")

    elif options==3:
        print("bienvenido a la seccion de multiplicar")

        mult1= int(input("digite su primer numero\n"))
        mult2= int(input("digite su segundo numero\n"))

        multiplicacion= mult1 * mult2
        print(f"la multiplicacion de sus 2 numeros es de{multiplicacion}")
        os.system("pause")
        os.system("cls")


    elif options==4:

        print("bienvenido a la seccion de division")

        div1= int(input("digite su primer numero\n"))
        div2= int(input("digite su segundo numero\n"))

        division= div1/div2

        print(f"la division de sus 2 numeros es de {division}")
        os.system("pause")
        os.system("cls")


    if i==3:
        break