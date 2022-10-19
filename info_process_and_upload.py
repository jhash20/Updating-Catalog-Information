#!/usr/bin/env python3

import os
import requests
import json
import re

"""
Creates script that iterates through a directory of text files, 
processes the information into a dictionary, 
and then makes POST requests to the web service endpoint, 
converting the dictionary into JSON format in the process.
"""

# initializes description directory path, escription dictionary, and url
descr_dir = '/supplier-data/descriptions/'
descr_dict = {}
url = "http://<linux-instance-external-IP>/fruits"

# iterates through directory of description text files
for item in os.listdir(descr_dir):
  # if conditional to ensure that script is only iterating text files
  if item.endswith('.txt', '.text'):
    # intializes path of text file
    item_path = str(descr_dir) + str(item)
    with open(item_path) as descr:
      # splits the item name and ext (i.e. 001, 002, 003) for image_name key value in descr_dir
      item_name, item_ext = os.path.splitext(item)
      # reads and splits text file by line, removes whitespace, and for use as key values in descr_dir
      descr_line = descr.read().split('\n')
      descr_dict['name'] = descr_line[0].strip()
      # additionally removes 'lbs' string and converts to integer
      descr_dict['weight (in lbs)'] = int(descr_line[1].replace('lbs', '').strip())
      descr_dict['description'] = descr_line[3].strip()
      #TODO: need to add value for image_name key that matches .jpeg to description text file
      descr_dict['image_name'] = str(item_name) + ".jpeg"
      # sends a POST request to the endpoint of the web service and then prints the status code of the request
      response = requests.post(url, json=descr_dict)
      print(response.status_code)
  else:
    # prints an error if the item wasn't a text file
    print("Error: Did not process: " + item + " is not a text file.")
      
      
