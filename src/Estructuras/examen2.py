from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Callable

E = TypeVar('E')
R = TypeVar('R')

class AgregadoLineal(ABC, Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0

    @property
    def elements(self) -> List[E]:
        return self._elements

    @abstractmethod
    def add(self, e: E) -> None:
        pass

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        if self.is_empty:
            raise EmptyContainerError("El agregado está vacío")
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    # Nuevas funcionalidades
    def contains(self, e: E) -> bool:
        """
        Verifica si un elemento está en el agregado.
        """
        return e in self._elements

    def find(self, func: Callable[[E], bool]) -> E | None:
        """
        Devuelve el primer elemento que cumple la condición dada por func.
        Si no encuentra nada, devuelve None.
        """
        for element in self._elements:
            if func(element):
                return element
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        """
        Devuelve una lista de elementos que cumplen la condición dada por func.
        """
        return [element for element in self._elements if func(element)]

class ListaOrdenada(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

    @classmethod
    def of(cls, order: Callable[[E], R]):
        return cls(order)

    def _index_order(self, e: E) -> int:
        for index, current in enumerate(self._elements):
            if self._order(e) < self._order(current):
                return index
        return len(self._elements)

    def add(self, e: E) -> None:
        index = self._index_order(e)
        self._elements.insert(index, e)

    def __str__(self) -> str:
        return f"ListaOrdenada({', '.join(map(str, self._elements))})"

class ColaConLimite(AgregadoLineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que 0")
        self._capacidad = capacidad

    @classmethod
    def of(cls, capacidad: int):
        return cls(capacidad)

    def add(self, e: E) -> None:
        if self.is_full:
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    @property
    def is_full(self) -> bool:
        return len(self._elements) >= self._capacidad

    def __str__(self) -> str:
        return f"ColaConLimite({', '.join(map(str, self._elements))})"
    
    '''
     Ejercicio 3: Pruebas de todo el código
    '''
    
def test_ejercicio_1():
    print("Pruebas para ColaConLimite:")

    # Crear una cola con límite de capacidad 3
    cola = ColaConLimite.of(3)
    print(f"Cola inicial: {cola}")

    # Agregar elementos hasta el límite
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")
    print(f"Cola después de agregar 3 elementos: {cola}")

    try:
        cola.add("Tarea 4")  # Debe lanzar OverflowError
    except OverflowError as e:
        print(f"Error esperado al agregar un cuarto elemento: {e}")

    # Eliminar un elemento y agregar otro
    print(f"Elemento removido: {cola.remove()}")
    cola.add("Tarea 4")
    print(f"Cola después de remover y agregar un nuevo elemento: {cola}")

def test_ejercicio_2():
    print("\nPruebas para AgregadoLineal (con las nuevas funcionalidades):")

    # Usamos ListaOrdenada como implementación concreta de AgregadoLineal
    lista = ListaOrdenada.of(lambda x: x)

    # Agregar elementos
    lista.add_all([1, 3, 5, 7, 9])
    print(f"Lista ordenada: {lista}")

    # Probar contains
    print(f"Contiene el número 3? {lista.contains(3)}")
    print(f"Contiene el número 4? {lista.contains(4)}")

    # Probar find
    print(f"Primer número mayor que 4: {lista.find(lambda x: x > 4)}")
    print(f"Primer número menor que 0: {lista.find(lambda x: x < 0)}")
    
    # Agregar más elementos
    lista.add_all([2, 4, 6, 8, 10])
    
    # Probar filter
    print(f"Números pares: {lista.filter(lambda x: x % 2 == 0)}")
    print(f"Números mayores que 5: {lista.filter(lambda x: x > 5)}")

    # Agregar más elementos y probar nuevamente
    lista.add_all([11,12,13,14,15,16])
    print(f"Lista después de agregar más elementos: {lista}")

    # Nuevas pruebas con el método filter
    print(f"Números divisibles por 3: {lista.filter(lambda x: x % 3 == 0)}")

# Ejecutamos las pruebas
test_ejercicio_1()
test_ejercicio_2()




