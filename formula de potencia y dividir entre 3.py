print("bienvemido a la calculadora")

num1= int(input("digite su primer numero\n"))
num2= int(input("digite su segundo numero\n"))
if num1<0 or num2<0:
    print(("numeros invalidos"))


formula= (num1+num2)**2/3

print(f"sus numeros {num1} {num2} con la formula dan {formula}")