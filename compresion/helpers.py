import matplotlib.pyplot as plt
import numpy as np
import os

def estadisticas_compresion(resultados):
    """
    Genera gráficos de las estadísticas de compresión.
    
    Args:
        resultados: Lista de diccionarios con las estadísticas de compresión
    """
    # Crear directorio de gráficos si no existe
    graficos_dir = os.path.join(os.path.dirname(__file__), 'graficos')
    os.makedirs(graficos_dir, exist_ok=True)

    # Extraer datos
    n_values = [r['n'] for r in resultados]
    longitudes = [r['longitud_promedio'] for r in resultados]
    tasas = [r['tasa_compresion'] for r in resultados]
    
    # Crear figura con dos subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Gráfico 1: Longitud promedio/n vs n
    ax1.plot(n_values, np.array(longitudes)/n_values, 'bo-', label='Longitud promedio/n')
    ax1.set_xlabel('n (tamaño del bloque)')
    ax1.set_ylabel('Longitud promedio/n (bits/símbolo)')
    ax1.set_title('Longitud promedio normalizada vs extension de fuente')
    ax1.grid(True)
    ax1.legend()
    
    # Gráfico 2: Tasa de compresión vs n
    ax2.plot(n_values, tasas, 'ro-', label='Tasa de compresión')
    ax2.set_xlabel('n (tamaño del bloque)')
    ax2.set_ylabel('Tasa de compresión')
    ax2.set_title('Tasa de compresión vs extension de fuente')
    ax2.grid(True)
    ax2.legend()
    
    # Ajustar layout y guardar antes de mostrar
    plt.tight_layout()
    output_file = os.path.join(graficos_dir, 'Longitudes_Tasas.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.show()


def distribuciones_probabilidad(codigos_info, n):
    """
    Genera gráficos de las distribuciones de probabilidad de los símbolos.

    Args:
        codigos_info: Lista de diccionarios con información de los símbolos
        n: Tamaño del bloque
    """
    # Crear directorio de gráficos si no existe
    graficos_dir = os.path.join(os.path.dirname(__file__), 'graficos')
    os.makedirs(graficos_dir, exist_ok=True)

    # Extraer símbolos y probabilidades
    simbolos = [codigo['simbolo'] for codigo in codigos_info]
    probabilidades = [codigo['probabilidad'] for codigo in codigos_info]
    equiprob = 1/len(probabilidades)
    
    # Crear figura
    plt.figure(figsize=(15, 5))
    
    # Gráfico de barras
    plt.bar(range(len(simbolos)), probabilidades, alpha=0.7, color='blue')
    plt.axhline(equiprob, color='red', linestyle='--', 
                label=f'Equiprobabilidad ({equiprob:.4f})')
    
    # Configurar ejes
    plt.title(f'Probabilidad de cada símbolo n={n}')
    plt.xlabel('Símbolo')
    plt.ylabel('Probabilidad')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Configurar etiquetas del eje x
    plt.xticks(range(len(simbolos)), simbolos, rotation=45, ha='right')
    
    # Ajustar layout y guardar antes de mostrar
    plt.tight_layout()
    output_file = os.path.join(graficos_dir, f'distribucion_probabilidades_n{n}.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.show()
    
    
