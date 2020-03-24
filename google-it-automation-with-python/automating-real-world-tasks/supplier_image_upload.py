#!/usr/bin/env python3
import requests
import os

url = "http://[linux-server-ip]/upload/"
dir = "supplier-data/images"

if __name__ == '__main__':
    files = [files for file in os.listdir(dir) if file.endswith('.jpeg')]
    for file in files:
        path = os.path.join(dir, file)
        with open(path, 'rb') as f:
            r = requests.post(url, files={'file': f})
