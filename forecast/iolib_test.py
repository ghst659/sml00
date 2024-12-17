#!/usr/bin/env python3

import numpy as np
import pandas as pd
import pathlib
import tempfile
import textwrap
import unittest

import iolib

class TestReadNasdaq(unittest.TestCase):

    def test_baseline(self):
        CSV_TEXT = textwrap.dedent("""\
        Date,Close/Last,Volume,Open,High,Low
        12/13/2024,$191.38,18883220,$192.71,$194.34,$191.26
        12/12/2024,$193.63,25197760,$196.30,$196.7053,$193.28
        """)
        with tempfile.NamedTemporaryFile(delete=True, delete_on_close=False) as csv:
            csv_path = pathlib.Path(csv.name)
            csv_path.write_text(CSV_TEXT)
            got_frame = iolib.read_nasdaq(csv_path)
        pd.testing.assert_frame_equal(got_frame, pd.DataFrame({
            "Date": [np.datetime64("2024-12-13"), np.datetime64("2024-12-12")],
            "Close/Last": [191.38, 193.63],
            "Volume": [18883220, 25197760],
            "Open": [192.71, 196.30],
            "High": [194.34, 196.7053],
            "Low": [191.26, 193.28]
        }))

if __name__ == "__main__":
    unittest.main()
