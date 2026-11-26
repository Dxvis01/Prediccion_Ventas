import numpy as np
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit


def crear_variables_derivadas(df):
    """Crea variables simples a partir de las fechas y de Sales.

    No se usa Profit para crear variables, para evitar fuga de datos.
    """
    df = df.copy()
    df["Anio_Pedido"] = df["Order Date"].dt.year
    df["Mes_Pedido"] = df["Order Date"].dt.month
    df["Dia_Semana_Pedido"] = df["Order Date"].dt.dayofweek
    df["Dias_Envio"] = (df["Ship Date"] - df["Order Date"]).dt.days
    df["Sales_Log"] = np.log1p(df["Sales"])
    return df


def separar_train_test(df, columna_grupo="Order ID", tamanio_test=0.2, semilla=42):
    """Separa en train y test sin mezclar filas de un mismo pedido."""
    separador = GroupShuffleSplit(n_splits=1, test_size=tamanio_test, random_state=semilla)
    indices_train, indices_test = next(separador.split(df, groups=df[columna_grupo]))
    return df.iloc[indices_train].copy(), df.iloc[indices_test].copy()


def codificar_categoricas(train, test, columnas_categoricas):
    """Aplica One-Hot Encoding. Las columnas se definen con train
    y test se ajusta a ellas (así no se usa información de test)."""
    train_cod = pd.get_dummies(train, columns=columnas_categoricas, dtype=int)
    test_cod = pd.get_dummies(test, columns=columnas_categoricas, dtype=int)
    test_cod = test_cod.reindex(columns=train_cod.columns, fill_value=0)
    return train_cod, test_cod


def separar_x_y(df, columna_objetivo="Profit", columnas_extra_a_quitar=None):
    """Separa las variables predictoras (X) de la variable objetivo (y)."""
    quitar = [columna_objetivo] + (columnas_extra_a_quitar or [])
    X = df.drop(columns=quitar)
    y = df[columna_objetivo]
    return X, y
