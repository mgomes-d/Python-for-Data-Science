import pandas as pd
import numpy as np


def load(path: str) -> pd.DataFrame:
    """read the csv file"""
    try:
        assert path.lower().endswith(".csv"), "Path in wrong format, .csv"
        df = pd.read_csv(path)
        return df
    except FileNotFoundError as msg:
        print(msg)
        return None
    except pd.errors.EmptyDataError as msg:
        print(msg)
        return None
    except AssertionError as msg:
        print("AssertionError:", msg)
        return None
