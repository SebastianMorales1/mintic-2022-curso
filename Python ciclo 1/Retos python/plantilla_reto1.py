# Reto 1

n= int(input())
suma_acidez= 0 
suma_materia= 0
total_noapto= 0
total_marginal= 0
total_modera= 0
total_suma=0
for i in range(n):
  datos= input()
#  datos= datos.split()
#  acidez= float(input())
#  materia= float(input())
  acidez, materia = map(float,input().split())

  entorno_acidez= 0
  suma_acidez += acidez 
  
  if acidez>8.0 or acidez<4.5:
    entorno_acidez= 1
  elif (4.5 <= acidez <= 5.0) or (7.0 <= acidez <= 8.0):
    entorno_acidez= 2
  elif (5.0<acidez<=5.5) or (6.5<acidez<=7.0):
    entorno_acidez = 3
  elif (5.5 < acidez <= 6.5):
    entorno_acidez= 4
  #
  entorno_materia= 0
  suma_materia += materia
  if materia < 3.0:
    entorno_materia= 1
  elif (3.0 <= materia <= 4.0):
    entorno_materia= 2
  elif (4.0 <= materia <= 5.0):
    entorno_materia= 3
  elif (materia > 5.0):
    entorno_materia = 4
  #
  # Determinando el entorno final
  entorno= 0
  if entorno_acidez < entorno_materia:
    entorno= entorno_acidez
  else :
    entorno= entorno_materia
  #
  if entorno==1:
    total_noapto += 1
  elif entorno==2:
    total_marginal += 1
  elif entorno==3:
    total_modera += 1
  elif entorno==4:
    total_suma += 1

# Salidas Esperadas
print('{:.2f}'.format(suma_acidez / n))
print('{:.2f}'.format(suma_materia / n))
print(f"sumamente apto {total_suma}")
print(f"moderadamente apto {total_modera}")
print(f"marginalmente apto {total_marginal}")
print(f"no apto {total_noapto}")