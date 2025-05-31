from frecuencias import frecuencias_imagen
from huffman import construir_arbol_huffman, obtener_codigos
from helpers import estadisticas_compresion, distribuciones_probabilidad
import numpy as np
from PIL import Image
import os

def calcular_estadisticas_compresion(n, ruta_imagen):
    """
    Calcula las estadísticas de compresión para un valor de n dado.
    
    Args:
        n (int): Tamaño del bloque
        ruta_imagen (str): Ruta de la imagen a comprimir
    
    Returns:
        dict: Diccionario con las estadísticas de compresión
    """
    # Datos de imagen original 
    original_img = np.array(Image.open(ruta_imagen).convert('L'))
    SHAPE = original_img.shape
    LONGITUD = original_img.size
    SIMBOLOS = LONGITUD // n
    LONGITUD_PROMEDIO_SC = 1  # Sin comprimir

    # Cálculo de frecuencias y armado de árbol de Huffman
    frecuencias = frecuencias_imagen(ruta_imagen, n)
    arbol = construir_arbol_huffman(frecuencias)
    codigos = obtener_codigos(arbol)

    # Información de los símbolos
    codigos_info = []
    for simbolo, codigo in codigos.items():
        codigos_info.append({
            'simbolo': simbolo,
            'codigo': codigo,
            'probabilidad': frecuencias[simbolo] / SIMBOLOS
        }) 

    # Verificación de la suma de probabilidades
    assert np.allclose(sum(codigo['probabilidad'] for codigo in codigos_info), 1)
    
    # Cálculo de estadísticas
    LONGITUD_PROMEDIO_C = sum((codigo['probabilidad']) * len(codigo['codigo']) for codigo in codigos_info)
    TASA_COMPRESION = 1/(LONGITUD_PROMEDIO_C / n)  # n símbolos por bloque  

    return {
        'n': n,
        'longitud_promedio': LONGITUD_PROMEDIO_C,
        'tasa_compresion': TASA_COMPRESION,
        'codigos_info': codigos_info,
        'shape': SHAPE,
        'longitud': LONGITUD,
        'simbolos': SIMBOLOS,
    }

def main():
    # Configuración de rutas
    directorio_actual = os.path.dirname(__file__)
    ruta_imagen = os.path.join(directorio_actual, 'logoFI.tif')
    
    # Parámetros de simulación
    n_values = np.arange(1, 15, 1)  # Valores de n a probar

    # Calcular estadísticas para cada valor de n
    resultados = []
    for n in n_values:
        print(f"\nCalculando estadísticas para n={n}...")
        stats = calcular_estadisticas_compresion(n, ruta_imagen)
        resultados.append(stats)

    # Generar gráficos
    estadisticas_compresion(resultados)
    
    # Generar gráfico de distribución de probabilidades para n=4
    distribuciones_probabilidad(resultados[3]['codigos_info'], n=4)

if __name__ == "__main__":
    main()

