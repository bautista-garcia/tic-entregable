import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc, erfcinv
import pandas as pd

def Q(x):
    """
    Q-function for array or scalar input.
    """
    return 0.5 * erfc(x / np.sqrt(2))

def Qinv(p):
    """
    Q-inverse function for array or scalar input.
    """
    p = np.asarray(p)
    return np.sqrt(2) * erfcinv(2 * p)

def random_U(n: int, k:int):
    """
    Genera una matriz U de n palabras de longitud k en GF(2)
    """
    return np.random.randint(0, 2, (n, k))


def graficos(Ebn_c, P_eb, Gc, Ga, MODO):
    """
    Primer subplot: Curvas de tasa de error de bit y teórica.
    Segundo subplot: Ganancia asintótica (constante) y ganancia real (curva).
    Todos los argumentos deben ser np.arrays.
    """
    Ebn_c = np.asarray(Ebn_c)
    P_eb = np.asarray(P_eb)
    Gc = np.asarray(Gc)
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    axs[0].semilogy(Ebn_c, P_eb, 'o-', label=f'BER - MODO: {MODO}')
    Q_teorica = 0.5 * erfc(np.sqrt(10**(Ebn_c/10)))
    axs[0].semilogy(Ebn_c, Q_teorica, '--', label=r'$Q(\sqrt{2 E_b/N_0})$ (teórica)')
    axs[0].set_xticks(np.arange(np.min(Ebn_c), np.max(Ebn_c) + 1, 1))
    axs[0].grid(True, which="both", ls="-", alpha=0.2)
    axs[0].set_yscale('log')
    axs[0].set_xlabel('Eb/N0 [dB]')
    axs[0].set_ylabel(f'$P_eb$') 
    axs[0].set_title(f'Curvas BER - MODO: {MODO}')
    axs[0].legend()
    axs[1].plot(Ebn_c, np.full_like(Ebn_c, Ga), 'k--', label='Ga (asintótico)')
    axs[1].plot(Ebn_c, Gc, 'o-', label='Ganancia real del código')
    axs[1].set_xticks(np.arange(np.min(Ebn_c), np.max(Ebn_c) + 1, 1))
    axs[1].set_xlabel('Eb/N0 [dB]')
    axs[1].set_ylabel('Ganancia (dB)')
    axs[1].set_title('Ganancia asintótica vs real')
    axs[1].legend()
    axs[1].grid(True, ls='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f'comunicacion_digital/graficos/{MODO}.png')
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

    



    
