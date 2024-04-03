import PyPDF2
with open (r'C:\Users\piotr\Desktop\Python Bootcamp\Day 91\sample.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    print(page.extract_text(0))


