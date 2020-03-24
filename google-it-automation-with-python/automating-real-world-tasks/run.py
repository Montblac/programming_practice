#!/usr/bin/env python3
import os
import requests

dir = 'supplier-data/descriptions/'
url = "http://[linux-server-ip]/fruits/"

def formatData(image_name, name, weight, desc):
    return {
        "image_name": image_name,
        "name": name,
        "weight": weight,
        "description": desc
    }

if __name__ == '__main__':
    files = os.listdir(dir)
    for file in files:
        path = os.path.join(dir, file)
        with open(path) as f:
            content = [line.strip() for line in f if line.strip()]
            name, weight, desc = content
            weight = int(weight.split()[0])

            image_name = os.path.splitext(file)[0] + '.jpeg'
            data = formatData(image_name, name, weight, desc)
            requests.post(url, json=data)
