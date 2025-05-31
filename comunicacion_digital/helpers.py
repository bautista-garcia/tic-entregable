import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc, erfcinv, comb
import pandas as pd
import os

def Q(x):
    """
    Función Q para entrada escalar o vectorial.
    """
    return 0.5 * erfc(x / np.sqrt(2))

def Qinv(p):
    """
    Función Q^-1 para entrada escalar o vectorial.
    """
    p = np.asarray(p)
    return np.sqrt(2) * erfcinv(2 * p)

def random_U(n: int, k:int):
    """
    Genera una matriz U de n palabras de longitud k en GF(2)
    """
    return np.random.randint(0, 2, (n, k))

def graficos_corrector(Ebn_c, P_eb, Gc, Ga, n, k, tc):
    """
    Genera gráficos para el modo CORRECTOR:
    - Curvas de tasa de error de bit y teórica
    - Ganancia asintótica y ganancia real
    """
    Ebn_c = np.asarray(Ebn_c) # Eb/n0 de fuente (simulacion) [dB]
    P_eb = np.asarray(P_eb) # Pebf de fuente (simulacion)
    Gc = np.asarray(Gc) # Ganancia del codigo
    Ebn_c_veces = 10**(Ebn_c/10) # Eb/n0 de fuente [veces]
    Q_teorica = Q(np.sqrt(2 * Ebn_c_veces)) # Q teorica
    p_canal = Q(np.sqrt(2 * Ebn_c_veces * (k/n))) # Pebf del canal
    P_eb_teorica = ((2 * tc + 1)/n) * (comb(n, tc + 1)) * (p_canal ** (tc + 1))
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    
    # Gráfico de tasa de error de bit
    axs[0].semilogy(Ebn_c, P_eb, 'o-', label=r'$P_{eb}$ (codificada - simulacion)')
    axs[0].semilogy(Ebn_c, P_eb_teorica, '--', label=r'$P_{eb}$ (codificada - teórica)')
    axs[0].semilogy(Ebn_c, Q_teorica, '--', label=r'$Q(\sqrt{2 E_b/N_0})$ (sin codificar - teórica)')
    axs[0].set_xticks(np.arange(np.min(Ebn_c), np.max(Ebn_c) + 1, 1))
    axs[0].grid(True, which="both", ls="-", alpha=0.2)
    axs[0].set_yscale('log')
    axs[0].set_xlabel('Eb/N0 [dB]')
    axs[0].set_ylabel(f'$P_eb$') 
    axs[0].set_title('Curvas BER - MODO: CORRECTOR')
    axs[0].legend()
    
    # Gráfico de ganancia de código vs tasa de error de bit
    axs[1].semilogx(P_eb, np.full_like(P_eb, Ga), 'k--', label='Ga (asintótico)')
    axs[1].semilogx(P_eb, Gc, 'o-', label='Ganancia real del código')
    axs[1].set_xlabel('Tasa de error de bit ($P_{eb}$)')
    axs[1].set_ylabel('Ganancia (dB)')
    axs[1].set_title('Ganancia asintótica vs real')
    axs[1].legend()
    axs[1].grid(True, ls='--', alpha=0.5)
    
    plt.tight_layout()
    graficos_dir = os.path.join(os.path.dirname(__file__), 'graficos')
    os.makedirs(graficos_dir, exist_ok=True)
    plt.savefig(os.path.join(graficos_dir, 'CORRECTOR.png'))
    plt.show()

def graficos_detector(Ebn_c, P_ep, n, k, td, dmin):
    """
    Genera gráficos para el modo DETECTOR:
    - Curvas de tasa de error de palabra y teórica
    Todos los argumentos deben ser np.arrays.
    """
    Ebn_c = np.asarray(Ebn_c) # Eb/n0 [dB]
    P_ep = np.asarray(P_ep) # Tasa de error de palabra
    Ebn_c_veces = 10**(Ebn_c/10) * (k/n) # Eb/n0 (canal) [veces]
    Q_teorica = Q(np.sqrt(2 * Ebn_c_veces)) # Q teorica
    P_ep_teorica = (comb(n, td + 1)) * (Q_teorica ** (td + 1))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Gráfico de tasa de error de palabra
    ax.semilogy(Ebn_c, P_ep, 'o-', label=r'$P_{ep}$ (codificada - simulacion)')
    ax.semilogy(Ebn_c , P_ep_teorica, '--', label=r'$P_{ep}$ (codificada - teórica)')
    ax.semilogy(Ebn_c, Q_teorica, '--', label=r'$Q(\sqrt{2 E_b/N_0})$ (sin codificar - teórica)')
    ax.set_xticks(np.arange(np.min(Ebn_c), np.max(Ebn_c) + 1, 1))
    ax.grid(True, which="both", ls="-", alpha=0.2)
    ax.set_yscale('log')
    ax.set_xlabel('Eb/N0 [dB]')
    ax.set_ylabel(f'$P_ep$') 
    ax.set_title('Curvas WER - MODO: DETECTOR')
    ax.legend()
    
    plt.tight_layout()
    graficos_dir = os.path.join(os.path.dirname(__file__), 'graficos')
    os.makedirs(graficos_dir, exist_ok=True)
    plt.savefig(os.path.join(graficos_dir, 'DETECTOR.png'))
    plt.show()

def simulation_table(Ebn_c, P_ep, P_eb, Gc, Ga):
    """
    Crea y retorna una tabla (DataFrame) con los resultados de la simulación.
    Todos los argumentos deben ser np.arrays.
    """
    Ebn_c = np.asarray(Ebn_c)
    P_ep = np.asarray(P_ep)
    P_eb = np.asarray(P_eb)
    Gc = np.asarray(Gc)
    Ga_arr = np.full_like(Ebn_c, Ga)
    df = pd.DataFrame({
        'Eb/N0 [dB]': Ebn_c,
        'P_ep': P_ep,
        'P_eb': P_eb,
        'Gc (dB)': Gc,
        'Ga (dB)': Ga_arr
    })
    return df

    



    
