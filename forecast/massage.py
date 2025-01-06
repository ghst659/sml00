#!/usr/bin/env python3
"""Functions/classes for data preparation."""

import numpy as np
import pandas as pd

def assign_values(frame: pd.DataFrame, new_values: np.ndarray) -> pd.DataFrame:
    result = frame.copy()
    c = 0
    for col in result:
        result[col] = new_values[:, c]
        c += 1
    return result
    
