#Gabriela Mañas

nota= float(input( " Introduce una nota: "))

if nota < 5:
    print("Suspendido")
elif nota >= 5 and nota<7:
    print("Bien")
elif nota >= 7 and nota <9:
    print("Notable")
else:
    print("Excelente")