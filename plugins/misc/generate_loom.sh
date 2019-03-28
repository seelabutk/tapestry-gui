#!/bin/bash

#ffmpeg -framerate 30 -i ../data/around_%05d.png -s:v 512x512 -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p ../data/loom.mp4
ffmpeg -framerate 30 -i temp/%05d.png -s:v 512x512 -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p temp/loom.mp4
