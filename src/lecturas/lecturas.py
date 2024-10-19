def ejercicio_6():
    nombre_fichero = "fichero.txt"
    separador:str = " "
    with open(nombre_fichero, "r", encoding="utf-8") as archivo:
        print("¿Qué palabra quieres contar cuántas veces está?")
        palabra:str = input(" ")
        contenido:str = archivo.read()
        palabras:str = contenido.split(separador)
        contador:int = palabras.count(palabra)
        return contador
def ejercicio_7():
    nombre_fichero = "fichero.txt"
    lineas:list = []
    with open(nombre_fichero, "r", encoding="utf-8") as archivo:
        print("¿Qué palabra quieres ver en qué líneas está?")
        palabra_buscada:str = input(" ")
        for linea in archivo:
            if palabra_buscada in linea:
                lineas.append(linea.strip())
    return lineas
def ejercicio_8():
    nombre_fichero = "fichero2.txt"
    palabras_ = set()
    with open(nombre_fichero, "r", encoding = "utf-8") as archivo:
        for linea in archivo:
            palabras = linea.split()
            palabras_.update(palabras)
    return f"Las palabras únicas en el fichero resources/archivo_palabras.txt son: {list(palabras_)}"
def ejercicio_9():
    total_longitud:int = 0
    total_lineas:int = 0
    fichero:str = input("¿Qué archivo quieres revisar su longitud média? ¿vacio.csv o palabras_random.csv? ")
    with open(fichero, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            total_longitud += len(linea)
            total_lineas += 1
    
    if total_lineas == 0:
        return f"Este archivo tiene 0 líneas."
    else:
        return f"La longitud media de las líneas del fichero {fichero} es: {total_longitud/total_lineas}"