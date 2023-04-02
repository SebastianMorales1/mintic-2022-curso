#num1 = 6
#print(num1)

edad = int(input("Coloca edad: "))

if edad< 18:
    print("No puede votar")
elif 18 < edad:
    print("Puede votar")
else:
    print("Primera vez que vota")