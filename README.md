# Predicción de ganancias (Profit) con el dataset Superstore

Proyecto académico de analítica de datos y Machine Learning. A partir del dataset *Sample - Superstore* se explora la información, se limpia y se construyen dos modelos de regresión para predecir la ganancia (`Profit`) de cada registro de venta.

**Autora:** Paula Quemba - Ingeniería de Sistemas

## Objetivo

Identificar y justificar la variable objetivo, preparar los datos sin fuga de información y comparar un modelo base (Regresión Lineal) con un Random Forest.

## Variable objetivo

Se eligió `Profit` (regresión) por ser continua, tener sentido de negocio y relacionarse con otras variables de forma no trivial (correlación 0,48 con `Sales` y -0,22 con `Discount`). La justificación completa está en `cuadernillos/01_exploracion.ipynb`.

## Estructura del repositorio

```
data/
├── raw/          # dataset original (no se modifica)
├── modificado/   # dataset limpio
├── train/        # datos de entrenamiento codificados
└── test/         # datos de prueba codificados
cuadernillos/
├── 01_exploracion.ipynb
├── 02_limpieza.ipynb
└── 03_modelamiento/
    ├── 01_modelamiento.ipynb   # Regresión Lineal
    └── 02_modelamiento.ipynb   # Random Forest y comparación
src/
├── carga_datos.py
├── limpieza.py
├── transformacion.py
├── entrenamiento.py
└── evaluacion.py
despliegue/       # base para la app en Streamlit y modelo entrenado
```

## Cómo ejecutar

```bash
pip install -r requirements.txt
jupyter notebook
```

Ejecutar los cuadernillos en orden: `01_exploracion`, `02_limpieza`, `03_modelamiento/01_modelamiento` y `03_modelamiento/02_modelamiento`. Para ver la base de la aplicación:

```bash
streamlit run despliegue/app.py
```

## Metodología

1. **Exploración:** dimensiones, tipos, nulos, duplicados, distribuciones, correlaciones y valores atípicos.
2. **Limpieza:** fechas, variables derivadas, columnas irrelevantes, `Sales_Log` para reducir la asimetría de las ventas y One-Hot Encoding.
3. **Separación:** 80% train y 20% test con `random_state=42`, agrupando por `Order ID` para que un mismo pedido no quede en ambos conjuntos.
4. **Modelamiento:** Regresión Lineal (modelo base) y Random Forest Regressor, evaluados con MAE, RMSE y R².

## Resultados (conjunto de prueba)

| Modelo | MAE | RMSE | R² |
|---|---|---|---|
| Regresión Lineal | 61,92 | 171,37 | 0,455 |
| Random Forest | 21,12 | 97,20 | 0,825 |

El Random Forest supera a la regresión lineal. Al repetir el proceso con otras separaciones train/test, el R² del Random Forest varía entre 0,50 y 0,81, porque el resultado depende de cuántos registros extremos caen en el conjunto de prueba. La conclusión de que supera al modelo lineal se mantiene en todos los casos probados.

## Limitaciones y trabajo futuro

- Los errores se concentran en los registros con ganancias o pérdidas extremas.
- No se hizo búsqueda de hiperparámetros ni validación cruzada.
- Se eliminaron `State`, `City` y datos de cliente y producto para mantener el modelo sencillo.
- Falta completar la aplicación de Streamlit (formulario y predicción).

## Dataset

*Sample - Superstore*, dataset público de ventas de una tienda de EE. UU. (2014-2017).
