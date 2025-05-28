import numpy as np 
from scipy.special import comb
from itertools import combinations

def mejorCodigo(n: int, k: int):
    """
    Encuentra el codigo con menor distancia minima de hamming para (n, k)
    
    Args:
        n (int): Longitud total del código
        k (int): Longitud de la palabra de información
    
    Returns:
        tuple: (tc, dmin)
        - tc: Cantidad de errores corregibles
        - dmin: Distancia minima de hamming 
    
    """
    LIM = 100
    tc = 0 

    while(tc < LIM):
        lhs = [comb(n, idx) for idx in range(tc + 1)]
        if((res1:=np.sum(lhs)) > (res2:=2**(n - k))): 
            tc -= 1
            break
        tc += 1

    return tc, (2 * tc + 1) 
    

def matrizGeneradora(n: int, k: int, dmin: int):
    """
    Genera una matriz de paridad H(transpuesta) de forma sistemática y su matriz P
    
    Args:
        n (int): Longitud total del código
        k (int): Longitud de la palabra de información
        dmin (int): Distancia mínima de Hamming requerida
        
    Returns:c
        tuple: (H, G)
            - H es la matriz de paridad (n x (n-k))
            - G es la matriz generadora (k x n)
    """
    # Crear matriz generadora vacía
    H = np.zeros((n, (n-k)), dtype=int)
    P = np.zeros((k, (n-k)), dtype=int)
    G = np.zeros((k, n), dtype=int)
    # k filas de P con peso de hamming >= dmin-1 
    filas = []
    min_w = dmin - 1
    # Generar filas sistemáticamente por peso de hamming 
    for num_ones in range(min_w, (n - k) + 1):
        for positions in combinations(range(n - k), num_ones):
            row = np.zeros((n - k), dtype=int)
            row[list(positions)] = 1
            filas.append(row)
            if len(filas) == k:
                break
        if len(filas) == k:
            break
    for i, row in enumerate(filas):
        H[i] = P[i] = row
    # Resto de filas de H forman la matriz identidad
    H[k:] = np.eye((n - k))
    # Generamos la matriz G a partir de P
    G[:, :k] = np.eye(k)
    G[:, k:] = P
    return H, G  

