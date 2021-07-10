from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle, StyleSheet1
from reportlab.lib import colors
from reportlab.platypus import Frame, PageTemplate, KeepInFrame, Paragraph
from reportlab.lib.units import cm
from reportlab.platypus import (Table, TableStyle, BaseDocTemplate)

import csv

with open('/Users/yningapp/Documents/automation/auto/outputdir/promise-Perf-Run-R4.csv', "r") as csvfile:
    data = list(csv.reader(csvfile))

########################################################################

def create_pdf():
    """
    Create a pdf
    """

    # Create a frame
    text_frame = Frame(
        x1=3.00 * cm,  # From left
        y1=1.5 * cm,  # From bottom
        height=19.60 * cm,
        width=22.90 * cm,
        leftPadding=0 * cm,
        bottomPadding=0 * cm,
        rightPadding=0 * cm,
        topPadding=0 * cm,
        showBoundary=1,
        id='text_frame')

    styles = StyleSheet1()
    styles.add(ParagraphStyle(name='Breadpointlist_style',
                              alignment=TA_LEFT,
                              bulletFontSize=7,
                              bulletIndent=0,
                              endDots=None,
                              firstLineIndent=0,
                              fontSize=14,
                              justifyBreaks=0,
                              justifyLastLine=0,
                              leading=2.2,
                              leftIndent=4,
                              rightIndent=0,
                              spaceAfter=0,
                              spaceBefore=0,
                              textColor=colors.black,
                              wordWrap='LTR',
                              splitLongWords=True,
                              spaceShrinkage=0.05,
                              ))

    bps = ParagraphStyle('bps', parent=styles['Breadpointlist_style'])

    # Create a table
    test_table = []
    
    for i in range(11, 1, -1):
        column1data = Paragraph('Column_1 on row {i}', bps)
        column2data = Paragraph('Column_last on row {i}', bps)
        #data.append(['1','1','1','1','1',column1data, column2data])

    data_table = Table(data, 22.90 * cm / 8)

    data_table.setStyle(TableStyle([
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ]))
    """
    data_table.setStyle(TableStyle([

        ('ALIGN', (0, 0), (1, -1), 'RIGHT'),
        ('SIZE', (0, 0), (-1, -1), 7),
        ('LEADING', (0, 0), (-1, -1), 8.4),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.6),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.gray),
    ]))
"""
    test_table.append(data_table)
    test_table = KeepInFrame(0, 0, test_table, mode='shrink')

    # Building the story
    story = [test_table] # adding test_table table (alternative, story.add(test_table))

    # Establish a document
    doc = BaseDocTemplate("Example_output.pdf", pagesize=(landscape(letter)))

    # Creating a page template
    frontpage = PageTemplate(id='FrontPage',
                             frames=[text_frame]
                             )
    # Adding the story to the template and template to the document
    doc.addPageTemplates(frontpage)

    # Building doc
    doc.build(story)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    create_pdf() # Printing the pdf