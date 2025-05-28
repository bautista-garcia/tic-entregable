import numpy as np

def canalCSB(n, k, A, EbfN0, V):
    """
    Simula la transmisión y recepción de palabras código a través de un canal AWGN con modulación BPSK.
    
    Args:
        n: Largo de palabra de código
        k: Largo de palabra de fuente
        A: Amplitud de la señal BPSK
        EbfN0: Cociente Eb/N0 deseado (en veces, no dB)
        V: Matriz de palabras código (cada fila es una palabra código)
    
    Returns:
        Rd: Matriz de palabras código recibidas (cada fila es una palabra código)
    """
    # Calcular energías
    Es = A**2 
    Ebf = Es * n / k
    N0 = Ebf / EbfN0
    # Modulación BPSK (0 -> -A, 1 -> +A)
    S = (2 * V - 1) * A
    # Ruido AWGN para cada palabra código
    noise = np.sqrt(N0 / 2) * (np.random.randn(*S.shape) + 1j * np.random.randn(*S.shape))
    # Señal recibida
    R = S + noise
    # Demodulación (detección dura)
    Rd = (np.real(R) > 0).astype(int)
    return Rd

