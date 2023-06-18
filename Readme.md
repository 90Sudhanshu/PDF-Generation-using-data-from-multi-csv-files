# PDF Generation using data from multi csv files

* Here we have used two csv files.
* Topics.csv is used for Title/topics.
* Description is used for related information to the topics.


## Code Explanation Below:

# __________***PDF Generation using data from multi csv files***__________

from fpdf import FPDF
import pandas as pd

# Creating PDF object with specified orientation, unit, and format
pdf = FPDF(orientation='p', unit="mm", format="A4")

# Setting the font for the PDF
pdf.set_font(family="Arial", style="B", size=12)

# Reading data from the first CSV file
df_pdf = pd.read_csv("Topics.csv", sep=",")

# Reading data from the second CSV file
df_description = pd.read_csv("Description.csv", sep=";")

# Iterating over rows in the first CSV file
for index, row in df_pdf.iterrows():
    topic = row["Topic"]
    
    # Adding a new page to the PDF
    pdf.add_page()
    
    # Adding a cell with the topic text to the PDF
    pdf.cell(w=0, h=12, txt=topic, border=0, ln=1)
    
    # Iterating over rows in the second CSV file
    for index_description, row_description in df_description.iterrows():
        if topic == row_description["Top"]:
            content = row_description["Content"]
            
            # Adding a multiline cell with the content text to the PDF
            pdf.multi_cell(w=0, h=10, txt=content, align="L")
            
            # Breaking the loop once a match is found
            break

# Saving the generated PDF document
pdf.output("output.pdf")

