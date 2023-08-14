import pandas as pd


def is_categorical(series: pd.Series) -> bool:
    return series.dtype in ["object", "bool"]
