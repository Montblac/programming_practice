#!/usr/bin/env python3
from PIL import Image
import os

if __name__ == '__main__':
    dir = 'supplier-data/images'
    size = (600,400)
    format = 'JPEG'

    files = [file for file in os.listdir(dir) if file.endswith('.tiff')]
    for file in files:
        base = os.path.splitext(file)[0]
        path = os.path.join(dir, file)
        out = os.path.join(dir, base) + '.jpeg'
        with Image.open(path) as im:
            im = im.resize(size)
            im = im.save(out, format)
