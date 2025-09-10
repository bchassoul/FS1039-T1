#!/usr/bin/env python3
"""
⚡️ Problema 2: Simulación de Onda de Alfvén

🎯 Tareas Implementadas:
1. Visualización de Bx(z), Bz(z), vx(z) con rangos fijos según ejercicio
2. Verificación de perturbación perpendicular: By ≈ 0, vy ≈ 0
3. Cálculo de condiciones iniciales: ρ₀, B₀, velocidad de Alfvén v_A
4. Análisis de amplitud de perturbación y clasificación del régimen
5. Determinación si es régimen sub-Alfvénico o súper-Alfvénico

📁 Datos requeridos: data/alfvenwave-data/
🔥 Resultados: results/problema2/

Ejecutar desde src/: python solucion_problema2.py
"""
import math
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from utils import clean_results_directory, discover_times, ensure_dir, create_video_and_gif

# ---------- Utilidades ----------

def fixed_ylim_from_series(series_list, pad_frac=0.05, symmetric=False):
    vmin = min(float(np.min(s)) for s in series_list if s is not None and s.size > 0)
    vmax = max(float(np.max(s)) for s in series_list if s is not None and s.size > 0)
    if symmetric:
        m = max(abs(vmin), abs(vmax))
        vmin, vmax = -m, m
    if np.isclose(vmin, vmax):
        delta = 1.0 if vmax == 0 else abs(vmax)*0.1
        vmin -= delta
        vmax += delta
    pad = (vmax - vmin) * pad_frac
    return vmin - pad, vmax + pad


def write_summary(path, lines):
    with open(path, 'w') as f:
        for L in lines:
            f.write(str(L).rstrip() + '\n')

# ---------- Limpieza de resultados anteriores ----------
# Limpiar resultados anteriores
clean_results_directory('problema2')

# ---------- Carga de datos de simulación PLUTO ----------
data_dir = Path('../data/alfvenwave-data')
z_path = data_dir / 'x3.npy'
if not z_path.exists():
    raise SystemExit(f"❌ No se encontró {z_path}. Asegúrate de que la carpeta 'data/alfvenwave-data/' esté en el directorio raíz del proyecto.")

z = np.load(z_path)

# Descubrir tiempos disponibles
time_candidates = []
for base in ('vx1', 'bx1', 'bx3'):
    time_candidates += discover_times(str(data_dir / f'{base}_*.npy'))

times = sorted(set(time_candidates))
if not times:
    raise SystemExit("❌ No se encontraron archivos *_*.npy en 'data/alfvenwave-data/' (vx1, bx1 o bx3).")

# Cargar series de datos
Bx_series = []
Bz_series = []
vx_series = []

for t in times:
    bx1 = data_dir / f'bx1_{t:02d}.npy'
    if bx1.exists():
        Bx_series.append(np.load(bx1))
    bz3 = data_dir / f'bx3_{t:02d}.npy'
    if bz3.exists():
        Bz_series.append(np.load(bz3))
    vx1 = data_dir / f'vx1_{t:02d}.npy'
    if vx1.exists():
        vx_series.append(np.load(vx1))

# Rangos según requisitos del ejercicio
Bx_ylim = (-1.0, 1.0)  # fijo
Bz_ylim = fixed_ylim_from_series(Bz_series, pad_frac=0.05)
vx_ylim = (-1.0, 1.0)  # fijo 

# ---------- Tarea 1: Videos de Bx(z), Bz(z), vx(z) ----------
def make_frames_and_video(varname, series_name, ylim):
    frames_dir = Path(f'../results/problema2/frames_{varname}')
    ensure_dir(frames_dir)

    print(f"✨ Generando fotogramas para {varname}...")
    for t in times:
        fpath = data_dir / f'{series_name}_{t:02d}.npy'
        if not fpath.exists():
            continue
        y = np.load(fpath)
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(z, y, lw=2)
        ax.set_title(f"{varname}(z) — t = {t}")
        ax.set_xlabel("z (u.l.)")
        ax.set_ylabel(varname + " (u.)")
        ax.set_ylim(*ylim)
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(frames_dir / f'{t:02d}.png', dpi=180)
        plt.close(fig)

    print(f"✨ Creando video MP4 y GIF para {varname}...")
    mp4_ok, gif_ok = create_video_and_gif(
        frames_dir=frames_dir,
        output_base=f'../results/problema2/{varname}',
        fps=10,
        file_pattern='%0{width}d.png'
    )

make_frames_and_video('Bx', 'bx1', Bx_ylim)
make_frames_and_video('Bz', 'bx3', Bz_ylim)
make_frames_and_video('vx', 'vx1', vx_ylim)

