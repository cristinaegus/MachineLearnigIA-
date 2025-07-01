#!/usr/bin/env python3
"""
Script para convertir notebook a PDF
"""
import subprocess
import sys
import os

def convert_notebook_to_pdf():
    """Convierte el notebook a PDF usando diferentes métodos"""
    
    notebook_file = "01 Regresión (Uni y Multivariante) (Hormigón).ipynb"
    output_file = "Analisis_Regresion_Hormigon.pdf"
    
    # Método 1: Intentar con webpdf
    try:
        print("🔄 Intentando conversión con webpdf...")
        result = subprocess.run([
            sys.executable, "-m", "nbconvert", 
            notebook_file, 
            "--to", "webpdf", 
            "--output", output_file
        ], capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print("✅ ¡Conversión exitosa con webpdf!")
            print(f"📄 Archivo creado: {output_file}")
            return True
        else:
            print(f"❌ Error con webpdf: {result.stderr}")
    except Exception as e:
        print(f"❌ Excepción con webpdf: {e}")
    
    # Método 2: Intentar con LaTeX
    try:
        print("🔄 Intentando conversión con LaTeX...")
        result = subprocess.run([
            sys.executable, "-m", "nbconvert", 
            notebook_file, 
            "--to", "pdf", 
            "--output", output_file
        ], capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print("✅ ¡Conversión exitosa con LaTeX!")
            print(f"📄 Archivo creado: {output_file}")
            return True
        else:
            print(f"❌ Error con LaTeX: {result.stderr}")
    except Exception as e:
        print(f"❌ Excepción con LaTeX: {e}")
    
    print("ℹ️  No se pudo crear PDF directamente.")
    print("💡 Alternativas disponibles:")
    print("   1. Archivo HTML creado: Analisis_Regresion_Hormigon.html")
    print("      - Abrelo en Chrome y usa 'Imprimir > Guardar como PDF'")
    print("   2. Desde VS Code: Ctrl+Shift+P > 'Notebook: Export to Format' > PDF")
    
    return False

if __name__ == "__main__":
    convert_notebook_to_pdf()
