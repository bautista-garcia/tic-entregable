import numpy as np
from collections import Counter
from PIL import Image


def frecuencias_imagen(image_path, n):
    """
    Calcula las frecuencias de bloques de tamaño n en la imagen.
    
    Args:
        image_path: Ruta de la imagen
        n: Tamaño del bloque
    
    Returns:
        Counter: Diccionario con las frecuencias de cada bloque de tamaño n
    """
    # Convertimos a imagen a array en escala de grises
    img = np.array(Image.open(image_path).convert('L'))
    # Convertimos (2D) a (1D)
    flat = img.flatten()
    
    # Aseguramos que la longitud sea múltiplo de n
    flat = flat[:len(flat) - (len(flat) % n)]
    
    # Bloques de exactamente n símbolos consecutivos
    blocks = [tuple(flat[i:i+n]) for i in range(0, len(flat), n)]
    
    # Frecuencias x bloque
    freq = Counter(blocks)
    return freq




