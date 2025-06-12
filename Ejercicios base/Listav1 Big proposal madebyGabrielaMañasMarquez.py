#Made by Gabriela Mañas Marquez

print("0-Terminar ")
print("1-Borrar lista ")
print("2-Añadir un nuevo numero 'por detrás' ")
print("3-Eliminar un numero 'por delante'")
print(">>>")

lista=[ ]
valorusuario = -1

def imprimilista(): print(" La lista queda: {0}".format(lista))

def esPar(): print({0}.formatlista)
esPar=True


while valorusuario !=0:
 valorusuario=int(input())

 if valorusuario == 1:
     lista.clear()
     imprimilista( )

 elif valorusuario == 2:
     nuevo= int(input("Dame un nuevo número: "))
     lista.append(nuevo)
     imprimilista()

 elif valorusuario ==3:
      if len(lista) >=1:
          del lista[0]
      imprimilista()
 elif valorusuario ==0:
     break


for valorusuario in lista:

    if valorusuario %2==0:
        print(valorusuario*2)
        esPar=True

    elif valorusuario:
        print(valorusuario+100)
        esPar=False


min=lista[0]
max=lista[0]
sumatorio=[0]

for i in range(len(lista)):
    sumatorio = lista[i]+lista[i]

    if lista[i] > max:
        max=lista[i]
    if lista[i] < min:
        min= lista[i]

print("El valor medio calculado es:", str(sumatorio/(len(lista)-1)))
print(" El valor máximo es: ", (max))
print(" El valor mínimo es: " +str(min))