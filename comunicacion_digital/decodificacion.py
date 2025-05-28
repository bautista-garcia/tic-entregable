import numpy as np

def corregir(R, H_t):
    """
    Corrige (tc = 1) errores en la matriz de palabras código recibidas R
    
    Args:
        R: Matriz de palabras código recibidas (cada fila es una palabra código)
        H_t: Matriz de chequeo de paridad del código (H_transpuesta)
    
    Returns:
        Ve: Matriz de palabras de codigo corregidas
    """
    
    # Calculamos sindromes
    S = np.dot(R, H_t) % 2

    for i in range(S.shape[0]): 
        if np.sum(S[i]) != 0:
            # Buscamos fila de H_t que coincide con el sindrome
            for j in range(H_t.shape[0]):
                if np.array_equal(S[i], H_t[j]):
                    # Corregimos el error (invertimos bit de error)
                    R[i][j] = (R[i][j] + 1) % 2
                    break
    return R

def detectar(R, H_t):
    """
    Detecta (td = 2) errores en la matriz de palabras código recibidas R
    
    Args:
        R: Matriz de palabras código recibidas (cada fila es una palabra código)
        H_t: Matriz de chequeo de paridad del código (H_transpuesta)
    
    Returns:
        detectados: Vector con indices de palabras con errores detectados
    """

    S = np.dot(R, H_t) % 2
    detectados = [i for i in range(S.shape[0]) if np.sum(S[i]) != 0]
    return detectados