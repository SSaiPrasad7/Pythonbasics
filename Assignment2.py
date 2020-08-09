import PyPDF2
import re
pattern=r"\d{3}"
file=open('Find_the_Phone_Number.pdf','rb')
file_read=PyPDF2.PdfFileReader(file)
file_read.getNumPages()
info=''
for i in range(file_read.getNumPages()):
    text=file_read.getPage(i)
    info=info+' '+text.extractText()
for match in re.finditer(pattern,info):
    print(match)
print(info[41791:41819])
