import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def calcular_metricas(y_real, y_predicho):
    """Devuelve MAE, RMSE y R² en un diccionario."""
    mae = float(mean_absolute_error(y_real, y_predicho))
    rmse = float(np.sqrt(mean_squared_error(y_real, y_predicho)))
    r2 = float(r2_score(y_real, y_predicho))
    return {"MAE": mae, "RMSE": rmse, "R2": r2}


def comparar_modelos(resultados):
    """Convierte un diccionario {nombre: metricas} en una tabla."""
    return pd.DataFrame(resultados).T.round(3)


def graficar_real_vs_predicho(y_real, y_predicho, titulo):
    """Dispersión de valores reales contra predichos."""
    plt.figure(figsize=(6, 5))
    plt.scatter(y_real, y_predicho, alpha=0.3)
    minimo = min(y_real.min(), y_predicho.min())
    maximo = max(y_real.max(), y_predicho.max())
    plt.plot([minimo, maximo], [minimo, maximo], color="red", linestyle="--")
    plt.xlabel("Profit real")
    plt.ylabel("Profit predicho")
    plt.title(titulo)
    plt.show()


def graficar_residuos(y_real, y_predicho, titulo):
    """Histograma de los errores (real - predicho)."""
    residuos = y_real - y_predicho
    plt.figure(figsize=(6, 4))
    plt.hist(residuos, bins=60)
    plt.xlabel("Error (real - predicho)")
    plt.ylabel("Frecuencia")
    plt.title(titulo)
    plt.show()
