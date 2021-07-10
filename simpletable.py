from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("simple_table.pdf", pagesize=A4)
elements = []

import csv

with open('/Users/yningapp/Documents/automation/auto/outputdir/Aurora-Perf-Run-R4.csv', "r") as csvfile:
    data = list(csv.reader(csvfile))


t=Table(data,colWidths=[0.9*inch]*8, rowHeights=[0.4*inch] *79)
#colWidth = size * number of columns
#rowHeights= size * number of rows
elements.append(t)
doc.build(elements)