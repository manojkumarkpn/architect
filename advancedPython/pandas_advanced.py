# Auto-Generate PDF Reports from Excel
import pandas as pd; import pdfkit  
pdfkit.from_string(pd.read_excel("report.xlsx").to_html(), "summary.pdf")

# 