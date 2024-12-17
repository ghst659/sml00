#!/usr/bin/env python3
#
# Functions to facilitate reading forecasting data.

import os
import pandas as pd

def read_nasdaq(csv_path: os.PathLike) -> pd.DataFrame:
    """Read a nasdaq historical data CSV_PATH file, returning a DataFrame."""
    data_frame = pd.read_csv(csv_path,
                             parse_dates=["Date"],
                             converters={
                                 c: _dollar_to_float
                                 for c in ("Close/Last", "Open", "High", "Low")
                             })
    return data_frame

def _dollar_to_float(cell_text: str) -> float | str:
    """Converts CELL_TEXT value like "$125.23" to the float value 125.23."""
    if isinstance(cell_text, str):
        return float(cell_text.replace("$", ""))
    return cell_text
