#extract data from pdf
import pdfplumber
with pdfplumber.open('PDF.pdf')as pdf:
    for i in pdf.pages:
        print(i.extract_text())
        print(f'$$$$$$$$$$$$over{i.page_number}')

