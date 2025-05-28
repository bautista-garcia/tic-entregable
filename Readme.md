# Documentación del Proyecto de Comunicaciones Digitales y Compresión

## Estructura del Proyecto

```
.
├── comunicacion_digital/
│   ├── resultados/         # Almacena resultados de simulaciones
│   ├── graficos/          # Almacena gráficos generados
│   ├── main.py            # Script principal de simulación
│   ├── helpers.py         # Funciones auxiliares
│   ├── csb.py             # Implementación del canal CSB
│   ├── codificacion.py    # Funciones de codificación
│   └── decodificacion.py  # Funciones de decodificación
│
└── compresion/
    ├── graficos/          # Almacena gráficos generados
    ├── main.py            # Script principal de compresión
    ├── helpers.py         # Funciones auxiliares
    ├── frecuencias.py     # Análisis de frecuencias
    ├── huffman.py         # Implementación del algoritmo de Huffman
    └── logoFI.tif         # Imagen de prueba
```

## Módulo de Comunicación Digital

### Descripción General
Este módulo implementa un sistema de comunicación digital con codificación de canal para la detección y corrección de errores.

### Componentes Principales

#### main.py
- Función `Simulacion(EbN0_c, n, k, dmin, MODO, A)`: Realiza la simulación del canal de comunicaciones
  - Calcula tasas de error de palabra y bit
  - Parámetros:
    - `EbN0_c`: Rango de energía/ruido con código [dB]
    - `n`: Longitud del bloque
    - `k`: Longitud de la palabra
    - `dmin`: Distancia mínima del código
    - `MODO`: 0 = DETECTOR, 1 = CORRECTOR
    - `A`: Amplitud (opcional, default=1)

#### csb.py
Implementa el canal simétrico binario (CSB) para la simulación de transmisión de datos.

#### codificacion.py
Contiene las funciones para la generación de matrices de código y la codificación de mensajes.

#### decodificacion.py
Implementa las funciones de detección y corrección de errores en los mensajes recibidos.

## Módulo de Compresión

### Descripción General
Este módulo implementa algoritmos de compresión de datos, específicamente el algoritmo de Huffman.

### Componentes Principales

#### main.py
Script principal que coordina el proceso de compresión.

#### huffman.py
Implementa el algoritmo de compresión de Huffman.

#### frecuencias.py
Analiza las frecuencias de los símbolos en los datos a comprimir.

## Funciones Auxiliares (helpers.py)

### En Comunicación Digital
- `random_U()`: Genera palabras fuente aleatorias
- `graficos()`: Genera gráficos de resultados
- `simulation_table()`: Crea tablas de resultados
- `Q()` y `Qinv()`: Funciones de error y su inversa

### En Compresión
- Funciones de soporte para el procesamiento de datos y visualización

## Uso

### Comunicación Digital
1. Ejecutar `main.py` en el directorio `comunicacion_digital/`
2. Los resultados se guardarán en el directorio `resultados/`
3. Los gráficos se generarán en el directorio `graficos/`

### Compresión
1. Ejecutar `main.py` en el directorio `compresion/`
2. Los resultados y gráficos se guardarán en el directorio `graficos/`

## Notas
- Los resultados de las simulaciones se guardan en formato CSV
- Los gráficos se generan automáticamente durante la ejecución
- El módulo de comunicación digital permite simular tanto detección como corrección de errores
- El módulo de compresión incluye una implementación del algoritmo de Huffman 

## Configuración del Entorno Virtual

Para configurar el entorno de desarrollo y ejecutar el proyecto, sigue estos pasos:

1. Crear un entorno virtual:
```bash
# En Windows
python -m venv venv

# En macOS/Linux
python3 -m venv venv
```

2. Activar el entorno virtual:
```bash
# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

Una vez completados estos pasos, el entorno estará listo para ejecutar los módulos del proyecto. Recuerda que cada vez que abras una nueva terminal, deberás activar el entorno virtual nuevamente. 