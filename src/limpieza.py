import pandas as pd


def convertir_fechas(df, columnas):
    """Convierte columnas de texto (mes/día/año) a tipo fecha."""
    df = df.copy()
    for columna in columnas:
        df[columna] = pd.to_datetime(df[columna], format="%m/%d/%Y")
    return df


def eliminar_duplicados(df):
    """Elimina filas completamente duplicadas e informa cuántas había."""
    cantidad = df.duplicated().sum()
    print(f"Duplicados encontrados: {cantidad}")
    return df.drop_duplicates()


def eliminar_columnas(df, columnas):
    """Elimina las columnas indicadas."""
    return df.drop(columns=columnas)


def contar_atipicos_iqr(serie):
    """Cuenta los valores fuera de 1.5 * IQR y devuelve los límites."""
    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    cantidad = ((serie < limite_inferior) | (serie > limite_superior)).sum()
    return cantidad, limite_inferior, limite_superior
