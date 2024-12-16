#!/usr/bin/env python3
#
# Functions to facilitate reading the NASDAQ historical data downloaded CSV files

import os
import pandas as pd
import pathlib

def read_history(csv_path: os.PathLike) -> pd.DataFrame:
    """Read the CSV_PATH file, parsing the columns."""
    data_frame = pd.read_csv(csv_path,
                             parse_dates=["Date"],
                             converters={
                                 c: dollar_to_float for c in ("Close/Last", "Open", "High", "Low")
                             })
    return data_frame

def dollar_to_float(dollar_text: str) -> float | str:
    if isinstance(dollar_text, str):
        return float(dollar_text.replace("$", ""))
    return dollar_text

                
