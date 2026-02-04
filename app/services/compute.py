import math
import numpy as np
import pandas as pd

def aggregate_metrics(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(columns=["CellId"]).agg(["mean", "std"])


def compute_row_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    a = np.sqrt(df["Nuclear Surface Area [um^2]"])
    b = np.sqrt(df["Nuclear Volume [fL]"])

    df["ncr"] = df["Nuclear Volume [fL]"] / df["Cellular Volume [fL]"]

    df["sphericity"] = (
        (math.pi ** (1/3)) *
        ((6 * df["Nuclear Volume [fL]"]) ** (2/3))
    ) / df["Nuclear Surface Area [um^2]"]

    df["vol_surface_ratio"] = (
        df["Cellular Volume [fL]"] /
        df["Cellular Surface Area [um^2]"]
    )

    df["eccentricity"] = 1 - (b / a)
    df["cell_density"] = 1 / df["Cellular Volume [fL]"]

    df["shape_factor"] = (
        4 * math.pi * df["Nuclear Surface Area [um^2]"]
    ) / (df["Cellular Surface Area [um^2]"] ** 2)

    return df[
        ["CellId",
         "ncr", "sphericity", "vol_surface_ratio",
         "eccentricity", "cell_density", "shape_factor"]
    ]
