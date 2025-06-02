#Gabriela Mañas

datousuario= int(input(" Dame un número del 1 al 10: "))

if datousuario % 2 !=0:
    print(" Elegiste impares ", end=' ')

    num=1

    while num<11:
        print(num)
        num+=2

else:
    print(" Elegiste pares ", end=' ')

    for num in range(0, 11, 2):

        print(num, end=" ")
