import pandas as pd


def is_categorical(*series: pd.Series) -> bool:
    for s in series:
        if s.dtype in ["object", "bool"]:
            return True

    return False
