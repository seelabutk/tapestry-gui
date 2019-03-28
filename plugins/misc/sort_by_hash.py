#!/usr/bin/env python

import os
import sys
import imagehash
import glob
from PIL import Image
from shutil import copyfile

if __name__ == '__main__':
    path = '../data/*.png'
    hashes = []
    filenames = []
    for f in glob.glob(path):
        with open(f) as _file:
            img = Image.open(_file)
            hashes.append((f, imagehash.phash(img, hash_size=64, highfreq_factor=32)))

    hashes = sorted(hashes, key = lambda x: x[1])

    i = 0
    for el in hashes:
        filename = os.path.basename(el[0])
        copyfile(el[0], "temp/" + str(i).zfill(5) + ".png")
        i += 1
    


    
