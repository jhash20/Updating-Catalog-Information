#!/usr/bin/env python3

import os
import requests
import json
import re

"""Script that iterates through a directory of text files, 
processes the information into a dictionary, 
and then makes POST requests to the web service endpoint, 
converting the dictionary into JSON format in the process.
"""

descr_dir = os.path.expanduser("~") + "/supplier-data/descriptions/"
descr_dict = {}
url = "http://<linux-instance-external-IP>/fruits/"

# iterates through directory of description text files
for item in os.listdir(descr_dir):
  # ensures that script is only iterating text files
  if item.endswith(".txt"):
    # splits the item name and ext (i.e. 001, 002, 003)
    item_name, item_ext = os.path.splitext(item)
    item_path = str(descr_dir) + str(item)
    
    # opens, reads, and splits files and sets strings as values for dictionary
    with open(item_path) as descr:
      descr_line = descr.read().split("\n")
      descr_dict['name'] = descr_line[0].strip()
      descr_dict['weight'] = int(descr_line[1].replace("lbs", "").strip())
      descr_dict['description'] = descr_line[2].strip()
      # uses "item_name + .jpeg" value so Django app can pair descr-img in catalog
      descr_dict['image_name'] = str(item_name) + ".jpeg"
      
      # sends a POST request and prints the status code of the request
      response = requests.post(url, json=descr_dict)
      print(response.status_code)
  else:
    print("Error: Did not process: " + item + " is not a text file.")
      
      
