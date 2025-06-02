#Gabriela Mañas

cadena1 = input(" Dame la cadena original: ")

cadena2 = input("Dame un candidato a sufijo: ")

esSufijo = True

pos=0

print(len(cadena1)-len(cadena2))

for i in range( len(cadena1)-len(cadena2), len(cadena1)):
    print(i,pos)
    if (cadena1[i] != cadena2[pos]):
        esSufijo= False
        break
    pos += 1

if(esSufijo==False):
    print("La segunda cadena no es sufijo de la primera.")
else:
    print("La segunda cadena es sufijo de la primera.")