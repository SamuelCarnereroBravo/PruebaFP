import math
from typing import List, Tuple
from collections import Counter
import string
def P2(): #En esta función y en todas las funciones están contempladas todas las posibles casuísticas que se puedan dar, lanzando el mensaje de error correspondiente. Para poder visualizar todas las casuísticas se debe dar los respectivos valores que las contemplen.
    while True:
        try:
            print("Dale valores a k, a n y a i")
            k:int = int(input("k = "))
            n:int = int(input("n = "))
            i:int = int(input("i = "))

            assert k <= n, "n tiene que ser mayor o igual que k"
            assert n >= 0, "n y k tienen que ser números positivos"
            assert i > 0, "i tiene que ser positivo mayor que 0"
            assert i < k + 1, "i tiene que ser menor a k + 1"

            resultado: int = 1
            for i in range(i, k - 1):
                resultado = resultado * (n - i + 1)

            return resultado

        except AssertionError as error:
            print(f"Error: {error}.")
        except ValueError:
            print("Error: n, k e i tienen que ser números enteros.")
def C2():
    while True:
        try:
            print("Dale valores a n y a k")
            k:int = int(input("k = "))
            n:int = int(input("n = "))
            
            assert n > k, "n tiene que ser mayor que k"
            assert n > 0, "n y k tienen que ser positivos"
            
            resultado:int = int(factorial(n)/(factorial(k+1)*factorial(n-k-1)))
            return resultado
        except AssertionError as error:
            print(f"Error: {error}.")
        except ValueError:
            print("Error: n y k tienen que ser números enteros.")
def S2() -> float:
    while True:
        try:
            print("Dale valores a k y a n")
            k:int = int(input("k = "))
            n:int = int(input("n = "))
            i:int = 1
            assert n>=k, "n tiene que ser mayor o igual que k"
            assert n>0, "n y k tienen que ser positivos mayores que 0"
            s:float = 0.0
            for i in range(i,k+1):
                s = s + (-1)**i * (math.factorial(k)/(math.factorial(i)*math.factorial(k-i))) * (k-i)**(n+1)
            resultado:float = math.factorial(k)*s/(n*math.factorial(k+2))
            return resultado
        except AssertionError as error:
            print(f"Error: {error}")
        except ValueError:
            print("Error: n y k tienen que ser números enteros.")
def palabrasMasComunes(fichero: str, n: int = 5) -> List[Tuple[str, int]]:
    if n <= 1:
        raise ValueError("El valor de 'n' debe ser mayor que 1")
    
    try:
        contenido: str
        with open(fichero, 'r', encoding='utf-8') as file:
            contenido = file.read()
        contenido_minusculas: str = contenido.lower()
        contenido_sin_puntuacion: str = contenido_minusculas.translate(
            str.maketrans('', '', string.punctuation)
        )
        palabras: List[str] = contenido_sin_puntuacion.split()
        contador: Counter = Counter(palabras)
        palabras_comunes: List[Tuple[str, int]] = contador.most_common(n)
        return palabras_comunes
    except FileNotFoundError:
        print(f"El archivo '{fichero}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
print("¿Qué ejercicio quieres hacer?")
Ejercicio:str = input("")
if Ejercicio == "P2":
    print(P2())
elif Ejercicio == "C2":
    print(C2())
elif Ejercicio == "S2":
    print(S2())
elif Ejercicio == "palabrasMasComunes":
    print(palabrasMasComunes("archivo_palabras.txt"))