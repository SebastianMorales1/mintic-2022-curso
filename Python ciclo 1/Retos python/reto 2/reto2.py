# Estos son las entradas
med1 = int(input())
med2 = int(input())

# Estos son cosas del bucle
atentidos1 = 0
atentidos2 = 0
pacientes = 0

if (med1>=2) and (med2>=3): 

# ¿Hay suficientes medicamentos o ya se acabaron?
# Hay suficientes, sigue el proximo paciente (continua el bucle)
# No hay suficientes, se termino el bucle
    while (med1 >= 1) and (med2 >= 1): 
        paciente = input()
        x = float(input()) 
        if paciente =='ayunas':
            if x < 70:
                med2 = med2-3
                atentidos2 += 1
                pacientes += 1 
            elif (70<=x<100):
                pacientes += 1
            elif (100<=x < 125):
                med1 = med1 - 2
                atentidos1 += 1
                pacientes += 1 
            else: 
                med1 = med1 - 4
                atentidos1 += 1
                pacientes += 1 
        elif paciente =='posprandial':
            if x<140:
                pacientes += 1
            elif (140 <= x < 200):
                med1 = med1 - 5
                atentidos1 += 1
                pacientes += 1 
            else:
                med1 = med1 - 8
                atentidos1 += 1
                pacientes += 1 
        else:
            pacientes += 1 

print(pacientes)

if pacientes > 0:
    print('{:} {:.2f}%'.format(atentidos1,atentidos1 / pacientes * 100))
    print('{:} {:.2f}%'.format(atentidos2,atentidos2 / pacientes * 100))
else:
    print('0 0.00%')
    print('0 0.00%')