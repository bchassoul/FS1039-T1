# 🌌 Simulaciones de Física Espacial - Tarea Programada I

Este proyecto contiene las soluciones computacionales para dos problemas fundamentales de la física espacial, implementados usando datos de simulaciones [PLUTO Code](https://plutocode.ph.unito.it).

## 📁 Estructura del Proyecto

```
tarea_programada_I/
├── src/                    # Código fuente
│   ├── solucion_problema1.py
│   ├── solucion_problema2.py
│   ├── generar_resumen_problema1.py
│   ├── generar_resumen_problema2.py
│   └── utils.py
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

# Generar resúmenes conceptuales
python generar_resumen_problema1.py
python generar_resumen_problema2.py
```

## 👀 Resultados

Los resultados se generan automáticamente en la carpeta `results/`:

### 👏 Problema 1: Onda Sonora
- **🎬 Videos**: `density.mp4` y `density.gif` - Evolución temporal de la densidad
- **📈 Análisis**: Gráficas de velocidad y presión en diferentes tiempos
- **🤔 Resumen conceptual**: `resumen_conceptual.md` - Respuestas a preguntas conceptuales con imágenes embebidas

### ⚡️ Problema 2: Onda de Alfvén
- **🎬 Videos**: `Bx.mp4`, `Bz.mp4`, `vx.mp4` y sus respectivos GIFs - Evolución de campo magnético y velocidad
- **📈 Análisis**: Gráficas de campo magnético, densidad y amplitud de perturbación
- **👀 Resumen numérico**: `resumen.txt` con valores calculados (ρ₀, B₀, v_A, régimen)
- **🤔 Resumen conceptual**: `resumen_conceptual.md` - Respuestas a preguntas conceptuales con imágenes embebidas

## 🔧 Dependencias

- **`numpy`** - Cálculos numéricos y manejo de arrays
- **`matplotlib`** - Visualizaciones y gráficas científicas
- **`Pillow`** - Creación de GIFs (opcional, fallback si no hay ffmpeg)
- **`ffmpeg`** - Creación de videos MP4 (opcional, pero recomendado) [FFmpeg Downloads](https://ffmpeg.org/download.html)


---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

**Autor**: Barbara Chassoul  
**Versión**: 1.0.0  
**Curso**: UCR, Física Espacial - Tarea Programada I
