import PyPDF2
info=[]
file_open=open('sample.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(file_open)
print(pdf_reader.getNumPages())
for i in range(pdf_reader.getNumPages()):
    text=pdf_reader.getPage(i)
    info.append(text.extractText())
print(info)
add_text=pdf_reader.getPage(1)
file_open.close()
#writing into pdf
pdf_writer=PyPDF2.PdfFileWriter()
pdf_writer.addPage(add_text)
f=open('sample1.pdf','wb')
pdf_writer.write(f)
f.close()


