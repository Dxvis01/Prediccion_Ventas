import pandas as pd


def cargar_datos(ruta):
    """Carga el CSV original de Superstore (usa codificación latin-1)."""
    return pd.read_csv(ruta, encoding="latin-1")


def cargar_csv(ruta):
    """Carga un CSV ya procesado (guardado en UTF-8)."""
    return pd.read_csv(ruta)


def guardar_csv(df, ruta):
    """Guarda un DataFrame en CSV sin el índice."""
    df.to_csv(ruta, index=False)
    print(f"Archivo guardado en {ruta} con forma {df.shape}")


def mostrar_resumen(df):
    """Imprime dimensiones y tipos de datos."""
    print("Dimensiones:", df.shape)
    print(df.dtypes)
