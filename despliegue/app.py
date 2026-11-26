import json
import sys
from pathlib import Path

import streamlit as st

# Permite importar la carpeta src desde despliegue/
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.append(str(RAIZ_PROYECTO))

from src.entrenamiento import cargar_modelo

CARPETA_MODELO = Path(__file__).resolve().parent / "modelo"


@st.cache_resource
def cargar_modelo_entrenado():
    modelo = cargar_modelo(CARPETA_MODELO / "modelo_random_forest.joblib")
    with open(CARPETA_MODELO / "columnas_modelo.json", encoding="utf-8") as archivo:
        columnas = json.load(archivo)
    return modelo, columnas


st.title("Predicción de Profit - Superstore")
st.write("Base de la aplicación. Por ahora solo se carga el modelo entrenado.")

modelo, columnas = cargar_modelo_entrenado()
st.success("Modelo Random Forest cargado correctamente.")
st.write(f"El modelo espera {len(columnas)} variables de entrada.")

# Pendiente: formulario de entrada y predicción
