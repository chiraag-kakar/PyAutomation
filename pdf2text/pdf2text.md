# PDF 2 TEXT CONVERTOR 
Uses the PyPDF2 module for extracting text from PDF files.

## Installing Dependency
To install the PyPDF2 module, we can use pip command. Run the below pip command to
download the PyPDF2 module:

```python3
pip install PyPDF2
```

## Dependency Explained
---

For extracting text from a PDF file we will be using the *PdfFileReader class* which
is used to initialize *PdfFileReader object*, taking a stream parameter, in which we
will provide the file stream for the PDF file.


Once we have the *PdfFileReader object* ready, we can use its methods
like *getDocumentInfo()* to get the file information, or *getNumPages()* to get
the total number of pages in the PDF file.
Then we have the *getPage()* method to get the page from the PDF file using the page
index which starts from 0, and finally the *extractText()* method which is used
to extract the text from the PDF file page.

---
The PyPDF2 module can be used to perform many opertations on PDF files, such as:
* Reading the text of the PDF file, which we just did above
* Rotating a PDF file page by any defined angle
* Merging two or more PDF files at a defined page number.
* Appending two or more PDF files, one after another.
* Find all the meta information for any PDF file to get informations like
creator, author, date of creation, etc.
* We can even create a new PDF file using the text coming from some text file.




## Running the Code Snippet Locally
To run the project locally :
* Clone the git repo.
* Then from the terminal/ command prompt navigate to the pdf2text directory of the cloned repo.
* Run the *pdf2text.py* file using the following command:
```
python pdf2text.py
```
## Use Cases
* To convert scanned files in PDF format to text which can be stored in database for data collection.
* Scanning physical document like candidate resumes, and then reading text from it for analysis

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
