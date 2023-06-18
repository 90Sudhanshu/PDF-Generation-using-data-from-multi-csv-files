# __________***PDF Generation using data from multi csv files***__________


from fpdf import FPDF

pdf = FPDF(orientation='p', unit="mm", format="A4")


pdf.set_font(family="Arial", style="B", size=12)

import pandas as pd

df_pdf = pd.read_csv("Topics.csv", sep=",")  # importing data from 1st csv file

df_description = pd.read_csv("Description.csv", sep=";") # importing data from 2nd csv file

for index, row in df_pdf.iterrows():
    topic = row["Topic"]
    pdf.add_page()
    pdf.cell(w=0, h=12, txt=topic, border=0,ln=1)
    for index_description, row_description in df_description.iterrows():
        print(row_description)
        if topic == row_description["Top"]:
            content = row_description["Content"]
            pdf.multi_cell(w=0, h=10, txt=content, align="L")
            break


pdf.output("output.pdf")