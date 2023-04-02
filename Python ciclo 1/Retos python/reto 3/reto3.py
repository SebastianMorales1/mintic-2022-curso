0list_sucursal =[]
list_pacientes=[]
list_medicina=[]
list_original=[]
sucursal=0
i = 0

print("Cantidad sucursal y paciente :")
while sucursal < 1:
      sucursal,paciente = map(int,input().split())
      if sucursal <1:
       print("dato no valido, ingresar nuevamente")
      if sucursal >=1:
          list_sucursal.append(sucursal)
          list_pacientes.append(paciente)

for i in range (sucursal):
    print("Cantidad medicina sucursal",i+1)
    medicina = int(input())
    while medicina <1:
        print("no valido, ingresar dato valido")
        medicina = int(input())
    else:    
        list_medicina.append(medicina)
        list_original.append(medicina)

for i in range (paciente):
    print(f"ingresa sucursal, presion sistolica y presion diastolica paciente {i+1}")
    sucursal, p_sist, p_dist = map(int,input().split())
    if sucursal >=1 and sucursal<=sucursal:
        if p_sist<70 and p_dist<50:
            list_medicina[sucursal-1]-= 5
        elif p_sist in range (70,110) and p_dist in range (50,70):
            list_medicina[sucursal-1]-=0
        elif p_sist in range (110,120) and p_dist in range (70,75):
            list_medicina[sucursal-1]-=0
        elif p_sist in range (120,130) and p_dist in range (75,80):
            list_medicina[sucursal-1]-=10
        elif p_sist in range (130, 150) and p_dist in range (80, 90):
            list_medicina[sucursal-1]-=15
        elif p_sist in range (150, 170) and p_dist in range (90,100):
            list_medicina[sucursal-1]-=25
        elif p_sist >= 170 and p_dist >=100:
            list_medicina[sucursal-1]-=45
        elif p_sist >= 130 and p_dist <80:
            list_medicina[sucursal-1]-=25

men_exis= min(list_medicina)
pos_exis=list_medicina.index(men_exis)
may_exis= max(list_medicina)
pos_may_exis=list_medicina.index(may_exis) 

print(f"posision {pos_exis+1} {men_exis} ") 
print(f"posision {pos_may_exis+1} {may_exis} ")

for list_medicina, list_original in zip(list_medicina,list_original):
    porcentaje = (100-((list_medicina * 100) / list_original)) 
    print()
    print(porcentaje)

#for i in range(sucursal):
#    promedio = (1-list_medicina[i]/list_original[i])*100
#    print(f'{i+1} {promedio:.2f}%')
    
     