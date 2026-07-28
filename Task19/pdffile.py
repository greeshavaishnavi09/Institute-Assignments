class PDFfile():
    def read(self):
        print("pdf file is read")

class Wordfile():
    def read(self):
        print("wordfile is read")

def open_file(file):
    file.read()

def display(file):
    file.read()

pfile = PDFfile()
word =  Wordfile()

display(pfile)
display(word)

