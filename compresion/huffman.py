import heapq
from collections import defaultdict, Counter

class Nodo:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(frecuencias):
    """
    Construye el árbol de Huffman a partir de las frecuencias.
    
    Args:
        frecuencias: Diccionario con las frecuencias de cada símbolo
    
    Returns:
        Nodo: Raíz del árbol de Huffman
    """
    # Creamos un nodo x simbolo de fuente con su frecuencia
    heap = [Nodo(s, f) for s, f in frecuencias.items()]
    heapq.heapify(heap)

    # Creamos arbol de huffman
    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)
        nuevo_nodo = Nodo(None, nodo1.frecuencia + nodo2.frecuencia)
        nuevo_nodo.izq = nodo1
        nuevo_nodo.der = nodo2
        heapq.heappush(heap, nuevo_nodo)
    
    return heap[0]

def obtener_codigos(nodo, codigo_actual="", codigos=None):
    """
    Obtiene los códigos Huffman para cada símbolo.
    
    Args:
        nodo: Nodo actual del árbol
        codigo_actual: Código acumulado hasta el momento
        codigos: Diccionario para almacenar los códigos
    
    Returns:
        dict: Diccionario con los códigos Huffman para cada símbolo
    """
    if codigos is None:
        codigos = {}
        
    # Recorremos arbol recursivamente (0: izquierda, 1: derecha)
    if nodo is None:
        return codigos
        
    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = codigo_actual
        
    obtener_codigos(nodo.izq, codigo_actual + "0", codigos)
    obtener_codigos(nodo.der, codigo_actual + "1", codigos)
    
    return codigos


