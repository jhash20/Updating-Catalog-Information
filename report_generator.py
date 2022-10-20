#!/usr/bin/env python3

"""
Module that generates pdf report 
"""

from reportlabs.platypus import getSampleStyleSheet
from reportlabs.platypus import SimpleDocTemplate
from reportlabs.platypus import Paragraph, Spacer

def generate(filename, title, info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(info, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line])
