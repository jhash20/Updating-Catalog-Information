#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

"""Module for generating and sending emails"""

def generate(sender, recipient, subject, body, attachment_path):
  """Generates an email."""
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)
  
  # checks if there is an attachment. If so, attaches it
  if attachment_path != None:
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)
    with open(attachment_path, "rb") as ap:
      message.add_attachment(ap.read(), maintype = mime_type, subtype = mime_subtype, filename = attachment_filename)
      
  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP("localhost")
  mail_server.send_message(message)
  mail_server.quit()
