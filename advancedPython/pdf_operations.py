# Merge Multiple PDFs into One
from PyPDF2 import PdfMerger  
PdfMerger().append("a.pdf"); PdfMerger().append("b.pdf"); PdfMerger().write("merged.pdf")

# 