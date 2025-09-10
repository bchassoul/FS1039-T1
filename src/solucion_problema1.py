#!/usr/bin/env python3
"""
🌬 Problema 1: Simulación de Onda Sonora

Este script analiza la propagación de ondas sonoras en un medio unidimensional
usando datos de simulación PLUTO. El problema simula el comportamiento de una
onda sonora en una "habitación" unidimensional con paredes reflectivas.

📋 Contexto del Problema:
- Ecuaciones hidrodinámicas: ∂ρ/∂t + ∇⋅(ρv) = 0, ∂v/∂t + (v⋅∇)v = -1/ρ ∇P
- Condiciones iniciales: perturbación tipo delta en el centro (como aplaudir)
- Condiciones de frontera: reflectivas (paredes de la habitación)
- Ecuación de estado: P = c_s²ρ con c_s = 1

🎯 Tareas Implementadas:
1. ✅ Visualización de densidad ρ(x,t) con rango fijo para comparación
2. ✅ Creación de video mostrando la evolución temporal
3. ✅ Análisis de componentes de velocidad (vx, vy, vz)
4. ✅ Cálculo y visualización de presión P = c_s²ρ
5. ✅ Respuestas conceptuales sobre reflexión en paredes

📁 Datos requeridos: data/soundwave-data/
📊 Resultados: results/problema1/

Ejecutar desde src/: python solucion_problema1.py
"""
import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from utils import clean_results_directory, discover_times, ensure_dir, create_video_and_gif

# ---------- Utilidades ----------

def fixed_ylim(values, pad_frac=0.05):
    vmin = float(np.min(values))
    vmax = float(np.max(values))
    if np.isclose(vmin, vmax):
        # Evitar rango cero
        delta = 1.0 if vmax == 0 else abs(vmax)*0.1
        vmin -= delta
        vmax += delta
    pad = (vmax - vmin) * pad_frac
    return vmin - pad, vmax + pad


# ---------- Limpieza de resultados anteriores ----------
# Limpiar resultados anteriores
clean_results_directory('problema1')

# ---------- Carga de datos de simulación PLUTO ----------
data_dir = Path('../data/soundwave-data')
x_path = data_dir / 'x1.npy'
if not x_path.exists():
    raise SystemExit(f"❌ No se encontró {x_path}. Asegúrate de que la carpeta 'data/soundwave-data/' esté en el directorio raíz del proyecto.")

x = np.load(x_path)
rho_times = discover_times(str(data_dir / 'rho_*.npy'))
if not rho_times:
    raise SystemExit("❌ No se encontraron archivos rho_*.npy en 'data/soundwave-data/'.")

# Descubrir tiempos para velocidades
vx1_times = discover_times(str(data_dir / 'vx1_*.npy'))
vx2_times = discover_times(str(data_dir / 'vx2_*.npy'))
vx3_times = discover_times(str(data_dir / 'vx3_*.npy'))

# Rango fijo para densidad
rhos_minmax = []
for t in rho_times:
    rho_t = np.load(data_dir / f'rho_{t:02d}.npy')
    rhos_minmax.append((rho_t.min(), rho_t.max()))
rho_min = min(v[0] for v in rhos_minmax)
rho_max = max(v[1] for v in rhos_minmax)
ymin, ymax = fixed_ylim([rho_min, rho_max], pad_frac=0.05)

# ---------- Tarea 1: Generación de fotogramas y video de densidad ----------
frames_dir = Path('../results/problema1/frames_density')
ensure_dir(frames_dir)

print(f"✨ Generando {len(rho_times)} fotogramas de densidad...")
for t in rho_times:
    rho_t = np.load(data_dir / f'rho_{t:02d}.npy')
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(x, rho_t, lw=2)
    ax.set_title(f"Densidad ρ(x)  —  t = {t} (u.t.)")
    ax.set_xlabel("x (u.l.)")
    ax.set_ylabel("ρ (u.)")
    ax.set_ylim(ymin, ymax)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fname = frames_dir / f'density_{t:02d}.png'
    fig.savefig(fname, dpi=180)
    plt.close(fig)

# ---------- Video y GIF a partir de los fotogramas ----------
print("✨ Creando video MP4 y GIF de densidad...")
mp4_ok, gif_ok = create_video_and_gif(
    frames_dir=frames_dir,
    output_base='../results/problema1/density',
    fps=10,
    file_pattern='density_%0{width}d.png'
)

# ---------- Tarea 4: Análisis de componentes de velocidad ----------
if rho_times:
    tA, tB = rho_times[0], rho_times[-1]
    for t in (tA, tB):
        # Cargar componentes de velocidad
        vx_data = []
        labels = []
        for comp in ('vx1', 'vx2', 'vx3'):
            fpath = data_dir / f'{comp}_{t:02d}.npy'
            if fpath.exists():
                vx = np.load(fpath)
                vx_data.append(vx)
                labels.append(comp)
            else:
                vx_data.append(None)
                labels.append(f"{comp} (no encontrado)")

        fig, ax = plt.subplots(figsize=(7, 4))
        for vx, lab in zip(vx_data, labels):
            if vx is not None:
                ax.plot(x, vx, lw=2, label=lab)
        ax.set_title(f"Componentes de velocidad — t = {t}")
        ax.set_xlabel("x (u.l.)")
        ax.set_ylabel("v (u.)")
        ax.grid(True, alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(f'../results/problema1/velocities_t{t:02d}.png', dpi=180)
        plt.close(fig)
    print(f"✨ Figuras de velocidad guardadas como velocities_t{tA:02d}.png y velocities_t{tB:02d}.png")

# ---------- Tarea 5: Cálculo y visualización de presión ----------
cs = 1.0  # Velocidad del sonido
tP = rho_times[-1]
rho_tP = np.load(data_dir / f'rho_{tP:02d}.npy')
P_tP = (cs**2) * rho_tP  # P = c_s² * ρ

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, P_tP, lw=2)
ax.set_title(f"Presión P(x) = c_s^2 · ρ(x)  —  t = {tP}  (c_s = {cs})")
ax.set_xlabel("x (u.l.)")
ax.set_ylabel("P (u.)")
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(f'../results/problema1/pressure_t{tP:02d}.png', dpi=180)
plt.close(fig)
print(f"✨ Figura de presión guardada como pressure_t{tP:02d}.png")

print("🔥 Archivos generados en results/problema1/:")
print(" - Videos: density.mp4 y density.gif")
print(" - Análisis: velocities_t{tA:02d}.png, velocities_t{tB:02d}.png, pressure_t{tP:02d}.png")
print(" - Fotogramas: frames_density/*.png")
print("📣 Para generar el resumen conceptual, ejecuta:")
print("===>   python generar_resumen_problema1.py")
