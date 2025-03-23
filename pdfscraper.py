from pypdf import PdfReader
def pdf_scraper(pdf):
    reader = PdfReader(pdf)
    print(len(reader.pages))
    text=''
    for i in range(len(reader.pages)):
        
        page = reader.pages[i]
        text += ' '+page.extract_text()
    print(text)
    return text
