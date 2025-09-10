#!/usr/bin/env python3
"""
🚀 Ejecutor de Simulaciones de Física Espacial

Este script ejecuta automáticamente ambas simulaciones de la tarea programada:
- Problema 1: Análisis de ondas sonoras con condiciones de frontera reflectivas
- Problema 2: Análisis de ondas de Alfvén en magnetohidrodinámica

Simplemente ejecuta: python run_all.py
Y obtendrás todos los resultados organizados en results/
"""
import subprocess
import sys
from pathlib import Path

def run_script(script_name):
    """Ejecuta un script de simulación y maneja cualquier error que pueda surgir"""
    print(f"\n{'='*50}")
    print(f"👀 Ejecutando {script_name}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              cwd='src', 
                              check=True, 
                              capture_output=False)
        print(f"🤍 {script_name}, Listo!!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando {script_name}: {e}")
        return False
    except FileNotFoundError:
        print(f"❌ No se encontró {script_name}")
        return False


def main():
    """Ejecuta todas las simulaciones de la tarea programada"""
    print("🚀 Iniciando simulaciones de Física Espacial - Tarea Programada I")
    print("👀 Verificando que los datos estén en data/...")
    
    scripts = [
        'solucion_problema1.py',
        'solucion_problema2.py',
        'generar_resumen_problema1.py',
        'generar_resumen_problema2.py'
    ]
    
    success_count = 0
    for script in scripts:
        if run_script(script):
            success_count += 1
    
    print(f"\n{'='*50}")
    print(f"🤍 Resumen: {success_count}/{len(scripts)} simulaciones completadas")
    print(f"👀 Resultados en results/")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
