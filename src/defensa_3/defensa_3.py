from __future__ import annotations
from dataclasses import dataclass
from typing import TypeVar, Generic, Dict, Set, List
import matplotlib.pyplot as plt
import networkx as nx
from grafo import Grafo
@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> Gen:
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones no puede ser negativo.")
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> RelacionGenAGen:
        if not (-1 <= conexion <= 1):
            raise ValueError("La conexión debe estar entre -1 y 1.")
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

# Clase RedGenica que hereda de Grafo
class RedGenica(Grafo[Gen, RelacionGenAGen]):
    """
    Representa una red génica basada en un grafo.
    """
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}  # Mapa de nombres a genes

    @staticmethod
    def of(es_dirigido: bool = False) -> RedGenica:
        """
        Método de factoría para crear una nueva Red Génica.
        :param es_dirigido: Indica si la red génica es dirigida (True) o no dirigida (False).
        :return: Nueva red génica.
        """
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> RedGenica:
        """
        Método de factoría para crear una Red Génica desde archivos de genes y relaciones.
        :param f1: Archivo de genes.
        :param f2: Archivo de relaciones entre genes.
        :param es_dirigido: Indica si la red génica es dirigida (True) o no dirigida (False).
        :return: Nueva red génica.
        """
        red = RedGenica.of(es_dirigido)

        # Leer los genes desde el archivo f1 (genes.txt)
        with open(f1, 'r') as archivo_genes:
            for linea in archivo_genes:
                nombre, tipo, num_mutaciones, loc_cromosoma = linea.strip().split(',')
                gen = Gen.of(nombre, tipo, int(num_mutaciones), loc_cromosoma)
                red.add_vertex(gen)  # Agregar el gen como vértice al grafo
                red.genes_por_nombre[nombre] = gen  # Guardar el gen en el diccionario por su nombre

        # Leer las relaciones desde el archivo f2 (red_genes.txt)
        with open(f2, 'r') as archivo_relaciones:
            for linea in archivo_relaciones:
                nombre_gen1, nombre_gen2, conexion = linea.strip().split(',')
                conexion = float(conexion)
                gen1 = red.genes_por_nombre.get(nombre_gen1)
                gen2 = red.genes_por_nombre.get(nombre_gen2)

                if gen1 and gen2:
                    relacion = RelacionGenAGen.of(gen1, gen2, conexion)
                    red.add_edge(gen1, gen2, relacion)

        return red


    def subgraph(self, vertices: Set[Gen]) -> RedGenica:
        subgrafo = RedGenica(self.es_dirigido)
        for gen in vertices:
            subgrafo.add_vertex(gen)
        for gen1 in vertices:
            for gen2 in self.successors(gen1):
                if gen2 in vertices:
                    subgrafo.add_edge(gen1, gen2, self.adyacencias[gen1][gen2])
        return subgrafo

# Función DFS para búsqueda en profundidad
def dfs(red: RedGenica, start: Gen, end: Gen, visited: Set[Gen], path: List[Gen]) -> bool:
    visited.add(start)
    path.append(start)

    if start == end:
        return True

    for sucesor in red.successors(start):
        if sucesor not in visited:
            if dfs(red, sucesor, end, visited, path):
                return True

    path.pop()
    return False

# Función para dibujar la red génica
def draw_simple() -> None:
    # Crear un grafo no dirigido
    G = nx.Graph()

    # Definir los vértices
    vertices = ['KRAS', 'TP53', 'PIK3CA']

    # Agregar los vértices al grafo
    G.add_nodes_from(vertices)

    # Agregar las aristas con las conexiones especificadas
    G.add_edge('KRAS', 'TP53', weight=0.7)
    G.add_edge('TP53', 'PIK3CA', weight=0.2)

    # Definir la posición de los nodos
    pos = nx.spring_layout(G, seed=42)

    # Crear la figura y ajustar los parámetros del dibujo
    plt.figure(figsize=(6, 6))

    # Dibujar los nodos y las aristas
    nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=500, font_size=12, arrowsize=10)

    # Dibujar las etiquetas con los valores de las conexiones
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    # Título del gráfico
    plt.title("Red Génica Simplificada: KRAS, TP53, PIK3CA")
    plt.show()


# Función principal
def main():
    # Archivos de genes y relaciones
    f1 = "genes.txt"
    f2 = "red_genes.txt"
    
    # Crear la red génica no dirigida desde los archivos
    red_genica = RedGenica.parse(f1, f2, es_dirigido=False)
    
    # Buscar los vértices correspondientes a los genes KRAS y PIK3CA
    gen_kras = next((gen for gen in red_genica.vertices() if gen.nombre == "KRAS"), None)
    gen_pik3ca = next((gen for gen in red_genica.vertices() if gen.nombre == "PIK3CA"), None)
    
    if gen_kras is None or gen_pik3ca is None:
        print("Uno o ambos genes no se encontraron.")
        return

    # Realizar el recorrido en profundidad (DFS) desde KRAS hasta PIK3CA
    visited = set()
    path = []
    found_path = dfs(red_genica, gen_kras, gen_pik3ca, visited, path)

    if not found_path:
        print(f"No se encontró un camino entre {gen_kras.nombre} y {gen_pik3ca.nombre}.")
        return
    
    # Imprimir el camino encontrado
    print("Camino encontrado:")
    for gen in path:
        print(f"{gen.nombre} ->", end=" ")
    print("PIK3CA")

    # Crear un subgrafo a partir de los vértices del camino encontrado
    vertices_camino = set(path)
    subgrafo = red_genica.subgraph(vertices_camino)

    # Dibujar el subgrafo
    subgrafo.draw(titulo="Subgrafo: Camino entre KRAS y PIK3CA", lambda_vertice=lambda gen: gen.nombre)

if __name__ == "__main__":
    main()
