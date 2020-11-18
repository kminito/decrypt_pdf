import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def decrypt_pdf(file_name):

    input_path = os.path.join(os.getcwd(), file_name)
    output_path = os.path.join(os.getcwd(), "decrypted_"+file_name)

    with open(input_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
        reader = PdfFileReader(input_file)

        writer = PdfFileWriter()

        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))
        
        writer.write(output_file)

if __name__ == "__main__":
    decrypt_pdf(os.sys.argv[1])