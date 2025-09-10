#!/usr/bin/env python3
"""
📝 Generador de Resumen del Problema 1

Este script genera un archivo Markdown con las respuestas conceptuales
y referencias a todos los resultados del Problema 1.
"""
from pathlib import Path
import os

def generar_resumen_problema1():
    """Genera el resumen completo del Problema 1 en formato Markdown"""
    
    # Verificar que existen los resultados
    results_dir = Path('../results/problema1')
    if not results_dir.exists():
        print("❌ No se encontraron resultados del Problema 1. Ejecuta primero solucion_problema1.py")
        return
    
    # Contenido del resumen
    contenido = """# 👏 Problema 1: Simulación de Onda Sonora - Respuestas Conceptuales

## 🌌 Resumen del Problema

El sistema modela el aire en una "habitación" unidimensional con paredes reflectivas.

### 🔬 Configuración Física
- **Ecuaciones hidrodinámicas**: ∂ρ/∂t + ∇⋅(ρv) = 0, ∂v/∂t + (v⋅∇)v = -1/ρ ∇P
- **Condiciones iniciales**: Perturbación tipo delta en el centro (como aplaudir)
- **Condiciones de frontera**: Reflectivas (paredes de la habitación)
- **Ecuación de estado**: P = c_s²ρ con c_s = 1

---

## 🤔 Respuestas a las Preguntas Conceptuales

### 1. ¿Qué pasa cuando la onda llega a las paredes?

**Respuesta:**
Con condiciones de frontera reflectivas, la onda se refleja invirtiendo el signo de la velocidad normal en la pared (no hay flujo saliendo) y generando interferencia con la onda incidente. Dependiendo del tiempo de viaje, pueden formarse patrones tipo estacionarios en el dominio (ecos internos).

**Evidencia visual:** Ver el video de densidad donde se observa cómo la perturbación se propaga hacia las paredes y se refleja.

![Video de Densidad](density.gif)

### 2. Si estás en el centro de la caja, ¿qué escucharías?

**Respuesta:**
Partimos de una perturbación localizada en el centro: se separa en dos frentes que viajan a ambos lados y regresan por reflexión. En el centro oirías una secuencia de pulsos (el original y ecos periódicos) separados por Δt ≈ 2L/cs (ida y vuelta), con cs = 1; la amplitud tiende a variar por superposición e interferencia.

**Evidencia visual:** El análisis de velocidades muestra la evolución temporal del movimiento en el centro.

**Condiciones iniciales (t=0):**
![Velocidades en t=0](velocities_t00.png)

**Evolución temporal (t=20):**
![Velocidades en t=20](velocities_t20.png)

### 3. Velocidades: dos tiempos y componente que es siempre cero

**Respuesta:**
En un caso unidimensional (eje x) con simetría y sin fuerzas transversales, las componentes transversales vx2 y vx3 se mantienen cero si arrancan en cero; solo vx1 (a lo largo de x) evoluciona.

**Evidencia visual:** Las imágenes muestran claramente que solo vx1 evoluciona, mientras vx2 y vx3 permanecen en cero.

*Las imágenes ya se mostraron arriba en la pregunta 2.*

### 4. Presión

**Respuesta:**
Con la ecuación de estado indicada P = c_s² ρ y c_s = 1, se cumple P = ρ. El script grafica P(x) para un tiempo seleccionado.

**Evidencia visual:** La distribución de presión calculada usando P = c_s² × ρ.

![Presión en t=20](pressure_t20.png)

---

## 🔥 Resultados Generados

### 🎬 Videos y Animaciones
- **Densidad**: `density.mp4` y `density.gif` - Evolución temporal de la densidad
- **Fotogramas**: `frames_density/*.png` - Imágenes individuales de cada tiempo

### 📈 Análisis de Velocidades
- **t=0**: Condiciones iniciales (todas las velocidades en cero)
- **t=20**: Evolución temporal (solo vx1 evoluciona)

### 📈 Análisis de Presión
- **t=20**: Distribución de presión P = c_s² × ρ

---

## 👀 Archivos de Resultados

Todos los archivos se encuentran en `results/problema1/`:
- Videos: `density.mp4`, `density.gif`
- Análisis: `velocities_t00.png`, `velocities_t20.png`, `pressure_t20.png`
- Fotogramas: `frames_density/*.png`

---

*Resumen generado automáticamente por el script de análisis del Problema 1*
"""
    
    # Escribir el archivo
    output_path = Path('../results/problema1/resumen_conceptual.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    print(f"✨ Resumen conceptual generado: {output_path}")

if __name__ == "__main__":
    generar_resumen_problema1()
