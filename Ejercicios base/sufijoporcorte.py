c1 = input(" Dame la cadena original: ")

c2 = input("Dame un candidato a sufijo: ")

corte= c1[len(c1)-len(c2):]

if corte ==c2:
    print("La segunda cadena no es sufijo de la primera.")
else:
    print("La segunda cadena es sufijo de la primera.")