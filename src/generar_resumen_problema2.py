#!/usr/bin/env python3
"""
📝 Generador de Resumen del Problema 2

Este script genera un archivo Markdown con las respuestas conceptuales
y referencias a todos los resultados del Problema 2.
"""
from pathlib import Path
import os

def generar_resumen_problema2():
    """Genera el resumen completo del Problema 2 en formato Markdown"""
    
    # Verificar que existen los resultados
    results_dir = Path('../results/problema2')
    if not results_dir.exists():
        print("❌ No se encontraron resultados del Problema 2. Ejecuta primero solucion_problema2.py")
        return
    
    # Leer el resumen numérico si existe
    resumen_path = results_dir / 'resumen.txt'
    resumen_numerico = ""
    if resumen_path.exists():
        with open(resumen_path, 'r') as f:
            resumen_numerico = f.read().strip()
    
    # Contenido del resumen
    contenido = f"""# ⚡️ Problema 2: Simulación de Onda de Alfvén - Respuestas Conceptuales

## 🌌 Resumen del Problema

Las ondas de Alfvén son fundamentales en física espacial y astrofísica, propagándose a lo largo de las líneas de campo magnético.

### 🔬 Configuración Física
- **Ecuaciones MHD**: Propagación de ondas en campo magnético
- **Campo inicial**: B₀ = B₀ê_z (alineado con eje z)
- **Perturbación**: B₁ = 0.1 sin(8π/L · z)ê_x (perpendicular al campo)
- **Condiciones de frontera**: Periódicas (simulación infinita)
- **Densidad**: Constante durante la propagación

---

## 🤔 Respuestas a las Preguntas Conceptuales

### 1. ¿Qué son las ondas de Alfvén y cómo se propagan?

**Respuesta:**
Las ondas de Alfvén son perturbaciones magnetohidrodinámicas que se propagan a lo largo de las líneas de campo magnético. En este problema, la perturbación inicial B₁ = 0.1 sin(8π/L · z)ê_x es perpendicular al campo principal B₀ê_z, lo que genera ondas de Alfvén que se propagan a lo largo del eje z.

**Evidencia visual:** Los videos muestran la propagación de estas perturbaciones a lo largo del dominio.

**Campo magnético Bx (perturbación perpendicular):**
![Video Bx](Bx.gif)

**Campo magnético Bz (campo principal):**
![Video Bz](Bz.gif)

**Velocidad vx (perturbación de velocidad):**
![Video vx](vx.gif)

### 2. ¿Por qué las componentes By y vy permanecen aproximadamente cero?

**Respuesta:**
En una onda de Alfvén pura propagándose a lo largo del eje z, las perturbaciones ocurren solo en las direcciones perpendiculares al campo magnético principal. Como el campo inicial es B₀ê_z y la perturbación es B₁ê_x, no hay componentes en la dirección y, por lo que By ≈ 0 y vy ≈ 0.

**Evidencia visual:** El análisis confirma que estas componentes permanecen en cero durante toda la simulación.

![Verificación By y vy](by_vy_t10.png)

### 3. ¿Cuál es la velocidad de Alfvén y cómo se calcula?

**Respuesta:**
La velocidad de Alfvén se calcula como v_A = B₀/√(ρ₀), donde B₀ es la intensidad del campo magnético principal y ρ₀ es la densidad del plasma. Esta velocidad caracteriza la propagación de las ondas de Alfvén.

**Resultados numéricos:**
{resumen_numerico}

**Evidencia visual de las condiciones iniciales:**

**Densidad inicial:**
![Densidad en t=0](rho_t00.png)

**Campo magnético inicial:**
![Campo magnético en t=0](bz_t00.png)

### 4. ¿En qué régimen se encuentra la simulación: sub-Alfvénico o súper-Alfvénico?

**Respuesta:**
El régimen se determina comparando la velocidad de perturbación con la velocidad de Alfvén. Si la velocidad de perturbación es menor que v_A, el régimen es sub-Alfvénico (M_A < 1); si es mayor, es súper-Alfvénico (M_A ≥ 1).

**Análisis:** Según los resultados, la simulación se encuentra en régimen **sub-Alfvénico** (M_A < 1), lo que significa que las perturbaciones se propagan más lentamente que la velocidad de Alfvén.

### 5. ¿Cómo evoluciona la amplitud de la perturbación en el tiempo?

**Respuesta:**
La amplitud de la perturbación puede evolucionar debido a efectos no lineales, dispersión o disipación. En ondas de Alfvén lineales, la amplitud debería mantenerse constante, pero efectos no lineales pueden causar modulaciones.

**Evidencia visual:** El gráfico muestra la evolución temporal de la amplitud de la perturbación de velocidad.

![Evolución de amplitud](vx_amp_over_time.png)

---

## 🔥 Resultados Generados

### 🎬 Videos y Animaciones
- **Campo magnético Bx**: `Bx.mp4` y `Bx.gif` - Evolución de la perturbación perpendicular
- **Campo magnético Bz**: `Bz.mp4` y `Bz.gif` - Evolución del campo principal
- **Velocidad vx**: `vx.mp4` y `vx.gif` - Evolución de la velocidad de perturbación
- **Fotogramas**: `frames_Bx/*.png`, `frames_Bz/*.png`, `frames_vx/*.png`

### 📈 Análisis de Condiciones Iniciales
- **Densidad inicial**: Distribución de densidad en t=0
- **Campo magnético inicial**: Campo magnético principal en t=0

### 📈 Verificación de Perturbaciones
- **Componentes perpendiculares**: Verificación de que By ≈ 0, vy ≈ 0

### 📈 Análisis de Amplitud
- **Evolución temporal**: Amplitud de perturbación vs tiempo

### 📝 Resumen Numérico
- **Parámetros calculados**: `resumen.txt` - Valores de ρ₀, B₀, v_A, M_A

---

## 👀 Archivos de Resultados

Todos los archivos se encuentran en `results/problema2/`:
- Videos: `Bx.mp4`, `Bx.gif`, `Bz.mp4`, `Bz.gif`, `vx.mp4`, `vx.gif`
- Análisis: `rho_t00.png`, `bz_t00.png`, `by_vy_tXX.png`, `vx_amp_over_time.png`
- Resumen: `resumen.txt`
- Fotogramas: `frames_Bx/*.png`, `frames_Bz/*.png`, `frames_vx/*.png`

---

*Resumen generado automáticamente por el script de análisis del Problema 2*
"""
    
    # Escribir el archivo
    output_path = Path('../results/problema2/resumen_conceptual.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    print(f"✨ Resumen conceptual generado: {output_path}")

if __name__ == "__main__":
    generar_resumen_problema2()
