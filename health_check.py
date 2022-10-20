#!/usr/bin/env python3

import os, sys
import psutil
import shutil
import socket
from report_emailer import generate as email_generate
from report_emailer import send as email_send

"""
Script that runs checks 
for cpu usage, disk space usage, memory usage, and hostname
and then sends an email alert if check fails
"""

def check_cpu_usage():
  """Checks if cpu usage is over 80%"""
  cpu_usage = psutil.cpu_percent(4) 
  if int(cpu_usage) > 80:
    case = "CPU usage is over 80%"
    email_alert(case)

def check_free_disk_space(disk):
  """Checks if available disk space is less than 20%"""
  disk_usage = shutil.disk_usage(disk)
  disk_available = int(disk_usage.free/disk_usage.total) * 100
  if disk_available < 20:
    case = "Available disk space is less than 20%"
    email_alert(case)
      
def check_available_memory():
  """Checks if available memory is less than 500MB"""
  memory = psutil.virutal_memory()
  # converts memory available to MB
  memory_available = int(memory.available) / 1024 ** 2 
  if memory_available < 500:
    case = "Available memory is less than 500MB"
    email_alert(case)
  
def check_hostname(hostname, ip_address):
  """Checks if the hostname cannot be resolved to IP address"""
  try:
    socket.gethostbyname(hostname)
    if socket.gethostbyname(hostname) != ip_address:
      case = "localhost cannot be resolved"
      email_alert(case)
  except socket.error:
    case = "localhost cannot be resolved"
    email_alert(case)

def email_alert(case):  
  """Generates and sends an email alert with error case if any check fails"""
  sender = "automation@example.com"
  recipient = "{}@example.com".format(os.environ["USER"])
  subject = "Error - {}".format(case)
  body = "Please check your system and resolve the issue as soon as possible."
  message = email_generate(sender, recipient, subject, body)
  email_send(message)

def main(argv):
  """Runs checks for cpu usage, disk space usage, memory usage, and hostname""""
  check_cpu_usage()
  check_free_disk_space("/")
  check_available_memory()
  check_hostname('localhost', '127.0.0.1')
  
if __name__ == "__main__":
  main(sys.argv)
