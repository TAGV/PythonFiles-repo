import PyPDF2 as pdf

# PDf are opened as binary files
with open("/home/myubuntu/Desktop/Tour.pdf","rb") as pdfobject:
    read_pdf = pdf.PdfFileReader(pdfobject)
    print(read_pdf.numPages)
    pageobj = read_pdf.getPage(0)           # Pages are indexed from zero
    #pageobj = pageobj.rotateClockwise(180)
    print(pageobj.extractText(),end=" ")

    print(read_pdf.isEncrypted)


