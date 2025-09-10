# 🌌 Simulaciones de Física Espacial - Tarea Programada I

Este proyecto contiene las soluciones computacionales para dos problemas fundamentales de la física espacial, implementados usando datos de simulaciones [PLUTO Code](https://plutocode.ph.unito.it).

## 📁 Estructura del Proyecto

```
tarea_programada_I/
├── src/                    # Código fuente
│   ├── solucion_problema1.py
│   ├── solucion_problema2.py
│   └── utils.py
├── notebooks/              # Jupyter Notebooks para análisis
│   ├── Problema1.ipynb
│   └── Problema2.ipynb
├── data/                   # Datos de entrada
│   ├── soundwave-data/
│   └── alfvenwave-data/
├── results/                # Resultados generados
│   ├── problema1/
│   └── problema2/
├── requirements.txt        # Dependencias
├── run_all.py              # Ejecutor de todas las simulaciones
└── README.md
```

## 🚀 Instalación y Uso

### 📋 Prerrequisitos (Ejecutar una vez)
```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 🎯 Opciones de Ejecución

#### Opción 1: Ejecutar todo de una vez (Recomendado)
```bash
python run_all.py
```

#### Opción 2: Ejecutar individualmente
```bash
# Problema 1: Onda sonora
cd src
python solucion_problema1.py

# Problema 2: Onda de Alfvén
python solucion_problema2.py
```

#### Opción 3: Análisis interactivo con Jupyter Notebooks
```bash
# Jupyter ya está incluido en requirements.txt
# Abrir notebooks interactivos
cd notebooks
jupyter notebook

# O abrir notebooks específicos
jupyter notebook Problema1.ipynb
jupyter notebook Problema2.ipynb
```

#### Opción 4: Exportar notebooks a diferentes formatos
```bash
# Exportar a HTML (recomendado para visualización)
jupyter nbconvert --to html notebooks/Problema1.ipynb --output-dir results/
jupyter nbconvert --to html notebooks/Problema2.ipynb --output-dir results/

# Exportar a PDF (requiere TeX)
# Opción A: Con TeX (más complejo)
# brew install --cask mactex  # En macOS
# jupyter nbconvert --to pdf notebooks/Problema1.ipynb --output-dir results/

```

## 👀 Resultados

Los resultados se generan automáticamente en la carpeta `results/`:

### 👏 Problema 1: Onda Sonora
- **🎬 Videos**: `density.mp4` y `density.gif` - Evolución temporal de la densidad
- **📈 Análisis**: Gráficas de velocidad y presión en diferentes tiempos
- **📓 Notebook**: `notebooks/Problema1.ipynb` - Análisis interactivo completo

### ⚡️ Problema 2: Onda de Alfvén
- **🎬 Videos**: `Bx.mp4`, `Bz.mp4`, `vx.mp4` y sus respectivos GIFs - Evolución de campo magnético y velocidad
- **📈 Análisis**: Gráficas de campo magnético, densidad y amplitud de perturbación
- **👀 Resumen numérico**: `resumen.txt` con valores calculados (ρ₀, B₀, v_A, régimen)
- **📓 Notebook**: `notebooks/Problema2.ipynb` - Análisis interactivo completo


## 🔧 Dependencias

### 📦 Dependencias Principales
- **`numpy`** - Cálculos numéricos y manejo de arrays
- **`matplotlib`** - Visualizaciones y gráficas científicas
- **`Pillow`** - Creación de GIFs (opcional, fallback si no hay ffmpeg)
- **`jupyter`** - Notebooks interactivos

### 🎬 Dependencias Opcionales
- **`ffmpeg`** - Creación de videos MP4 (opcional, pero recomendado) [FFmpeg Downloads](https://ffmpeg.org/download.html)
- **`TeX`** - Para exportar notebooks a PDF (opcional) [MacTeX](https://www.tug.org/mactex/)

---

**Autor**: Barbara Chassoul  
**Curso**: UCR, Física Espacial - Tarea Programada I
