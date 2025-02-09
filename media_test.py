#!/usr/bin/env python3

import logging
import pathlib
import tempfile
import unittest
import urllib

import numpy as np

import media

class GetImageTest(unittest.TestCase):

    ROSE = "https://upload.wikimedia.org/wikipedia/commons/d/d7/Red_rose_with_black_background.jpg"

    def test_url(self):
        img = media.fetch_image(self.ROSE)
        self.assertEqual(img.shape, (2365, 3077, 3))

    def test_request(self):
        req = urllib.request.Request(self.ROSE)
        img = media.fetch_image(req)
        self.assertEqual(img.shape, (2365, 3077, 3))

    def test_file(self):
        with tempfile.NamedTemporaryFile(delete_on_close=False) as tmp:
            with urllib.request.urlopen(self.ROSE) as http_response:
                image_bytes = http_response.read()
                tmp.write(image_bytes)
                tmp.close()
            read_image = media.fetch_image(tmp.name)
            self.assertEqual(read_image.shape, (2365, 3077, 3))

if __name__ == "__main__":
    unittest.main()
