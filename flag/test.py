import itertools
import os
from glob import glob
from os.path import basename

from PIL import Image

data = {}

for file in sorted(glob('./*.dat'), reverse=True):
    with open(file, 'rb') as f:
        data[basename(file)] = f.read()

start = data['flagpart-30225.dat']
del data['flagpart-30225.dat']

permutations = list(itertools.permutations(data.keys()))

def is_image_corrupt(file_path):
    try:
        # Try opening the image
        with Image.open(file_path) as img:
            # Attempt to load the image data
            img.verify()  # Will not load the entire image but checks file integrity
        return False  # If no exception is raised, the image is not corrupt
    except (IOError, SyntaxError) as e:
        # If an IOError or SyntaxError is raised, the image is corrupt or invalid
        return True


for idx, permutation in enumerate(permutations):
    try:
        os.remove("data.png")
    except FileNotFoundError:
        pass

    inner_data = start
    for k in permutation:
        inner_data += data[k]

    with open(f'./data.png', 'wb') as f:
        f.write(inner_data)

    if is_image_corrupt('data.png'):
        continue
    exit(1)