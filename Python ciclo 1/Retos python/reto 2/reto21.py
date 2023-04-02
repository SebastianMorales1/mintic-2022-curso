medicamento1=int(input())
medicamento2=int(input())

Paciente1=0
Paciente2=0
Total=0

if medicamento1 >= 2 and medicamento2 >=3:
    while medicamento1 >= 1 and medicamento2 >=1:
        estado=input()
        glucosa=float(input())
        if estado == "ayunas":
            if glucosa < 70:
                medicamento2 = medicamento2-3
                Paciente2 = Paciente2 + 1
                Total = Total+1
            elif glucosa >= 70 and glucosa < 100:
                Total = Total+1 
            elif glucosa >= 100 and glucosa < 125:
                medicamento1 = medicamento1-2
                Paciente1 = Paciente1 + 1
                Total = Total+1 
            else:
                medicamento1 = medicamento1-4
                Paciente1 = Paciente1 + 1
                Total = Total+1 
        elif estado == 'posprandial':
            if glucosa < 140:
                Total = Total + 1
            elif glucosa >= 140 and glucosa < 200:
                medicamento1 = medicamento1-5
                Paciente1 = Paciente1 + 1
                Total = Total+1 
            else:
                medicamento1 = medicamento1-8
                Paciente1 = Paciente1 + 1
                Total = Total+1   

        else:
            Total = Total+1    

print(Total)

if Total > 0:
    print('{:} {:.2f}%'.format(Paciente1, Paciente1 / Total * 100))
    print('{:} {:.2f}%'.format(Paciente2, Paciente2 / Total * 100))
else:
    print('0 0.00%')
    print('0 0.00%')

