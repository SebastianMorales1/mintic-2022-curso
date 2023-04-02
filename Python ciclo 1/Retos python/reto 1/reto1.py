paciente = input()
# Ingresar solamente las palabras "ayunas" o "posprandial".
sangre = float(input())
# Ingresar el nivel de glucosa en sangre (mg/dl).

if paciente =='ayunas':
  if sangre<70:
    print("hipoglusemia")
  elif 70 <= sangre < 100:
    print("sin diabetes")
  elif 100 <= sangre < 125:
    print("pre diabetes")
  else:
    print("diabetes")  
elif paciente =='posprandial':
  if sangre<140:
    print("sin diabetes")
  elif 140 <= sangre < 200:
    print("pre diabetes")
  else:
    print("diabetes")
else:
  print("error en los datos")