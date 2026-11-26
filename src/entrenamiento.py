import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression


def entrenar_regresion_lineal(X_train, y_train):
    """Entrena el modelo base de regresión lineal."""
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    return modelo


def entrenar_random_forest(X_train, y_train, n_arboles=100, profundidad_maxima=12):
    """Entrena un Random Forest. La profundidad se limita para evitar sobreajuste."""
    modelo = RandomForestRegressor(
        n_estimators=n_arboles,
        max_depth=profundidad_maxima,
        min_samples_leaf=5,
        random_state=42,
        n_jobs=-1,
    )
    modelo.fit(X_train, y_train)
    return modelo


def guardar_modelo(modelo, ruta):
    """Guarda el modelo entrenado en disco."""
    joblib.dump(modelo, ruta, compress=3)
    print(f"Modelo guardado en {ruta}")


def cargar_modelo(ruta):
    """Carga un modelo guardado."""
    return joblib.load(ruta)
