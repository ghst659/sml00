#!/usr/bin/env python3

import unittest

import numpy as np
import pandas as pd
import sklearn

import massage

class TestMinMaxScale(unittest.TestCase):

    def test_raw_scaling(self):
        original = np.array([[1, 2], [-3, 4], [5, 6]])
        # Create the scaler
        scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1))
        # Fit the scaler to the data and transform it
        scaled_data = scaler.fit_transform(original)  # remembers the scaling factor for the data.
        # Use inverse_transform to get back the original values
        recovered = scaler.inverse_transform(scaled_data)
        np.testing.assert_array_equal(recovered, original)
       
    def test_assign_values_roundtrip(self):
        scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1))
        indices = ["P", "Q", "R"]
        frame = pd.DataFrame({
            "A": pd.Series([1, 2, 0], index=indices),
            "B": pd.Series([-1, 0, 1], index=indices),
            "C": pd.Series([0, 1, -1], index=indices),
        }).astype("float64")
        print(f"{frame}")
        scaled = massage.assign_values(frame, scaler.fit_transform(frame))
        print(f"{scaled}")
        recovered = massage.assign_values(scaled, scaler.inverse_transform(scaled))
        print(f"{recovered}")
        pd.testing.assert_frame_equal(recovered, frame)

if __name__ == "__main__":
    unittest.main()
