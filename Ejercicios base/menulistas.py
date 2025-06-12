

print("0-Terminar ")
print("1-Borrar lista ")
print("2-Consultar tamaño de lista ")
print("3-Añadir elemento 'por detrás' ")
print("4-Elimianr elementos 'por delante'")
print(" Introduce una opción >>>")

def imprimilista(): print(" La lista queda: {0}".format(lista))
#programa principal

valorusuario = -1
lista=[ ]

while valorusuario !=0:
 valorusuario=int(input())

 if valorusuario == 1:
     lista.clear()
     imprimilista( )

 elif valorusuario == 2:
     print(len(lista))

 elif valorusuario == 3:
     nuevo= int(input("Dame un nuevo número: "))
     lista.append(nuevo)
     imprimilista()

 elif valorusuario ==4:
      if len(lista) >=1:
          del lista[0]
      imprimilista()



