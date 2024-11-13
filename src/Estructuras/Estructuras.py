from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic, Callable

E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')

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

class ListaOrdenadaSinRepeticion(ListaOrdenada[E, R]):
    @classmethod
    def of(cls, order: Callable[[E], R]):
        return cls(order)

    def add(self, e: E) -> None:
        if e not in self._elements:
            index = self._index_order(e)
            self._elements.insert(index, e)

    def __str__(self) -> str:
        return f"ListaOrdenadaSinRepeticion({', '.join(map(str, self._elements))})"

class Cola(AgregadoLineal[E]):
    @classmethod
    def of(cls):
        return cls()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __str__(self) -> str:
        return f"Cola({', '.join(map(str, self._elements))})"

class ColaPrioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []
        self._priorities: List[P] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0

    @property
    def elements(self) -> List[E]:
        return self._elements

    def add(self, e: E, priority: P) -> None:
        index = self._index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    def _index_order(self, priority: P) -> int:
        for index, current_priority in enumerate(self._priorities):
            if priority < current_priority:
                return index
        return len(self._priorities)

    def remove(self) -> E:
        if self.is_empty:
            raise EmptyContainerError("La cola de prioridad está vacía")
        self._priorities.pop(0)
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def decrease_priority(self, e: E, new_priority: P) -> None:
        if e in self._elements:
            index = self._elements.index(e)
            if new_priority < self._priorities[index]:
                self._elements.pop(index)
                self._priorities.pop(index)
                self.add(e, new_priority)

    def __str__(self) -> str:
        elements_with_priorities = [(e, p) for e, p in zip(self._elements, self._priorities)]
        return f"ColaPrioridad({elements_with_priorities})"

class Pila(AgregadoLineal[E]):
    @classmethod
    def of(cls):
        return cls()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)

    def __str__(self) -> str:
        return f"Pila({', '.join(map(str, self._elements))})"
    
# Test_Lista_ordenada.py

print("TEST DE LISTA ORDENADA:")

# Crear una lista ordenada con el criterio de orden: orden natural (lambda x: x)
orden_lista = ListaOrdenada.of(lambda x: x)

print("Creación de una lista con criterio de orden lambda x: x")
print("Se añade en este orden: 3, 1, 2")
# Añadir elementos
orden_lista.add(3)
orden_lista.add(1)
orden_lista.add(2)

# Imprimir el resultado
print(f"Resultado de la lista: {orden_lista}")


# Eliminar un elemento con remove()
eliminado = orden_lista.remove()
print(f"El elemento eliminado al utilizar remove(): {eliminado}")


# Eliminar todos los elementos con remove_all()
eliminados = orden_lista.remove_all()
print(f"Elementos eliminados utilizando remove_all: {eliminados}")


# Añadir elementos de nuevo para comprobar si se añaden en la posición correcta
print("Comprobando si se añaden los números en la posición correcta...")
orden_lista.add(0)
print(f"Lista después de añadirle el 0: {orden_lista}")
orden_lista.add(10)
print(f"Lista después de añadirle el 10: {orden_lista}")
orden_lista.add(7)
print(f"Lista después de añadirle el 7: {orden_lista}")
print("#" * 48)
# Test_Lista_ordenada_sin_repeticion.py

print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")

# Crear una lista ordenada sin repetición con el criterio de orden: orden inverso (lambda x: -x)
orden_lista_sin_rep = ListaOrdenadaSinRepeticion.of(lambda x: -x)

print("Creación de una lista con criterio de orden lambda x: -x")
print("Se añade en este orden: 23, 47, 47, 1, 2, -3, 4, 5")
# Añadir elementos
orden_lista_sin_rep.add(23)
orden_lista_sin_rep.add(47)
orden_lista_sin_rep.add(47)
orden_lista_sin_rep.add(1)
orden_lista_sin_rep.add(2)
orden_lista_sin_rep.add(-3)
orden_lista_sin_rep.add(4)
orden_lista_sin_rep.add(5)

# Imprimir el resultado
print(f"Resultado de la lista ordenada sin repetición: {orden_lista_sin_rep}")

# Eliminar un elemento con remove()
eliminado = orden_lista_sin_rep.remove()
print(f"El elemento eliminado al utilizar remove(): {eliminado}")

# Eliminar todos los elementos con remove_all()
eliminados = orden_lista_sin_rep.remove_all()
print(f"Elementos eliminados utilizando remove_all: {eliminados}")

# Añadir elementos de nuevo para comprobar si se añaden en la posición correcta
print("Comprobando si se añaden los números en la posición correcta...")
orden_lista_sin_rep.add(0)
print(f"Lista después de añadirle el 0: {orden_lista_sin_rep}")
orden_lista_sin_rep.add(10)
print(f"Lista después de añadirle el 0: {orden_lista_sin_rep}")
orden_lista_sin_rep.add(7)
print(f"Lista después de añadirle el 7: {orden_lista_sin_rep}")
print("#" * 48)
# Test_Cola.py

print("TEST DE COLA:")

# Crear una cola vacía
cola = Cola.of()

print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
# Añadir elementos a la cola
cola.add(23)
cola.add(47)
cola.add(1)
cola.add(2)
cola.add(-3)
cola.add(4)
cola.add(5)

# Imprimir el resultado
print(f"Resultado de la cola: {cola}")

# Eliminar todos los elementos con remove_all()
eliminados = cola.remove_all()
print(f"Elementos eliminados utilizando remove_all: {eliminados}")
print("#" * 48)

def test_cola_prioridad():
    # Crear una cola de prioridad de pacientes
    cola = ColaPrioridad[str, int]()
    
    # Agregar pacientes con prioridades
    cola.add('Paciente A', 3)  # Dolor de cabeza leve
    cola.add('Paciente B', 2)  # Fractura en la pierna
    cola.add('Paciente C', 1)  # Ataque cardíaco

    # Verificar el estado de la cola
    assert cola.elements == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto."

    # Atender a los pacientes y verificar el orden de atención
    atencion = []
    while not cola.is_empty:
        atencion.append(cola.remove())
    
    assert atencion == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de atención no es correcto."
    
    print("Pruebas superadas exitosamente.")

if __name__ == '__main__':
    print("TEST DE COLA CON PRIORIDAD")
    test_cola_prioridad()
    print("#" * 48)