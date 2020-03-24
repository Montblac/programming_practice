#! /usr/bin/env python3

import os
import requests

src = '/data/feedback'
dest = 'http://[linux-server-ip]/feedback/'
filenames = os.listdir(src)

for filename in filenames:
    filename = os.path.join(src, filename)
    with open(filename) as fn:
        keys = ['title', 'name', 'date', 'feedback']
        lines = fn.read().splitlines()
        p = dict(zip(keys, lines))

        response = requests.post(dest, data=p)
        response.raise_for_status()
