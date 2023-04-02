# Actividad 1

print('Actividad 1')

luz = input('Ingresar luz de semaforo (verde, naranja o rojo): ')
#luz = luz.lower()
peaton = input('¿Hay peaton? (si/no): ')

if peaton == 'si':
    HayPeaton == True
else:
    HayPeaton == False

if luz == 'verde':
    print('Siga')
elif luz == 'amarillo':
    if peaton == 'si':
        print('Pare')
    else:
        print('Precaucion')    
elif luz == 'rojo':
    print('pare')
else:
    print('error')