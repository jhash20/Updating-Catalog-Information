#!/usr/bin/env python3

import os, sys
import requests

"""
Script that iterates through directory of images 
and uploads .jpeg files to web service endpoint
"""

# initializes directory path and moves to directory
dir_path = os.path.expanduser('~') + '/supplier-data/images/'
os.chdir(dir_path)
# intializes url variable
url = "http://localhost/upload/"

# iterates through directory
for file in os.listdir(dir_path):
  # sorts for .jpeg files
  if file.endswith(".jpeg"):
    file_path = str(dir_path) + str(file)
    with open(file_path, 'rb') as opened:
      # makes a POST request to web service endpoint and then prints the response status code
      response = requests.post(url, files={'file': opened})
      print(response.status_code)
  else:
    # prints an error that the script did not process file as it was not a .jpeg
    print("Error: Did not process, " + file + " is not a .jpeg")
