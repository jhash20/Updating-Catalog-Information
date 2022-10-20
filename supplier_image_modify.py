#!/usr/bin/env python3

import os, sys
from PIL import Image

"""
Script to reformat images:
from: .TIFF format with image resolution 3000x2000
to: .JPEG format with image resolution 600x400
""""

# changes to directory path containing images to be modified
dir_path = os.path.expandusr('~') + '/supplier-data/images/'
os.chdir(dir_path)

# iterates through files in directory
for root, dirs, files in os.walk("."):
  for file in files:
    # ensures only .tiff files are being iterated on since .jpegs are being saved in same path
    if file.endswith(".tiff"):
      # splits file name and ext
      f, e = os.path.splitext(file)
      # joins directory path and file name to create new and old file paths
      old_file_path = str(dir_path + file)
      new_file_path = os.path.join(dir_path, f)
      # reformats images to specified format and image resolution and saves in the same path
      try:
        with Image.open(old_file_path) as im:
          new_im = im.convert('RGB')
          new_im = new_im.resize((600,400))
          new_im = new_im.save(new_file_path + ".jpeg")
      # prints an exception if unable to convert file and file name
      except (IOError, OSError):
        print('Cannot convert: ' + str(f))
