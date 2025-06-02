from helpers import random_U, graficos_corrector, graficos_detector, simulation_table, Qinv, Q
from codificacion import matrizGeneradora, mejorCodigo 
from decodificacion import corregir, detectar
from csb import canalCSB
import numpy as np
from scipy.special import erfcinv
import os


# e_p: Error de palabra
# e_b: Error de bit
# P_ep: Tasa de error de palabra
# P_eb: Tasa de error de bit
# EbN0_c: Energia/ruido con codigo (bit de fuente) [dB]
# EbN0_sc: Energia/ruido sin codigo (bit de fuente) [dB]
# Gc: Ganancia de codigo [dB]
# Ga: Ganancia de codigo asintotica [dB]


def Simulacion(EbN0_c, n, k, dmin, MODO, A = 1):
    """
    Simula el canal de comunicaciones y calcula las tasas de error de palabra y bit para un rango de energía/ruido.
    Args:
        EbN0_c (array): Rango de energía/ruido con codigo [dB]
        n (int): Longitud del bloque
        k (int): Longitud de la palabra
        tc (int): Longitud del codigo
        dmin (int): Distancia minima del codigo
        MODO (int): 0 = DETECTOR; 1 = CORRECTOR
    Returns:
        P_ep (np.ndarray): Tasa de error de palabra
        P_eb (np.ndarray): Tasa de error de bit
    """
    P_ep = np.zeros_like(EbN0_c, dtype=float)
    P_eb = np.zeros_like(EbN0_c, dtype=float)
    ITERACIONES = 10
    
    for i, EbN0 in enumerate(EbN0_c):
        H_t, G = matrizGeneradora(n, k, dmin) # Generar matrices de codigo 
        EbfN0 = 10**(EbN0/10)                 # Eb/N0 [veces]
        P_eb_t = Q(np.sqrt(2 * EbfN0))        # Tasa de error de bit teorica (estimada)
        PALABRAS = int((100) * (1/P_eb_t)) 
        PALABRAS = PALABRAS if (PALABRAS > 1000000) else 1000000
        
        # Arrays para almacenar resultados de cada iteración
        P_ep_iter = np.zeros(ITERACIONES)
        P_eb_iter = np.zeros(ITERACIONES)
        
        for iter in range(ITERACIONES):
            U = random_U(PALABRAS, k)             # Palabras fuente random
            V = np.dot(U, G) % 2                  # Codificar palabras fuente
            R = canalCSB(n, k, A, EbfN0, V)       # Simular canal con ruido
            if MODO:
                Ve = corregir(R, H_t)             # Decodificar palabras recibidas
                Ue = Ve[:, :k]
                E = U != Ue
            else:
                detectados = detectar(R, H_t)
                Ve = np.delete(R, detectados, axis=0)
                U = np.delete(U, detectados, axis=0)
                Ue = Ve[:, :k]
                E = U != Ue
            e_p = (E.sum(axis=1) > 0).sum() 
            P_ep_iter[iter] = e_p / E.shape[0] # Tasa de error de palabra
            e_b = E.sum()
            P_eb_iter[iter] = e_b / (k * E.shape[0]) # Tasa de error de bit
        # Promedio de iteraciones
        P_ep[i] = np.mean(P_ep_iter)
        P_eb[i] = np.mean(P_eb_iter)

        # Si no se observaron errores, establecer una cota superior para evitar ceros en la gráfica logarítmica
        total_palabras_simuladas = PALABRAS * ITERACIONES
        total_bits_simulados = k * total_palabras_simuladas
        if P_ep[i] == 0:
            P_ep[i] = 1 / total_palabras_simuladas
        if P_eb[i] == 0:
            P_eb[i] = 1 / total_bits_simulados
        
        print(f"Promedio final - Eb/N0: {EbN0:.2f} dB, Tasa de error de bit: {P_eb[i]:.6f}")
    return P_ep, P_eb

def main():
    MODO = 0 # 0 = DETECTOR; 1 = CORRECTOR
    n, k = 14, 10 # Parametros del codigo
    tc, dmin = mejorCodigo(n, k) # Parametros del codigo: Mejor (14,10)
    EbN0_c = np.linspace(1, 10, 30) # Rango de energia/ruido [dB]
    P_ep, P_eb = Simulacion(EbN0_c, n, k, dmin, MODO)
    Ga = 10 * np.log10((k/n)*np.floor((dmin + 1)/2)) # Ganancia de codigo asintotica
    EbN0_sc = 10 * np.log10((Qinv(P_eb) ** 2) * 0.5)
    Gc = EbN0_sc - EbN0_c

    # Crear directorios si no existen
    resultados_dir = os.path.join(os.path.dirname(__file__), 'resultados')
    os.makedirs(resultados_dir, exist_ok=True)

    # Analizar resultados
    print(f"n: {n}, k: {k}, tc: {tc}, dmin: {dmin}, Ga: {Ga:.2f} dB")
    
    if MODO == 0:  # DETECTOR
        graficos_detector(EbN0_c, P_ep, n, k, td=dmin - 1)
    else:  # CORRECTOR
        graficos_corrector(EbN0_c, P_eb, Gc, Ga, n, k, tc)
    
    # Guardar resultados
    df = simulation_table(EbN0_c, P_ep, P_eb, Gc, Ga)
    output_file = os.path.join(resultados_dir, f'{"detector" if MODO == 0 else "corrector"}.csv')
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()










