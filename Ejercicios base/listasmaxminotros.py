lista = []

for i in range (10):
    lista.append(int(input(" Introduce un nuevo número:" )))

min=lista[0]
max=lista[0]
sumatorio=[0]

for i in range(len(lista)):
    sumatorio+=lista[i]


    if lista[i] > max:
        max=lista[i]
    if lista[i] < min:
        min= lista[i]

print(" El valor medio calculado es: " +str(sumatorio/len(lista)))
print(" El valor máximo es: " .format(max))
print(" El valor mínimo es: " +str(min))
