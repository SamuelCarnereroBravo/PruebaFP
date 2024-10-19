from funciones.funciones import *
print("¿Qué ejercicio quieres hacer?")
ejercicio:int = int(input("Ejercicio: "))
if ejercicio == 1:
    print(ejercicio_1())
elif ejercicio == 2:
    print(ejercicio_2())
elif ejercicio == 3:
    print(ejercicio_3())
elif ejercicio == 4:
    print(ejercicio_4())
elif ejercicio == 5:
    print(ejercicio_5())
else:
    print("Ese no es un ejercicio de la lista.")