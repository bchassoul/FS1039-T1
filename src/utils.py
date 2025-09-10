#!/usr/bin/env python3
"""
🛠️ Utilidades

Funciones auxiliares compartidas entre los scripts de simulación.
"""
import re
import glob
import subprocess
import shutil
from pathlib import Path


def clean_results_directory(problem_name):
    """
    Limpia los resultados anteriores de un problema específico.
    
    Args:
        problem_name (str): Nombre del problema ('problema1' o 'problema2')
    """
    results_dir = Path(f'../results/{problem_name}')
    if results_dir.exists():
        print(f"✨ Limpiando resultados anteriores del {problem_name.title()}...")
        shutil.rmtree(results_dir)
        print("✨ Resultados anteriores eliminados")
    else:
        print(f"✨ No hay resultados del {problem_name.title()} para limpiar")
    
    # Crear directorio vacío
    results_dir.mkdir(parents=True, exist_ok=True)


def discover_times(pattern):
    """Descubre los tiempos disponibles en archivos de simulación PLUTO"""
    times = []
    rx = re.compile(r'_(\d+)\.npy$')
    for fp in glob.glob(pattern):
        m = rx.search(fp)
        if m:
            times.append(int(m.group(1)))
    return sorted(set(times))


def ensure_dir(d):
    """Crea un directorio si no existe"""
    Path(d).mkdir(parents=True, exist_ok=True)


def try_ffmpeg(frames_dir, width, output='output.mp4', fps=10, file_pattern='%0{width}d.png'):
    """
    Intenta crear un video usando ffmpeg
    
    Args:
        frames_dir: Directorio con los frames
        width: Ancho del número de frame (ej: 2 para 01, 02, etc.)
        output: Archivo de salida
        fps: Frames por segundo
        file_pattern: Patrón de archivos (ej: '%0{width}d.png' o 'density_%0{width}d.png')
    """
    pattern = str(Path(frames_dir) / file_pattern.format(width=width))
    cmd = ['ffmpeg', '-y', '-framerate', str(fps), '-i', pattern,
           '-vf', 'format=yuv420p', output]
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


def save_gif_with_pillow(frames_dir, output='output.gif', fps=10, file_pattern='*.png'):
    """
    Crea un GIF usando Pillow como fallback
    
    Args:
        frames_dir: Directorio con los frames
        output: Archivo de salida
        fps: Frames por segundo
        file_pattern: Patrón de archivos (ej: '*.png' o 'density_*.png')
    """
    try:
        from PIL import Image
    except ImportError:
        print("Pillow no está instalado; no se puede crear GIF.")
        return False
    frames = sorted(Path(frames_dir).glob(file_pattern))
    if not frames:
        return False
    images = [Image.open(fp).convert('P', palette=Image.ADAPTIVE) for fp in frames]
    duration_ms = int(1000 / fps)
    images[0].save(output, save_all=True, append_images=images[1:], loop=0, 
                   duration=duration_ms, optimize=False)
    return True


def create_video_and_gif(frames_dir, output_base, fps=10, file_pattern='%0{width}d.png', width=None):
    """
    Crea tanto un video MP4 como un GIF a partir de los frames
    
    Args:
        frames_dir: Directorio con los frames
        output_base: Nombre base del archivo (sin extensión)
        fps: Frames por segundo
        file_pattern: Patrón de archivos para ffmpeg (ej: '%0{width}d.png' o 'density_%0{width}d.png')
        width: Ancho del número de frame (se calcula automáticamente si no se proporciona)
    
    Returns:
        tuple: (mp4_success, gif_success)
    """
    frames_dir = Path(frames_dir)
    
    # Calcular width automáticamente si no se proporciona
    if width is None:
        frames = sorted(frames_dir.glob('*.png'))
        if frames:
            # Extraer números de los nombres de archivo
            import re
            numbers = []
            for frame in frames:
                match = re.search(r'(\d+)\.png$', frame.name)
                if match:
                    numbers.append(int(match.group(1)))
            if numbers:
                width = max(2, len(str(max(numbers))))
            else:
                width = 2
        else:
            width = 2
    
    # Crear archivos de salida
    mp4_output = f"{output_base}.mp4"
    gif_output = f"{output_base}.gif"
    
    # Intentar crear MP4 con ffmpeg
    mp4_success = try_ffmpeg(frames_dir, width, output=mp4_output, fps=fps, file_pattern=file_pattern)
    if mp4_success:
        print(f"✨ Video creado: {mp4_output}")
    else:
        print(f"❌ No se pudo crear video: {mp4_output}")
    
    # Crear GIF con Pillow
    gif_pattern = '*.png' if '%' not in file_pattern else '*.png'
    gif_success = save_gif_with_pillow(frames_dir, output=gif_output, fps=fps, file_pattern=gif_pattern)
    if gif_success:
        print(f"✨ GIF creado: {gif_output}")
    else:
        print(f"❌ No se pudo crear GIF: {gif_output}")
    
    return mp4_success, gif_success
