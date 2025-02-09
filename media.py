#!/usr/bin/env python3

"""Utilities to load images from files or the web."""

import urllib.request
import io

import PIL.Image
import numpy as np

def fetch_image(location: str|urllib.request.Request) -> np.ndarray:
    """Fetches an image from LOcATION as a numpy ndarray."""
    url = location
    if not (isinstance(location, urllib.request.Request) or location.startswith("http")):
        url = "file:" + urllib.request.pathname2url(location)
    print("url is", url)
    with urllib.request.urlopen(url) as http_response:
        image_bytes = http_response.read()
        image_io = io.BytesIO(image_bytes)
        image_pil = PIL.Image.open(image_io)
        return np.asarray(image_pil)

