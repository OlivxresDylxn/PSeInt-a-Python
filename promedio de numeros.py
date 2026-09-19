numeros=[]
suma=0
producto=1
for i in range(1,9):

    num= int(input(f"indique su numero por {i}: vez\n"))
    numeros.append(num)
    print(numeros)
    suma= num + num
    producto= num * num
  
for num in numeros:
    os.system("pause")
    os.system("cls")
    if num>0:
        print(f" {num} numero positivo")
    elif num<0:
        print(f" {num} numero negativo")

    else:
        print(f" {num} numer igual a 0")
       

    promedio=suma/8
    if promedio>0:
       

        print(f" el promedio es de {promedio}")

    else:
        print(f"el promedio es negativo entonces la multiplicacion es de {producto}")

