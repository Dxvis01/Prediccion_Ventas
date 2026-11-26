# Predicción de ganancias (Profit) con el dataset Superstore

Proyecto académico de analítica de datos. A partir del dataset *Sample - Superstore* se explora la información, se limpia y se construyen dos modelos de regresión para predecir la ganancia (`Profit`) de cada registro de venta.

**Autores:** Paula Alejandra Quemba Vega; Juan David Amaya Latorre - Ingeniería de Sistemas

## Objetivo

Identificar y justificar la variable objetivo, preparar los datos sin fuga de información y comparar un modelo base (Regresión Lineal) con un Random Forest.

## Variable objetivo

Se eligió `Profit` (regresión) por ser continua, tener sentido de negocio y relacionarse con otras variables de forma no trivial (correlación 0,48 con `Sales` y -0,22 con `Discount`). La justificación completa está en `cuadernillos/01_exploracion.ipynb`.


## Metodología

1. **Exploración:** dimensiones, tipos, nulos, duplicados, distribuciones, correlaciones y valores atípicos.
2. **Limpieza:** fechas, variables derivadas, columnas irrelevantes, `Sales_Log` para reducir la asimetría de las ventas y One-Hot Encoding.
3. **Separación:** 80% train y 20% test con `random_state=42`, agrupando por `Order ID` para que un mismo pedido no quede en ambos conjuntos.
4. **Modelamiento:** Regresión Lineal (modelo base) y Random Forest Regressor, evaluados con MAE, RMSE y R².

El Random Forest supera a la regresión lineal. Al repetir el proceso con otras separaciones train/test, el R² del Random Forest varía entre 0,50 y 0,81, porque el resultado depende de cuántos registros extremos caen en el conjunto de prueba. La conclusión de que supera al modelo lineal se mantiene en todos los casos probados.

## Limitaciones y trabajo futuro

- Los errores se concentran en los registros con ganancias o pérdidas extremas.
- No se hizo búsqueda de hiperparámetros ni validación cruzada.
- Se eliminaron `State`, `City` y datos de cliente y producto para mantener el modelo sencillo.
- Falta completar la aplicación de Streamlit (formulario y predicción).

## Dataset

*Sample - Superstore*, dataset público de ventas de una tienda de EE. UU. (2014-2017).