# ---------- Tarea 3: Verificación de By y vy (deberían ser ≈ 0) ----------
t_check = times[len(times)//2]
by_path = data_dir / f'bx2_{t_check:02d}.npy'
vy_path = data_dir / f'vx2_{t_check:02d}.npy'
if by_path.exists() or vy_path.exists():
    fig, ax = plt.subplots(figsize=(7, 4))
    if by_path.exists():
        by = np.load(by_path)
        ax.plot(z, by, lw=2, label='By')
    if vy_path.exists():
        vy = np.load(vy_path)
        ax.plot(z, vy, lw=2, label='vy')
    ax.set_title(f"By y vy — t = {t_check} (deberían ser ≈ 0)")
    ax.set_xlabel("z (u.l.)")
    ax.set_ylabel("magnitud (u.)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(f'../results/problema2/by_vy_t{t_check:02d}.png', dpi=180)
    plt.close(fig)

# ---------- Tarea 4: Condiciones iniciales y velocidad de Alfvén ----------
summary_lines = []
rho0 = None
B0 = None
rho0_path = data_dir / 'rho_00.npy'
bz0_path = data_dir / 'bx3_00.npy'
if rho0_path.exists():
    rho_init = np.load(rho0_path)
    rho0 = float(np.mean(rho_init))
    # Gráfica de densidad inicial
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(z, rho_init, lw=2)
    ax.set_title(r'$\rho(z)$ en $t=0$')
    ax.set_xlabel("z (u.l.)")
    ax.set_ylabel("ρ (u.)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('../results/problema2/rho_t00.png', dpi=180)
    plt.close(fig)
    summary_lines.append(f" - rho0 (promedio en t=0) = {rho0:.6g}")
if bz0_path.exists():
    bz_init = np.load(bz0_path)
    B0 = float(np.mean(bz_init))
    # Gráfica de campo magnético inicial
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(z, bz_init, lw=2)
    ax.axhline(B0, ls='--', alpha=0.6, label=f'B0 ≈ {B0:.3g} (promedio)')
    ax.set_title(r'$B_z(z)$ en $t=0$ (se espera $B_0 \approx 1$)')
    ax.set_xlabel("z (u.l.)")
    ax.set_ylabel("Bz (u.)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig('../results/problema2/bz_t00.png', dpi=180)
    plt.close(fig)
    summary_lines.append(f" - B0 (promedio de Bz en t=0) = {B0:.6g}")

if (rho0 is not None) and (B0 is not None):
    vA = B0 / math.sqrt(rho0)  # Factor 1/sqrt(4π) absorbido en unidades de PLUTO
    summary_lines.append(f" - v_A = B0 / sqrt(rho0) = {vA:.6g}")
else:
    vA = None

# ---------- Tarea 5: Análisis de amplitud y régimen Alfvénico ----------
amp_by_time = []
for t in times:
    fp = data_dir / f'vx1_{t:02d}.npy'
    if not fp.exists():
        continue
    v = np.load(fp)
    # Calcular amplitud de perturbación
    A = 0.5 * (float(np.max(v)) - float(np.min(v)))
    Aabs = float(np.max(np.abs(v)))
    amp_by_time.append((t, A, Aabs))

if amp_by_time:
    ts = [t for (t, A, Aabs) in amp_by_time]
    Avals = [A for (t, A, Aabs) in amp_by_time]
    Aabsvals = [Aabs for (t, A, Aabs) in amp_by_time]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(ts, Avals, lw=2, marker='o')
    ax.set_title("Amplitud (max-min)/2 de vx por tiempo")
    ax.set_xlabel("t (índice)")
    ax.set_ylabel("Amplitud de vx (u.)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('../results/problema2/vx_amp_over_time.png', dpi=180)
    plt.close(fig)

    Amax = max(Aabsvals)
    summary_lines.append(f" - Amplitud máxima |vx| observada = {Amax:.6g}")
    if vA is not None:
        MA = Amax / vA
        regime = "sub-Alfvénico (M_A < 1)" if MA < 1 else "súper-Alfvénico (M_A >= 1)"
        summary_lines.append(f" - Mach Alfvénico aproximado M_A = |vx|max / v_A = {MA:.6g} → {regime}")

# ---------- Escribir resumen ----------
if summary_lines:
    write_summary('../results/problema2/resumen.txt', summary_lines)
    print("🔥 Resumen: \n" + "\n".join(summary_lines))

print("🔥 Archivos generados en results/problema2/:")
print(" - Videos: Bx.mp4, Bz.mp4, vx.mp4 y sus respectivos GIFs")
print(" - Análisis: by_vy_tXX.png, rho_t00.png, bz_t00.png, vx_amp_over_time.png")
print(" - Resumen: resumen.txt")
