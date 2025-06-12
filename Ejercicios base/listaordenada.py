
def esPar(num):
   return num %2==0

numcomponentes= int(input(" Introduce el tamaño de la lista: "))

lista= []

for i in range(numcomponentes):

    nuevonum= int(input("Introduce un nuevo número: "))
    lista.append(nuevonum)

print(lista)

for num in lista:
    if esPar(num):
        print("El número {0} ES par".format(num))
    else:
        print("El número {0} NO ES par".format(num))