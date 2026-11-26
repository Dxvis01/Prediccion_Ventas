# Despliegue (Streamlit)

Base para la aplicación web. Por ahora solo carga el modelo entrenado.

## Contenido

- `app.py`: aplicación de Streamlit.
- `modelo/modelo_random_forest.joblib`: modelo entrenado (se genera en `cuadernillos/03_modelamiento/02_modelamiento.ipynb`).
- `modelo/columnas_modelo.json`: lista de columnas que espera el modelo, en el mismo orden del entrenamiento.

## Ejecutar

Desde la raíz del proyecto:

```bash
streamlit run despliegue/app.py
```

## Pendiente

- Formulario para ingresar Sales, Discount, Quantity, categoría, etc.
- Aplicar la misma transformación de los datos (`Sales_Log`, codificación) antes de predecir.
- Mostrar el Profit predicho.
