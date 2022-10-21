#!/usr/bin/env python3

"""Script that uploads images to web service endpoint
by iterating through directory of .jpeg files and making a POST request.
Also prints a response status code
"""

import os, sys
import requests

dir_path = os.path.expanduser('~') + '/supplier-data/images/'
os.chdir(dir_path)

url = "http://localhost/upload/"

# iterates through directory of images and uploads them
for file in os.listdir(dir_path):
  # ensures that files iterated are .jpeg files
  if file.endswith(".jpeg"):
    file_path = str(dir_path) + str(file)
    with open(file_path, "rb") as opened:
      response = requests.post(url, files={"file": opened})
      print(response.status_code)
  else:
    print("Error: Did not process, " + file + " is not a .jpeg")
