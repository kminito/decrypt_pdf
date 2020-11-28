import pikepdf

input_pdf = pikepdf.Pdf.open('test.pdf')
pdf = pikepdf.Pdf.new()

for n, page in enumerate(input_pdf.pages):
    pdf.pages.append(page)
    
pdf.save('test_decrypted.pdf')

