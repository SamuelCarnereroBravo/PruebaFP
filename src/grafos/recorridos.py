from typing import TypeVar, List, Dict, Set
from collections import deque

# Importa la clase Grafo desde su módulo
from grafo import Grafo  # Asegúrate de que Grafo esté correctamente implementado

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    """
    Realiza un recorrido en anchura (BFS) desde un vértice inicial hasta un vértice destino usando una Cola.
    
    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino más corto desde inicio a destino, o [] si no hay camino.
    """
    visitados: Set[V] = set()  # Conjunto para guardar vértices visitados
    cola: deque[V] = deque()  # Cola para BFS
    predecesores: Dict[V, V] = {}  # Diccionario para rastrear predecesores
    
    cola.append(inicio)
    predecesores[inicio] = None  # El inicio no tiene predecesor
    
    while cola:
        vertice = cola.popleft()
        
        if vertice == destino:  # Si encontramos el destino, salimos
            break
        
        if vertice not in visitados:
            visitados.add(vertice)
            
            for vecino in grafo.successors(vertice):  # Obtener vecinos del vértice
                if vecino not in visitados and vecino not in cola:
                    cola.append(vecino)
                    predecesores[vecino] = vertice
    
    # Reconstruimos el camino desde el diccionario de predecesores
    return reconstruir_camino(predecesores, destino)

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    """
    Realiza un recorrido en profundidad (DFS) desde un vértice inicial hasta un vértice destino usando una Pila.
    
    :param grafo: Grafo sobre el que realizar la búsqueda.
    :param inicio: Vértice inicial.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino desde inicio a destino, o [] si no hay camino.
    """
    visitados: Set[V] = set()  # Conjunto para guardar vértices visitados
    pila: List[V] = []  # Pila para DFS
    predecesores: Dict[V, V] = {}  # Diccionario para rastrear predecesores
    
    pila.append(inicio)
    predecesores[inicio] = None  # El inicio no tiene predecesor
    
    while pila:
        vertice = pila.pop()
        
        if vertice == destino:  # Si encontramos el destino, salimos
            break
        
        if vertice not in visitados:
            visitados.add(vertice)
            
            # Agregar vecinos en orden inverso para procesar en el orden correcto
            for vecino in reversed(grafo.neighbors(vertice)):
                if vecino not in visitados and vecino not in pila:
                    pila.append(vecino)
                    predecesores[vecino] = vertice
    
    # Reconstruimos el camino desde el diccionario de predecesores
    return reconstruir_camino(predecesores, destino)

def reconstruir_camino(predecesores: Dict[V, V], destino: V) -> List[V]:
    """
    Reconstruye el camino desde el origen hasta el destino usando el diccionario de predecesores.
    
    :param predecesores: Diccionario que mapea cada vértice a su predecesor.
    :param destino: Vértice de destino.
    :return: Lista de vértices en el camino desde el origen hasta el destino.
    """
    camino: List[V] = []
    vertice_actual = destino
    
    while vertice_actual is not None:  # Reconstruir desde el destino hasta el inicio
        camino.insert(0, vertice_actual)
        vertice_actual = predecesores.get(vertice_actual)
    
    return camino
