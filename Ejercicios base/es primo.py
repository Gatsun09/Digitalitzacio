#Gabriela Mañas

datousuario= int(input(" Introduce un número: "))

esPrimo=True

for num in range(2,datousuario//2 +1):
  if datousuario % num ==0:
      esPrimo = False
      break

if esPrimo == True:
    print("{0} es un número primo".format(datousuario))
else:
    print("{0} no es un número primo".format(datousuario))
