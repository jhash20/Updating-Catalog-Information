#!/usr/bin/env python3

"""
Script that processes text files in a directory and 
generates a report and sends it to supplier via email, 
detailing the type and amount of each fruit uploaded to catalog.
"""

# imports necessary modules
import os, sys
import datetime
from report_generator import generate as pdf_generate
from report_emailer import generate as email_generate
from report_emailer import send as email_send

def generate_info(dir_path):
  """Generates info string with newlines in correct format for pdf BodyText."""
  # initalizes list to store each item string 
  info_list = []
  # iterates through directory of text files passed by main() 
  for item in os.listdir(dir_path):
    # conditional ensures that files iterated are text files
    if item.endswith(".txt", ".text"):
      # initializes full item path to be opened
      item_path = str(dir_path) + str(item)
      with open(item_path) as info:
        # splits info in item into lines and then strips whitespace/makes string
        info_line = info.read().split('\n')
        name = str(info_line[0].strip())
        weight = str(info_line[1].strip())
        newline = '<br/>'
        # adds specified lines and newline symbols into one string
        newstring = name + newline + weight + newline + newline
        # appends strings to list
        info_list.append(newstring)
  # joins list into one string and then returns string to main()
  info_string = info_list.join()
  return info_string

def main(argv):
  """Processes directory of text files, generates a pdf, and sends pdf via email."""
  # gets today's date in GMT time (default) to be used for title of report pdf
  current_date = datetime.datetime.now()
  # initializes directory path to generate info to be used for info of report pdf
  dir_path = "/supplier_data/descriptions/"
  # initializes arguments to be passed to pdf_generate()
  title = "Processed Update on " + str(current_date)
  info = generate_info(dir_path)
  pdf_path = "/tmp/processed.pdf"
  # generates pdf report
  pdf_generate(pdf_path, title, info)
  # intializes arguments to be passed to email_generate()
  sender = "automation@example.com"
  recipient = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  body =  "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
  attachment_path = pdf_path
  # generates and sends email with pdf attachment
  message = email_generate(sender, recipient, subject, body, attachment_path)
  email_send(message)
  
if __name__ == "__main__":
  main(sys.argv)
