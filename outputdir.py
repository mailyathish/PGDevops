# !/usr/bin/python
import csv
import datetime
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter, A4, landscape 
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
import os
from os import walk

outputDirectory = '/Users/yningapp/Documents/automation/auto/outputdir/'

data=""


def CreatePDF():

    data = list(csv.reader(csvfile))

    elements = []

    # PDF Table
    # PDF Table - Styles
    # [(start_column, start_row), (end_column, end_row)]
    all_cells = [(0, 0), (-1, -1)]
    header = [(0, 0), (-1, -1)]
    column0 = [(0, 0), (0, -1)]
    column1 = [(1, 0), (1, -1)]
    column2 = [(2, 0), (2, -1)]
    column3 = [(3, 0), (3, -1)]
    column4 = [(4, 0), (4, -1)]
    column5 = [(5, 0), (5, -1)]
    column6 = [(6, 0), (6, -1)]
    column7 = [(7, 0), (7, -1)]
    column8 = [(8, 0), (8, -1)]

    table_style = TableStyle([
        ('VALIGN', all_cells[0], all_cells[1], 'TOP'),
        ('LINEBELOW', header[0], header[1], 1, colors.black),
        ('LINEBELOW',column0[0],column1[1],1,colors.red),
        ('ALIGN', column0[0], column0[1], 'LEFT'),
        ('ALIGN', column1[0], column1[1], 'LEFT'),
        ('ALIGN', column2[0], column2[1], 'LEFT'),
        ('ALIGN', column3[0], column3[1], 'LEFT'),
        ('ALIGN', column4[0], column4[1], 'LEFT'),
        ('ALIGN', column5[0], column5[1], 'LEFT'),
        ('ALIGN', column6[0], column6[1], 'LEFT'),
        ('ALIGN', column7[0], column7[1], 'LEFT'),
        ('ALIGN', column8[0], column8[1], 'LEFT'),
    ])

    # PDF Table - Column Widths
    colWidths = [
        7 * cm,  # Column 0
        3 * cm,  # Column 1
        3 * cm,  # Column 2
        3 * cm,  # Column 3
        3 * cm,  # Column 4
        3 * cm,  # Column 5
        3 * cm,  # Column 6
        3 * cm,  # Column 7
        4 * cm,  # Column 8
    ]

    # PDF Table - Strip '[]() and add word wrap to column 5
    for index, row in enumerate(data):
        for col, val in enumerate(row):
            if col != 8 or index == 0:
                data[index][col] = val.strip("'[]()")
            else:
                data[index][col] = Paragraph(val, styles['Normal'])

    # Add table to elements
    t = Table(data, colWidths=colWidths)
    elements.append(Spacer(inch, .25 * inch))
    t.setStyle(table_style)
    elements.append(t)

    # Generate PDF
    archivo_pdf = SimpleDocTemplate(
        'Data Report.pdf',
        pagesize=(landscape(letter)),
        rightMargin=5,
        leftMargin=5,
        topMargin=10,
        bottomMargin=10)
    archivo_pdf.build(elements)
    print('Data Report Generated!')




for root, dirs, files in os.walk(outputDirectory, topdown=True):
    for file in files:
   
    	with open(outputDirectory+file, "r") as csvfile:
             CreatePDF()
             