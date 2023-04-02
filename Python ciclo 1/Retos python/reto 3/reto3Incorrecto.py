med = []
medantes = []
i = 0

while True:
    n, m = map(int,input().split())
    
    if n >= 1:
        break
    print("Volver a ingresar")

while i < n:
    cant = int(input())

    if cant >=1:
        med.append(cant)
        medantes.append(cant)
        i+=1
    else: print("Volver a digitar")

for i in range(m):
    #suc, paciente, x = map(input().split())
    suc = int(input())
    paciente = input()
    x = float(input())
    if suc>=1 and suc <= n:
        if paciente =='ayunas':
            if x < 70:
                med[suc-1]-= 3
            elif (70<=x<100):
                med[suc-1]-= 0
            elif (100<=x < 125):
                med[suc-1]-= 2
            else: 
                med[suc-1]-= 4
        elif paciente =='posprandial':
            if x<140:
                med[suc-1]-= 0
            elif (140 <= x < 200):
                med[suc-1]-= 5
            else:
                med[suc-1]-= 8
#        else: med[suc-1]-= 0

b = min(med)
pb= med.index(b)
c = max(med)
pc= med.index(c)

print(pb+1, b)
print(pc+1, c)

for i in range(n):
    prom = (1- med[i]/medantes[i])*100
    print(f'{i+1} {prom:.2f}%')
