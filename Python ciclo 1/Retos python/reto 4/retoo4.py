med = []
medantes = []
i = 0

while True:
    n, k, m = map(int,input().split())
    if n >= 1 and k >=1:
        break
    print("Volver a ingresar")

while i < n:
    cant = int(input())

    if cant >=1:
        med.append(cant)
        medantes.append(cant)
        i+=1
    else: print("Volver a digitar")