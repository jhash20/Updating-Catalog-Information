#!/usr/bin/env python3

"""Generates a report and emails it
by processing text files in a directory,
generating a pdf, and sending it to supplier via email. 
The report details the type and amount of each fruit uploaded to catalog.
"""

import os, sys
import datetime
from report_generator import generate as pdf_generate
from report_emailer import generate as email_generate
from report_emailer import send as email_send

def generate_info(dir_path):
  """Processes info from text files in directory into string with correct format for pdf's BodyText."""
  info_list = []
  # iterates through directory of text files, reformats into string, and adds to list
  for item in os.listdir(dir_path):
    if item.endswith(".txt"):
      item_path = str(dir_path) + str(item)
      with open(item_path) as info:
        info_line = info.read().split('\n')
        name = str(info_line[0].strip())
        weight = str(info_line[1].strip())
        newline = "<br/>"
        newstring = "name: " + name + newline + "weight: " + weight + newline + newline
        info_list.append(newstring)
  # joins list into one string and then returns string to main()
  info_string = ''.join(info_list)
  return info_string

def main(argv):
  """Processes directory of text files, generates a pdf, and sends pdf via email."""  
  # gets today's date in GMT time (default) to be used for title of report pdf
  current_date = datetime.datetime.now().strftime("%B %-d, %Y")
  dir_path = os.path.expanduser('~') + "/supplier-data/descriptions/"
  
  pdf_path = "/tmp/processed.pdf"
  title = "Processed Update on " + str(current_date)
  info = generate_info(dir_path)
  pdf_generate(pdf_path, title, info)

  sender = "automation@example.com"
  recipient = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  body =  "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
  attachment_path = pdf_path

  message = email_generate(sender, recipient, subject, body, attachment_path)
  email_send(message)
  
if __name__ == "__main__":
  main(sys.argv)
