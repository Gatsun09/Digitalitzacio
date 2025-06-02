#Gabriela Mañas
#Version 1.0

cadenausuario=input("Introduce una cadena: ")

posicionreversa= len(cadenausuario)-1

esPalindromo=True

for posicion in range(0, len(cadenausuario)):
    if(cadenausuario[posicion]!= cadenausuario[posicionreversa]):
        esPalindromo=False
        break
    posicionreversa= posicionreversa-1

if esPalindromo ==True:
    print("La cadena {0} es palindramo".format(cadenausuario))
else:
    print("La cadena {0} no es palindramo".format(cadenausuario))
