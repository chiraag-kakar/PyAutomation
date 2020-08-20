#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# importing PyPDF2 module for extracting text from PDF files.
from PyPDF2 import PdfFileReader

# open the PDF file 
# make sure the pdf file is in the same directory
# if the file is present in some other directory then one can provide the file path
pdfFile = open('pdf-file-name.pdf', 'rb')

# create PDFFileReader object to read the file
pdfReader = PdfFileReader(pdfFile)

# printing the title and name of the creator
print("PDF File name: " + str(pdfReader.getDocumentInfo().title))
print("PDF File created by: " + str(pdfReader.getDocumentInfo().creator))
print("- - - - - - - - - - - - - - - - - - - -")

# calculating the number of pages pdf consists of
numOfPages = pdfReader.getNumPages()

# running the for loop to convert pdf to text till the required no of pages
for i in range(0, numOfPages):
    print("Page Number: " + str(i))
    print("- - - - - - - - - - - - - - - - - - - -")
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
    print("- - - - - - - - - - - - - - - - - - - -")
    
# close the PDF file object
pdfFile.close()

