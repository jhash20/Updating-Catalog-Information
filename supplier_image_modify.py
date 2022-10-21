#!/usr/bin/env python3

"""Script that reformats images:
from: .TIFF format with image resolution 3000x2000
to: .JPEG format with image resolution 600x400
"""

import os, sys
from PIL import Image


dir_path = os.path.expanduser("~") + "/supplier-data/images/"
os.chdir(dir_path)

# iterates through files in directory
for root, dirs, files in os.walk("."):
  for file in files:
    # ensures only .tiff files being iterated (.jpegs saved in same path)
    if file.endswith(".tiff"):
      # splits file name and ext
      f, e = os.path.splitext(file)
      
      old_file_path = str(dir_path + file)
      new_file_path = os.path.join(dir_path, f)
      # converts images to specifications and saves in same path
      try:
        with Image.open(old_file_path) as im:
          new_im = im.convert("RGB")
          new_im = new_im.resize((600,400))
          new_im = new_im.save(new_file_path + ".jpeg")
      except (IOError, OSError):
        print("Cannot convert: " + str(f))
