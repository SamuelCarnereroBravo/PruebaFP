import math
def ejercicio_1():
    print("Dale valores a n y a k:")
    n:int = int(input("n= "))
    k:int = int(input("k= "))
    if n>k: 
        s:int=1
        for i in range(0,k+1):
            s=s*(n-i+1)
        return(f"El producto de {n} y {k} es {s}")
    else:
        return("El primer número debe ser más grande que el segundo")
def ejercicio_2():
    print("Dale valores a a, k y r respectivamente:")
    a:int = int(input("a = "))
    k:int = int(input("k = "))
    r:int = int(input("r = "))
    b:int
    c:int=1
    n:int
    for n in range(1,k+1):
        b=a*(r**(n-1))
        c=c*b
    return(f"El producto de la secuencia geométrica con a1 = {a}, r = {r} y k = {k} es: {c}") 
def ejercicio_3():
    print("Dale valores a n y a k, además, asegúrate de que n sea mayor que k.")
    n:int= int(input("n = "))
    k:int= int(input("k = "))
    fact:int=int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
    if n<k or k<0:
        print("n tiene que ser mayor que k y ambos tienen que ser positivos")
    else:
       return(f"El combinatorio de {n} y {k} es {fact}")
def ejercicio_4():
    print("Dale valores tanto a n como a k")
    n= int(input("n = "))
    k= int(input("k = "))
    i:int
    suma:int=0
    total:float
    if n<=k or k<2:
        return("n tiene que ser mayor que k y ambos tienen que ser mayores que dos")
    else:
        for i in range(0,k):
            suma=suma +((-1)**i) * (int(math.factorial(k+1)/(math.factorial(i+1)*math.factorial(k-i))))*((k-i)**n)
            total=(1/(math.factorial(k))*suma)
        return(f"El número S(n,k) siendo n = {n} y k = {k} es: {total}")
def ejercicio_5(): #Sea f(x)=2x^2+2x-3 y f'(x)=4x+2
    print("Dada la función f(x)=2x^2+2x-3 y f'(x)=4x+2. Inicializa el valor de inicial a que tomará f y el error que quieres asegurar.")
    a:float = float(input("a = "))
    error:float = float(input("error = "))
    while abs((2*a**2+2*a-3)) > error:
        a = a - (2*a**2+2*a-3)/(4*a+2)
    return(f"El resultado con a = 3 y el error = {error} en las funciones: f(x) = 2x^2+2x-3 y f'(x) = 4x+2 es {a}")
