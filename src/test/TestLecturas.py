from lecturas.lecturas import *
print("¿Qué ejercicio quieres hacer?")
ejercicio:int = int(input("Ejercicio: "))
if ejercicio == 6:
    print(f"Tu palabra aparece {ejercicio_6()} veces.")
elif ejercicio == 7:
    print(f"Tu palabra está en las siguientes líneas: {ejercicio_7()}")
elif ejercicio == 8:
    print(ejercicio_8())
elif ejercicio == 9:
    print(ejercicio_9())