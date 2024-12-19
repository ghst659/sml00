#!/usr/bin/env python3
#
# Functions to facilitate reading forecasting data.

import os
import pandas as pd

def make_prophet_frame(source: pd.DataFrame, ds_col: str, y_col: str) -> pd.DataFrame:
    """Copies the SOURCE frame's DS_COL and Y_COL columns into a new frame for Prophet.

    Prophet needs a 2-column dataframe, with headings "ds" for the time axis and "y"
    for the values to be forecast.
    """
    result = source[[ds_col, y_col]].copy()
    result.rename(columns={ds_col: "ds", y_col: "y"}, inplace=True)
    return result

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
