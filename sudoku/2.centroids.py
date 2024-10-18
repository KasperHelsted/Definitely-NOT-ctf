import json
import os
from glob import glob
from os.path import basename

folders = os.listdir('./solution/')

boards = {}

for folder in folders:
    for file in glob(f'./solution/{folder}/*.json'):
        with open(file, 'r') as f:
            data = json.load(f)

            centroid = []

            for i in range(3, 6):
                centroid.append(data[i][3:6])

            if folder not in boards:
                boards[folder] = {}
            boards[folder][basename(file)] = centroid

with open('centroids.json', 'w') as f:
    json.dump(boards, f)
